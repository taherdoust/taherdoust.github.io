# Generated by Django 4.2 on 2025-03-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('passage', models.TextField()),
                ('album', models.JSONField(default=list)),
                ('summary', models.TextField()),
                ('post_pic', models.URLField(blank=True, null=True)),
                ('classification', models.CharField(choices=[('professional', 'Professional Weblog'), ('social', 'Social Weblog'), ('portfolio', 'Portfolio'), ('personal', 'Personal Weblog'), ('coaching', 'Coaching Page')], max_length=20)),
                ('privacy', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=10)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
