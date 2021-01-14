from django.contrib import admin
from .models import (
                    Hero, World, Image
                        )
admin.site.register(Hero)
admin.site.register(World)
admin.site.register(Image)
