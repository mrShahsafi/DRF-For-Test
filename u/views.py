from rest_framework.authentication import TokenAuthentication
#from rest_auth.registration.views import LoginView

class LoginViewCustom(LoginView):
    authentication_classes = (TokenAuthentication,)
