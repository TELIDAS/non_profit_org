# Generated by Django 3.1.6 on 2021-02-12 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_npo', '0006_auto_20210211_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsimage',
            name='news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='news_npo.news'),
        ),
    ]
