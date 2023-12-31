# Generated by Django 4.2.5 on 2023-09-19 07:24

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
                ('user_name', models.CharField(max_length=200)),
                ('post_title', models.CharField(max_length=200)),
                ('post_content', models.TextField(default='Demo content')),
                ('date_published', models.DateField(blank=True, null=True)),
                ('user_profile_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
