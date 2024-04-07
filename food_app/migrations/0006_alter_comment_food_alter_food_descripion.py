# Generated by Django 4.1.3 on 2024-04-07 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0005_remove_food_tag_alter_food_descripion_delete_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='food',
            field=models.ForeignKey(help_text='کامنت مدنظر برای کدوم غذاست', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='food_app.food', verbose_name='غذا'),
        ),
        migrations.AlterField(
            model_name='food',
            name='descripion',
            field=models.TextField(verbose_name='توضیحات غذا'),
        ),
    ]
