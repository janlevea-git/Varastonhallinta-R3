# Generated by Django 4.0.3 on 2022-04-19 07:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('varasto', '0003_alter_varastotapahtuma_palautuspaiva_profiili'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profiili',
            options={'verbose_name': 'Profiili', 'verbose_name_plural': 'Profiilit'},
        ),
        migrations.AlterField(
            model_name='profiili',
            name='kuva',
            field=models.ImageField(default='oletus.jpg', upload_to='profiilikuvat'),
        ),
        migrations.AlterField(
            model_name='varastotapahtuma',
            name='palautuspaiva',
            field=models.DateField(default=datetime.datetime(2022, 5, 3, 7, 55, 2, 881390, tzinfo=utc), verbose_name='Palautuspäivä'),
        ),
    ]
