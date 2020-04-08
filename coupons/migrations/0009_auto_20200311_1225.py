# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0008_auto_20180326_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, related_name='coupons', to='coupons.Campaign', verbose_name='Campaign', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='couponuser',
            name='coupon',
            field=models.ForeignKey(related_name='users', to='coupons.Coupon', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='couponuser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='User', on_delete=models.SET_NULL),
        ),
    ]
