# Generated by Django 4.1.3 on 2022-12-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0004_tag_comment_food_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='tag',
        ),
        migrations.AlterField(
            model_name='food',
            name='descripion',
            field=models.TextField(max_length=100, verbose_name='توضیحات غذا'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
