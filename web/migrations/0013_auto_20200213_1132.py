# Generated by Django 3.0.3 on 2020-02-13 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20200213_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrecord',
            name='apply_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='申请日期'),
        ),
    ]