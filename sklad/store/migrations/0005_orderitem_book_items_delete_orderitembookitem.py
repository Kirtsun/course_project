# Generated by Django 4.1.5 on 2023-01-31 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_bookitem_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='book_items',
            field=models.ManyToManyField(to='store.bookitem'),
        ),
        migrations.DeleteModel(
            name='OrderItemBookItem',
        ),
    ]