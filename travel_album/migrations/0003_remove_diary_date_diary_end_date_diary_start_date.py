# Generated by Django 4.0.4 on 2022-11-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_album', '0002_diary_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='date',
        ),
        migrations.AddField(
            model_name='diary',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='終了日'),
        ),
        migrations.AddField(
            model_name='diary',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='旅行開始日'),
        ),
    ]
