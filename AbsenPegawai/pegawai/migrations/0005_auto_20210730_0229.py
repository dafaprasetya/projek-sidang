# Generated by Django 3.2.5 on 2021-07-29 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pegawai', '0004_post_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='kategori',
            field=models.CharField(choices=[('Hadir', 'Hadir'), ('Sakit', 'Sakit'), ('Izin', 'Izin'), ('Tanpa Keterangan', 'Tanpa Keterangan')], default='Hadir', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='nama',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='absenn', to=settings.AUTH_USER_MODEL),
        ),
    ]
