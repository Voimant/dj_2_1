# Generated by Django 4.2.1 on 2023-06-02 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='photo')),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(null=True)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
    ]
