# Generated by Django 3.0.7 on 2020-06-15 15:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import order.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+254 or '07'.", regex='^\\(?:254|\\+254|0)?(7(?:(?:[129][0-9])|(?:0[0-8])|(4[0-1]))[0-9]{6})$')])),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ORDER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, default=order.models.increment_order_id, editable=False, max_length=20, null=True)),
                ('payment_status', models.IntegerField(choices=[(0, 'Not Paid'), (2, 'Partial Paid'), (1, 'Paid')], default=0)),
                ('lock', models.BooleanField(default=False)),
                ('delivercost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created', '-id'),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('AV', 'AVAILABLE'), ('OUT', 'OUT OF STOCK'), ('CS', 'COMING SOON')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='order.Buyer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='order.Product')),
            ],
            options={
                'unique_together': {('buyer', 'product')},
            },
        ),
    ]
