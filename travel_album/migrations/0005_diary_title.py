# Generated by Django 4.0.4 on 2023-02-04 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_album', '0004_remove_album_photo_alter_diary_prefecture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='タイトル'),
        ),
    ]