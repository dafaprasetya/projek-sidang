# Generated by Django 3.2.5 on 2021-07-28 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pegawai', '0002_auto_20210728_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='nama',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
