from django.urls import path
from .views import CustomAuthToken
app_name - 'u'

urlpatterns += [
    path(
        'token-singup',
         CustomAuthToken.as_view(),
         name='token-singup'
         )
         ,
]
