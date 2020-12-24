# Generated by Django 3.1.4 on 2020-12-25 15:32

from django.db import migrations, models
import message.models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_status',
            field=models.CharField(choices=[(message.models.MessageStatus['CREATED'], 'Created'), (message.models.MessageStatus['SENT'], 'Sent'), (message.models.MessageStatus['DELIVERED'], 'Delivered'), (message.models.MessageStatus['READ'], 'Read'), (message.models.MessageStatus['FAILED'], 'Failed')], default='Created', max_length=50),
            preserve_default=False,
        ),
    ]
