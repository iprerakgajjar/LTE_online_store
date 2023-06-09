# Generated by Django 3.0.7 on 2020-08-17 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(max_length=2000)),
                ('fname', models.CharField(max_length=500)),
                ('lname', models.CharField(max_length=500)),
                ('email', models.CharField(default='', max_length=800)),
                ('address1', models.CharField(default='', max_length=800)),
                ('address2', models.CharField(default='', max_length=800)),
                ('phone', models.CharField(default='', max_length=800)),
                ('state', models.CharField(max_length=500)),
                ('city', models.CharField(default='', max_length=500)),
                ('zip', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
