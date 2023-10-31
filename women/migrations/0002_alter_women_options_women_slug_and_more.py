# Generated by Django 4.2.6 on 2023-10-30 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['-time_create']},
        ),
        migrations.AddField(
            model_name='women',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AddIndex(
            model_name='women',
            index=models.Index(fields=['-time_create'], name='women_women_time_cr_9f33c2_idx'),
        ),
    ]
