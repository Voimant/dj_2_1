from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photo')
    release_date = models.DateField()
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField(max_length=200)

    # TODO: Добавьте требуемые поля
    pass
