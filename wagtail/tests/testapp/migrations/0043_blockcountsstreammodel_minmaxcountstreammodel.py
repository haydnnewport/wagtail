# Generated by Django 2.1.7 on 2019-03-28 02:30

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0042_simplechildpage_simpleparentpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockCountsStreamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock()), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])),
            ],
        ),
        migrations.CreateModel(
            name='MinMaxCountStreamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock()), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])),
            ],
        ),
    ]
