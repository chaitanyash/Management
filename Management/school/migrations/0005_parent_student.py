# Generated by Django 2.0.8 on 2018-08-23 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0004_auto_20180823_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.BigIntegerField(max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('contact', models.BigIntegerField(max_length=10)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Parent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
