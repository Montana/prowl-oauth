"""
Prowl OAuth2 backend

"""
from social.backends.oauth import BaseOAuth2


class ProwlOAuth2(BaseOAuth2):
    name = 'prowl'
    AUTHORIZATION_URL = 'http://api.getprowl.com/oauth/authorize/'
    ACCESS_TOKEN_METHOD = 'POST'
    ACCESS_TOKEN_URL = 'http://api.getprowl.com/oauth/token/'
    REDIRECT_STATE = False

    def get_user_details(self, response):
        """Return user details from Prowl merchant account"""
        email = response['email']
        username = response['email']
        return {'username': username,
                'email': email}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json('http://api.getprowl.com/v0.1/user', headers={
            'Authorization': 'Bearer %s' % access_token
        })
