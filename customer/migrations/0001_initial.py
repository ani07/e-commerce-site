# Generated by Django 3.0.6 on 2020-05-30 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('organization', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=2)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('mobile', models.IntegerField(max_length=128)),
                ('address1', models.CharField(max_length=128)),
                ('address2', models.CharField(max_length=128)),
                ('address3', models.CharField(max_length=128)),
                ('address4', models.CharField(max_length=128)),
                ('zip', models.BigIntegerField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('person', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ref_payment_methods',
            fields=[
                ('payment_method_code', models.AutoField(primary_key=True, serialize=False)),
                ('payment_method_des', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='cust_payments_methods',
            fields=[
                ('cust_payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('card_number', models.CharField(max_length=24)),
                ('name_on_card', models.CharField(max_length=256)),
                ('expiry_date', models.DateField()),
                ('other_details', models.CharField(max_length=256)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customers')),
                ('payment_method_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.ref_payment_methods')),
            ],
        ),
    ]
