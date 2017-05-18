import json
import requests

from rest_framework.authtoken.models import Token
from django.core.urlresolvers import reverse
from django.contrib.auth import views as auth_views, authenticate
from django.core.management.base import BaseCommand, CommandError
from wger.core.models import UserProfile
from wger.core.models import User

from wger.core.models import ApiUser
from wger import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('new_username', type=str)
        parser.add_argument('new_email', type=str)

    def handle(self, **options):
        user = User.objects.filter(username=options['username']).first()
        if user:
            client = requests.session()
            client.get(settings.SITE_URL + '/user/login')
            csrftoken = client.cookies['csrftoken']
            response = requests.post(settings.SITE_URL + '/user/login',
                                     data={"username": options['username'],
                                           "password": options['password'],
                                           "csrfmiddlewaretoken": csrftoken})
            self.token, created = Token.objects.get_or_create(user=user)
            token = self.token.key
            print(token)
            if user.userprofile.adding_permissions == False:
                return 'No permisions for adding user'
            else:
                if response.status_code == 200:
                    if User.objects.filter(username=options['new_username'])\
                       or User.objects.filter(email=options['new_email']):
                        raise CommandError("Username or email provided is already in use")
                    else:
                        payload = {"username": options['new_username'],
                                   "password": '1234',
                                   "email": options['new_email'],
                                   "csrfmiddlewaretoken": csrftoken}
                        r = requests.post(settings.SITE_URL + '/api/v2/usercreation/',
                                          headers={
                                              'Authorization': 'Token ' + token,
                                              'content-type': 'application/json'},
                                          data=json.dumps(payload))
                        print(r.status_code)
                        new_user = User.objects.filter(username=options['new_username']).first()
                        new_user.userprofile.adding_permissions = False
                        new_user.userprofile.save()

                        return 'Successfully saved user'

                else:
                    raise CommandError("Incorrect password")
        else:
            raise CommandError("The username provided does not exist")
