# Generated by Django 2.0.9 on 2019-01-07 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20190104_1426'),
        ('images', '0003_customimage_license'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customimage',
            name='alt',
        ),
        migrations.RemoveField(
            model_name='customimage',
            name='credit',
        ),
        migrations.AddField(
            model_name='customimage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.PersonPage'),
        ),
        migrations.AddField(
            model_name='customimage',
            name='description',
            field=models.TextField(blank=True, max_length=165),
        ),
        migrations.AddField(
            model_name='customimage',
            name='image_source_url',
            field=models.URLField(blank=True),
        ),
    ]
