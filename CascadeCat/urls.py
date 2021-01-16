from django.urls import path
from .views import SingleProductApi

app_name = 'CascadeCat'

urlpatterns = [

    path(
        'product/<id>',
         SingleProductApi.as_view(),
         name='porduct'
          )
          ,

]
