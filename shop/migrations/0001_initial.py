# Generated by Django 3.0.8 on 2020-08-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('product_desc', models.CharField(max_length=400)),
                ('product_date', models.DateField()),
                ('product_img', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
