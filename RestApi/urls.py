from django.urls import include, path
from . import views
from django.contrib.auth.decorators import login_required
app_name = 'RestApi'

urlpatterns = [
        #find special Hero by its name or alias /?name
        path(
            'hero/',
            views.SingleHeroApi.as_view(),
            name='hero'
           )
           ,
           #GET all Heroes
        path(
             'hero/all',
             views.AllHeroesApi.as_view(),
             name='all-heroes'
        )
            ,
           #Test for Display models in django template
        path(
            'hero/as_template',
            views.AllHeroesTemplate.as_view(),
            name='all-heroes-as-template'
           )
           ,
        #search bunches of heroes by its name or alias /?q

        path(
              'hero/search/',
              views.SearchHeroApi.as_view(),
              name='search-heroes'
              )
              ,
        #Create a New Hero
        path(
              'hero/submit',
              views.SubmitHeroApi.as_view(),
              name='submit-heroes'
              )
          ,
          #for delete ; return tow parameter (name,flag)
          # flag(1) is for confirm delete
          #otherwise operation will fail
         path(
                'hero/delete',
                views.DeleteHeroApi.as_view(),
                name='submit-heroes'
                )
                ,
        #find special world by its name or discribtion /?world_name
        path(
              'world/',
              views.SingleWorldApi.as_view(),
              name='world'
              )
              ,
        #GET all worlds
        path(
              'world/all',
              views.AllWorldsApi.as_view(),
              name='all-worlds'
              )
              ,
]
