# Generated by Django 3.0 on 2020-12-22 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201222_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='glow',
            old_name='author',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='glow',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
