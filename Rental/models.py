from django.db import models

# Create your models here.
class Pemesanan(models.Model):
    nama_pemesan = models.CharField(max_length=255)
    mobil = models.CharField(max_length=255)
    tanggal_pemesanan = models.DateField()

    def __str__(self):
        return self.nama_pemesan

class Mobil(models.Model):
    jenis_mobil = models.CharField(max_length=255)
    lokasi = models.CharField(max_length=255)
    tersedia = models.BooleanField(default=True)


    def __str__(self):
        return self.jenis_mobil

class Keuangan(models.Model):
    pemesanan = models.CharField(max_length=255)
    total_pembayaran = models.DecimalField(max_digits=10, decimal_places=2)
    metode_pembayaran = models.CharField(max_length=255)
    
    def __str__(self):
        return self.pemesanan