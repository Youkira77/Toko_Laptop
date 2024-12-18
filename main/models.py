from babel.numbers import format_currency
from django.db import models

# Model untuk Pembeli
class Pembeli(models.Model):
    idPembeli = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=50, verbose_name='Nama Pembeli', null=False)
    alamat = models.TextField(verbose_name='Alamat')

    class Meta:
        verbose_name_plural = 'Pembeli'

    def __str__(self):
        return f'{self.nama} - {self.alamat}'


# Model untuk Laptop 
class Laptop(models.Model):
    idLaptop = models.AutoField(primary_key=True)
    namaLaptop = models.CharField(max_length=100, verbose_name='Nama Laptop', null=False)
    processor = models.CharField(max_length=100, verbose_name='Processor', null=False)
    storage = models.CharField(max_length=100, verbose_name='Storage', null=False)
    ram = models.CharField(max_length=100, verbose_name='RAM', null=False)
    layar = models.CharField(max_length=100, verbose_name='Layar', null=False)
    gpu = models.CharField(max_length=100, verbose_name='GPU', null=False)
    harga = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Harga')

    class Meta:
        verbose_name_plural = 'Laptop'
        ordering = ['namaLaptop']

    def __str__(self):
        formatted_harga = format_currency(self.harga, 'IDR', locale='id_ID')
        return f'{self.namaLaptop} | {self.processor} | {self.ram} | {formatted_harga}'


# Model untuk Transaksi Pembelian
class Membeli(models.Model):
    id_membeli = models.AutoField(primary_key=True)
    total_harga = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Total Harga')
    tanggal_beli = models.DateField(verbose_name='Tanggal Pembelian', auto_now_add=True)
    id_pembeli = models.ForeignKey(Pembeli, on_delete=models.CASCADE, verbose_name='Pembeli')

    class Meta:
        verbose_name_plural = 'Transaksi Pembelian'
        ordering = ['-tanggal_beli']

    def __str__(self):
        formatted_harga = format_currency(self.total_harga, 'IDR', locale='id_ID')
        tanggal_format = self.tanggal_beli.strftime('%d %B %Y')
        return f'Transaksi {self.id_membeli} - {self.id_pembeli.nama} - {tanggal_format} - {formatted_harga}'


# Model untuk Detail Pembelian
class DetailMembeli(models.Model):
    id = models.AutoField(primary_key=True)
    id_laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, verbose_name='Laptop')
    id_membeli = models.ForeignKey(Membeli, on_delete=models.CASCADE, verbose_name='Transaksi Membeli')
    jumlahPcs = models.PositiveIntegerField(verbose_name='Jumlah Pcs', default=1)

    class Meta:
        verbose_name_plural = 'Detail Pembelian'
        ordering = ['id_membeli', 'id_laptop']

    def subtotal(self):
        return self.jumlahPcs * self.id_laptop.harga

    def __str__(self):
        formatted_subtotal = format_currency(self.subtotal(), 'IDR', locale='id_ID')
        return f'{self.id_membeli.id_pembeli.nama} - {self.id_laptop.namaLaptop} ({self.jumlahPcs} pcs) - {formatted_subtotal}'


# Create your models here.
