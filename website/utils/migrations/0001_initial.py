# Generated by Django 2.1.7 on 2019-03-22 22:07

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenseSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('version', models.TextField(blank=True)),
                ('url', models.URLField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_handle', models.CharField(blank=True, help_text='Your Twitter username without the @, e.g. katyperry', max_length=255)),
                ('facebook_app_id', models.CharField(blank=True, help_text='Your Facebook app ID.', max_length=255)),
                ('default_sharing_text', models.CharField(blank=True, help_text='Default sharing text to use if social text has not been set on a page.', max_length=255)),
                ('site_name', models.CharField(blank=True, default='website', help_text='Site name, used by Open Graph.', max_length=255)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SystemMessagesSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_404', models.CharField(default='Page not found', max_length=255, verbose_name='Title')),
                ('body_404', wagtail.core.fields.RichTextField(default='<p>You may be trying to find a page that doesn&rsquo;t exist or has been moved.</p>', verbose_name='Text')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'system messages',
            },
        ),
    ]