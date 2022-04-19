# Generated by Django 4.0.3 on 2022-04-19 07:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('varasto', '0002_alter_varastotapahtuma_aikaleima_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varastotapahtuma',
            name='palautuspaiva',
            field=models.DateField(default=datetime.datetime(2022, 5, 3, 7, 38, 53, 293575, tzinfo=utc), verbose_name='Palautuspäivä'),
        ),
        migrations.CreateModel(
            name='Profiili',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kuva', models.ImageField(default='default.jpg', upload_to='profiilikuvat')),
                ('kayttaja', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
