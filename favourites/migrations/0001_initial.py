# Generated by Django 3.2.19 on 2023-05-16 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tutorials', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to='tutorials.tutorial')),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('owner', 'tutorial')},
            },
        ),
    ]
