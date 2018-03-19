# Generated by Django 2.0.3 on 2018-03-19 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siem', '0011_auto_20180317_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='limitrule',
            old_name='action_filter',
            new_name='action_filter_regex',
        ),
        migrations.RenameField(
            model_name='limitrule',
            old_name='command_filter',
            new_name='command_filter_regex',
        ),
        migrations.RenameField(
            model_name='limitrule',
            old_name='dest_host_filter',
            new_name='dest_host_filter_regex',
        ),
        migrations.RenameField(
            model_name='limitrule',
            old_name='dest_port_filter',
            new_name='dest_port_filter_regex',
        ),
        migrations.RenameField(
            model_name='limitrule',
            old_name='interface_filter',
            new_name='interface_filter_regex',
        ),
        migrations.RenameField(
            model_name='limitrule',
            old_name='log_source_filter',
            new_name='log_source_filter_regex',
        ),
        migrations.RenameField(
            model_name='limitrule',
            old_name='process_filter',
            new_name='process_filter_regex',
        ),
        migrations.RenameField(
            model_name='limitrule',
            old_name='rulename_filter',
            new_name='rulename_filter_regex',
        ),
        migrations.RenameField(
            model_name='limitrule',
            old_name='source_host_filter',
            new_name='source_host_filter_regex',
        ),
        migrations.RenameField(
            model_name='limitrule',
            old_name='source_port_filter',
            new_name='source_port_filter_regex',
        ),
        migrations.RenameField(
            model_name='limitrule',
            old_name='source_user_filter',
            new_name='source_user_filter_regex',
        ),
        migrations.RenameField(
            model_name='limitrule',
            old_name='target_user_filter',
            new_name='target_user_filter_regex',
        ),
        migrations.AddField(
            model_name='limitrule',
            name='parameters_filter_regex',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='limitrule',
            name='path_filter_regex',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='limitrule',
            name='referer_filter_regex',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='logevent',
            name='parameters',
            field=models.CharField(default='', max_length=384),
        ),
        migrations.AddField(
            model_name='logevent',
            name='path',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='logevent',
            name='referer',
            field=models.CharField(default='', max_length=384),
        ),
    ]
