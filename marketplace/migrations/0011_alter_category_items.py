# Generated by Django 4.0 on 2021-12-29 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0010_alter_category_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='items',
            field=models.ManyToManyField(null=True, related_name='categories', to='marketplace.Item'),
        ),
    ]
