# Generated by Django 4.1.5 on 2023-01-24 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('quantity', models.IntegerField()),
                ('id_in_sklad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('CART', 'CART'), ('ORDERED', 'ORDERED'), ('SUCCESS', 'SUCCESS'), ('FAIL', 'FAIL')], default='CART', max_length=8)),
                ('delivery_address', models.CharField(max_length=150)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]