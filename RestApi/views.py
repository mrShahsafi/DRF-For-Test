from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import (
                                login_required
                                            )
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import (
                            SingleHeroSerializer,
                            )

from .models import (Hero,
                        World
                        )
from ratelimit.decorators import ratelimit


class CheckSystemStatus(APIView):
#    @cache_page(60 * 15)
    def get(self,request,format=None):
        return Response(
                    {
                    'status':'GET method works'
                    }
                    ,
                    status=status.HTTP_200_OK
                )
#    @ratelimit(key='ip', rate='3/m')
    def post(self, request,format=None):
        return Response(
                    {
                    'status':'POST method works'
                    }
                    ,
                    status=status.HTTP_200_OK
                )

class SingleHeroByNameApi(APIView):
    def get(self,request,format=None):
        from django.db.models import Q
        try:
            get_hero_name = request.GET['name']
            my_hero = Hero.objects.filter(
                (
                Q(name__iexact=get_hero_name) | Q(alias__iexact=get_hero_name)
                )
                & Q(is_deleted=False)
                                        )
            if my_hero:
                serialized_data = SingleHeroSerializer(
                                                my_hero,
                                                many=True
                                                        )
                data =  serialized_data.data

                return Response(
                            {
                            'data':data
                            }
                            ,
                            status=status.HTTP_200_OK
                        )
            else:
                return Response(
                            {
                                'status':"File your looking for not found"
                                }
                                ,
                                 status=status.HTTP_404_NOT_FOUND
                                 )
        except:
            return Response(
            {
                'message':"Wrong request,please insert name /api/hero/?name=''"
                }
                ,status=status.HTTP_400_BAD_REQUEST)

class SingleHeroByPkApi(APIView):
    def get(self, request, id):
        my_hero = Hero.objects.filter(pk=id)
        if my_hero:
            serialized_data = SingleHeroSerializer(
                                            my_hero,
                                            many=True
                                                    )
            data =  serialized_data.data

            return Response(
                        {
                        'data':data
                        }
                        ,
                        status=status.HTTP_200_OK
                    )
        else:
            return Response(
                        {
                            'status':"File your looking for not found"
                            }
                            ,
                             status=status.HTTP_404_NOT_FOUND
                             )

    def post(self,request,id):
        return Response(
            {'status':'GET only accepted, passed id='+str(id)+'.'}
            ,
            status=status.HTTP_405_METHOD_NOT_ALLOWED
            )


class AllHeroesApi(APIView):
    def get(self,request,format=None):
        try:
            all_heroes = Hero.objects.filter(is_deleted=False)
            data  = []

            for hero in all_heroes:
                data.append({
                    'name is':hero.name
                    ,
                    'alias is':hero.alias
                    ,
                    'world is':hero.world.world_name
                    ,
                })

            return Response(
                        {
                        'data':data
                        }
                        ,
                        status=status.HTTP_200_OK
                    )
        except:
            return Response(
                        {
                        'status':"internal server Error"
                        }
                        ,
                         status=status.HTTP_500_INTERNAL_SERVER_ERROR
                         )


    def post(self,request,format=None):
        return Response(
                    {
                    'status':"Pemission denied!"
                    }
                    ,
                     status=status.HTTP_403_FORBIDDEN
                     )


class SearchHeroApi(APIView):
    def get(self,request,format=None):
        from django.db.models import Q
        get_hero       = request.GET['q']
        searched_hero = Hero.objects.filter(
            (
            Q(name__icontains=get_hero) | Q(alias__icontains=get_hero)
            )
            & Q(is_deleted=False)
                                        )
        print('pass'+str(searched_hero))
        data        =[]
        if searched_hero:
            for hero in searched_hero:
                data.append({
                        'name is':hero.name
                        ,
                        'alias is':hero.alias
                        ,
                        'world is':hero.world.world_name
                        ,
                        })


            return Response(
                            {
                            'data':data
                            }
                            ,
                            status=status.HTTP_200_OK
                            )
        else:
            return Response(
                        {
                            'status':"File your looking for not found"
                            }
                            ,
                             status=status.HTTP_404_NOT_FOUND
                             )
