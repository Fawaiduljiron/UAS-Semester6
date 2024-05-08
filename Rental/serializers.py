from rest_framework import serializers
from .models import Pemesanan, Mobil, Keuangan

# buat kelas serializer
class PemesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pemesanan
        fields = ["nama_pemesan", "mobil", "tanggal_pemesanan"]

class MobilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobil
        fields = ["jenis_mobil", "lokasi", "tersedia"]

class KeuanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keuangan
        fields = ["pemesanan", "total_pembayaran", "motode_pembyaran"]
        