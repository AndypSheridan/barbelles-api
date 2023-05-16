# Generated by Django 3.2.19 on 2023-05-16 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('tutorials', '0001_initial'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='tutorial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorials.tutorial'),
        ),
    ]
