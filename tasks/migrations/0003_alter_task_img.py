# Generated by Django 5.1.3 on 2024-11-24 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_img_alter_task_datecompleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_deb/'),
        ),
    ]