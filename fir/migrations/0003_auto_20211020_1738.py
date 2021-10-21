# Generated by Django 3.2.8 on 2021-10-20 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fir', '0002_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='person',
            name='user_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='Address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='Company',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='GST_Number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='Name',
            field=models.CharField(max_length=100),
        ),
    ]
