# Generated by Django 3.2.6 on 2021-09-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Time', models.TextField()),
                ('Log_Category', models.TextField()),
                ('Actual_Message', models.TextField()),
            ],
        ),
    ]