# Generated by Django 4.2.4 on 2023-11-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='wikipedia_link',
            new_name='wikipedia_url',
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
