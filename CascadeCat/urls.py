from django.urls import path
from .views import Product

app_name = 'CascadeCat'

urlpatterns = [

    path(
        'product/<slug>',
         Product.as_view(),
         name='home'
          )
          ,

]
