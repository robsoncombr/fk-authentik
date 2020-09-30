# Generated by Django 3.1.1 on 2020-09-30 08:10

from django.apps.registry import Apps
from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor

SCOPE_PB_PROXY_EXPRESSION = """return {
    "pb_proxy": {
        "user_attributes": user.group_attributes()
    }
}"""


def create_proxy_scope(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    from passbook.providers.proxy.models import SCOPE_PB_PROXY, ProxyProvider

    ScopeMapping = apps.get_model("passbook_providers_oauth2", "ScopeMapping")

    ScopeMapping.objects.update_or_create(
        scope_name=SCOPE_PB_PROXY,
        defaults={
            "name": "Autogenerated OAuth2 Mapping: passbook Proxy",
            "scope_name": SCOPE_PB_PROXY,
            "description": "",
            "expression": SCOPE_PB_PROXY_EXPRESSION,
        },
    )

    for provider in ProxyProvider.objects.all():
        provider.set_oauth_defaults()
        provider.save()


class Migration(migrations.Migration):

    dependencies = [
        ("passbook_providers_proxy", "0007_auto_20200923_1017"),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxyprovider',
            name='internal_host_ssl_validation',
            field=models.BooleanField(
                default=True, help_text='Validate SSL Certificates of upstream servers', verbose_name='Internal host SSL Validation'),
        ),
        migrations.AddField(
            model_name='proxyprovider',
            name='basic_auth_enabled',
            field=models.BooleanField(
                default=False, help_text='Set a custom HTTP-Basic Authentication header based on values from passbook.', verbose_name='Set HTTP-Basic Authentication'),
        ),
        migrations.AddField(
            model_name='proxyprovider',
            name='basic_auth_password_attribute',
            field=models.TextField(
                blank=True, help_text='User Attribute used for the password part of the HTTP-Basic Header.', verbose_name='HTTP-Basic Password'),
        ),
        migrations.AddField(
            model_name='proxyprovider',
            name='basic_auth_user_attribute',
            field=models.TextField(
                blank=True, help_text="User Attribute used for the user part of the HTTP-Basic Header. If not set, the user's Email address is used.", verbose_name='HTTP-Basic Username'),
        ),
        migrations.RunPython(create_proxy_scope),
    ]
