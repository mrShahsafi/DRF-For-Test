from django.db import models



class World(models.Model):
    world_name = models.CharField(
                                'hero world',
                                max_length=255,
                                default='Real',
                                )
    about = models.TextField(
                            'hero discribtion',
                            max_length=1044,
                            default='no content',
                            )
    def __str__(self):
            return str(self.pk) + ':' + self.world_name

class Image(models.Model):
    image_name = models.CharField(
                                    max_length=256,
                                    default='Alt',
                                        )
    source = models.ImageField(
                                upload_to="hero/",
                                null=True,
                                blank=True
                                )

    def __str__(self):
        return self.image_name

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    world = models.ForeignKey(
                            World,
                            on_delete=models.CASCADE,
                            verbose_name = "Hero's world"
                            )
    image = models.ForeignKey(
                                Image,
                                on_delete=models.CASCADE,
                                verbose_name = "Hero's picture",
                                blank=True,
                                null=True,
                                )
    is_deleted = models.BooleanField(default = False)


    def __str__(self):
        return self.name + '-' + self.alias + '-' + self.world.world_name
