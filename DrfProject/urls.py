
from django.contrib import admin
from django.urls import path, include
from django.views.generic import (
                                    TemplateView,
                                    RedirectView
                                    )
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_protect
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_swagger_view(title='Heroes API')

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
        )
        ,
    path(
	'grappelli/',
	 include('grappelli.urls')
	)
	, # grappelli URLS
    path('',
    csrf_protect(
        TemplateView.as_view(
        template_name='main.html'
                        )
                )
        )
        ,
    path(
        'api/',
         include('RestApi.urls')
         )
         ,
    path(
        'api/',
         include('CascadeCat.urls')
         )
         ,
    path(
        'Vue/',
         include('VueApp.urls')
         )
         ,
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
      )
      ,
    path(
        'api/token/refresh/',
         TokenRefreshView.as_view(),
          name='token_refresh'
          )
          ,
     path(
    'api/auth/',
     include(
     'rest_framework.urls',
     namespace='rest_framework'
                 )
     )
         ,
    path(
        'schema/',
         schema_view
         )
         ,
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
