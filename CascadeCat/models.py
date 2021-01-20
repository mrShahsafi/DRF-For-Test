from django.db import models

class SubCategory(models.Model):
    name = models.CharField(
                'category name',
                max_length=255,
                default='null'
                )

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(
                'category name',
                max_length=255,
                default='null'
                )
    has_subcategory = models.BooleanField(default=False)
    sub_category = models.ManyToManyField(
                SubCategory,
                verbose_name='sub category',
                )
    def __str__(self):
        return self.name


from django.utils.text import slugify
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(
                'name',
                 max_length=256,
                 default='Product',
                 )

    barcode = models.IntegerField(
                'barcode',
                default=0000,
                )

    category = models.ManyToManyField(
                    Category,
                    verbose_name='Category',
                    )
    sub_category = models.ManyToManyField(
                    SubCategory,
                    verbose_name='Sub-Category',
                    )
    slug = models.SlugField(
                    editable=False,
                    max_length=255,
                    default=None,
                    )#-batmans-cape123456789

    def get_absolute_url(self):
        return reverse('CascadeCat:product',
                       kwargs=
                       {
                           'slug': self.slug
                       }
                       )

    def save(self, *args, **kwargs):
        name = str(self.name)
        code = str(self.barcode)
        self.slug = slugify(
                '-' + name + code,
                allow_unicode=True
                )

        super().save(*args, **kwargs)
    def __str__(self):
        return self.name + ' - '+ str(self.barcode)
