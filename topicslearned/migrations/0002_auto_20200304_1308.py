# Generated by Django 3.0.3 on 2020-03-04 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topicslearned', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topics',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
    ]
