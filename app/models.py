from prowlpy import prowl
from django.contrib.auth.models import User 
from django.db import models

def get_prowl_api(self):
  access_token = self.social_auth.all()[0].extra_data['access_token']
  return Prowl(access_token)

User.get_prowl_api = get_prowl_api