class SubmitHeroApi(APIView):
#    permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        return Response(
        {'status':'POST only accepted'},
        status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
    def post(self,request,format=None):
        import json
        #from rest_framework.parsers import JSONParser
        data = json.dumps(request.data)
        ToJsonData = json.loads(data)
        name = ToJsonData["name"]
        alias  = ToJsonData["alias"]
        world_id = ToJsonData["world_id"]
        '''serializer = SubmitHeroSerializer(data=data)
        print(serializer)
        #print(serializer.data)
        if serializer.is_valid():
            for attrebiute in serializer.data:
                name = attrebiute.get('name')
                alias = attrebiute.get('alias')
                #itst better to do not serialize ForeignKey by it's character data
                #because of other keyword's languages type
                world_id = attrebiute.data.get('world_id')
            #get Hero's world ForeignKey's pk
            world = World.objects.get(id=world_id)
            hero = Hero()
            hero.name = name
            hero.alias = alias
            #we calculate world type by world id & new we can user world object
            hero.world = world'''
        world  = World.objects.get(id=world_id)
        try:
            hero = Hero.objects.create(name=name, alias=alias, world=world)
            hero.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(
                        {
                        'data':'Hero Saved'
                        }
                        ,
                        status=status.HTTP_200_OK
                    )

'''        if serializer.error_messages:
            return Response(
            {'message':serializer.error_messages},
            status=status.HTTP_400_BAD_REQUEST
            )
'''

class DeleteHeroApi(APIView):
#    permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def post(self,request,format=None):
        import json
        data = json.dumps(request.data)
        ToJsonData = json.loads(data)
        DeleteRequest = ToJsonData['flag']
        HeroName      =  ToJsonData['name']
        if DeleteRequest=='1':
            try:
                target_hero = Hero.objects.get(name=HeroName)
                if target_hero:
                    target_hero.is_deleted = 1
                    target_hero.save()
                    return Response(
                        {'status':' The hero '+HeroName+' has been deleted :('}
                        ,
                        status=status.HTTP_200_OK
                        )
                else:
                    return Response(
                        {'message':'You are trying delete nonexistent hero.'}
                        ,
                        status=status.HTTP_404_NOT_FOUND)
            except:
                return Response(
                    {'message':'You are trying delete nonexistent hero.'}
                    ,
                    status=status.HTTP_404_NOT_FOUND
                    )

        else:
            return Response(
                {'fatal':'Wrong falg'}
                ,
                status=status.HTTP_400_BAD_REQUEST)


class SingleWorldApi(APIView):
    def get(self,request,format=None):
        from django.db.models import Q

        get_world_name = request.GET['world_name']
        query = World.objects.filter(
                Q(world_name__iexact=get_world_name
                    )
                    |Q(about__iexact=get_world_name)
                )
        if query:
            data  = []
            for world in query:
                data.append({
                "world's name":world.world_name
                ,
                'discribtion ':world.about
                ,
                })

            return Response(
                {'data':data}
                ,
                status=status.HTTP_200_OK
                )
        else:
            return Response(
            {'status':'The world you are looking for is not available'}
            ,
            status=status.HTTP_404_NOT_FOUND
            )
    def post(self,request,format=None):
        return Response(
                    {
                    'status':"Pemission denied!"
                    }
                    ,
                     status=status.HTTP_403_FORBIDDEN
                     )

class AllWorldsApi(APIView):
    def get(self, request,format=None):
        all_worlds = World.objects.all().order_by('world_name')
        data = []
        if all_worlds:
            for world in all_worlds:
                data.append({
                    'name':world.world_name
                    ,
                    "world's number":world.pk
                })
            return Response(
                {'data':data}
                ,
                status=status.HTTP_200_OK
                )
        return Response(
            {'message':'Sorry,there is no worlds available yet.please cone back later.'}
            ,
            status=status.HTTP_404_NOT_FOUND
            )
    def post(self, request,format=None):
        pass


#jus test for return query in django template
from django.http import HttpResponse
class AllHeroesTemplate(View):
    def get(self, request, *args, **kwargs):
        all_heroes = Hero.objects.all()
        context = {
        'all_heroes':all_heroes,
        }

        return render(request,
                        'heroes.html',
                        context
                        )
