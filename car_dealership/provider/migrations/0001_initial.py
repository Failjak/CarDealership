# Generated by Django 4.0.2 on 2022-02-06 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dealer', '0001_initial'),
        ('core', '0001_initial'),
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('change_date', models.DateField(auto_now=True, verbose_name='change_date')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='create_date')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('found_year', models.DateField(verbose_name='found_name')),
                ('car_prices', models.ManyToManyField(to='car.CarPrices', verbose_name='car_prices')),
                ('cars', models.ManyToManyField(to='car.Car', verbose_name='cars')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProviderToDealerOffer',
            fields=[
                ('offer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.offer')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('change_date', models.DateField(auto_now=True, verbose_name='change_date')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='create_date')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.dealer', verbose_name='dealer')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.provider', verbose_name='provider')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.offer', models.Model),
        ),
        migrations.CreateModel(
            name='ProviderDiscount',
            fields=[
                ('discount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.discount')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.provider', verbose_name='provider')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.discount', models.Model),
        ),
    ]
