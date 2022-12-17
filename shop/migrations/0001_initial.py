# Generated by Django 4.1.4 on 2022-12-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('stock', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image_url', models.URLField()),
            ],
        ),
    ]