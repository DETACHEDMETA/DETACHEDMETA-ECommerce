# Generated by Django 4.0.5 on 2022-08-19 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_product_model_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_model',
            name='model',
            field=models.FileField(blank=True, null=True, upload_to='images/models/'),
        ),
    ]
