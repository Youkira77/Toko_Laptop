# Generated by Django 5.1.1 on 2024-12-18 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('idLaptop', models.AutoField(primary_key=True, serialize=False)),
                ('namaLaptop', models.CharField(max_length=100, verbose_name='Nama Laptop')),
                ('processor', models.CharField(max_length=100, verbose_name='Processor')),
                ('storage', models.CharField(max_length=100, verbose_name='Storage')),
                ('ram', models.CharField(max_length=100, verbose_name='RAM')),
                ('layar', models.CharField(max_length=100, verbose_name='Layar')),
                ('gpu', models.CharField(max_length=100, verbose_name='GPU')),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Harga')),
            ],
            options={
                'verbose_name_plural': 'Laptop',
                'ordering': ['namaLaptop'],
            },
        ),
        migrations.CreateModel(
            name='Membeli',
            fields=[
                ('id_membeli', models.AutoField(primary_key=True, serialize=False)),
                ('total_harga', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Total Harga')),
                ('tanggal_beli', models.DateField(auto_now_add=True, verbose_name='Tanggal Pembelian')),
            ],
            options={
                'verbose_name_plural': 'Transaksi Pembelian',
                'ordering': ['-tanggal_beli'],
            },
        ),
        migrations.CreateModel(
            name='Pembeli',
            fields=[
                ('idPembeli', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=50, verbose_name='Nama Pembeli')),
                ('alamat', models.TextField(verbose_name='Alamat')),
            ],
            options={
                'verbose_name_plural': 'Pembeli',
            },
        ),
        migrations.CreateModel(
            name='DetailMembeli',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('jumlahPcs', models.PositiveIntegerField(default=1, verbose_name='Jumlah Pcs')),
                ('id_laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.laptop', verbose_name='Laptop')),
                ('id_membeli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.membeli', verbose_name='Transaksi Membeli')),
            ],
            options={
                'verbose_name_plural': 'Detail Pembelian',
                'ordering': ['id_membeli', 'id_laptop'],
            },
        ),
        migrations.AddField(
            model_name='membeli',
            name='id_pembeli',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pembeli', verbose_name='Pembeli'),
        ),
    ]