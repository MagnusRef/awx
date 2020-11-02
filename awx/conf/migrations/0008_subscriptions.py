# Generated by Django 2.2.11 on 2020-08-04 15:19

import logging

from django.db import migrations

from awx.conf.migrations._subscriptions import clear_old_license, prefill_rh_credentials

logger = logging.getLogger('awx.conf.migrations')


def _noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0007_v380_rename_more_settings'),
    ]


    operations = [
        migrations.RunPython(clear_old_license, _noop),
        migrations.RunPython(prefill_rh_credentials, _noop)
    ]