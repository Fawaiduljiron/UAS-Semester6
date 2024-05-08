from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Pemesanan, Mobil, Keuangan
from .serializers import PemesananSerializer, MobilSerializer, KeuanganSerializer

# Create your views here.
@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Pemesanan_list(request, format=None):

    if request.method == 'GET':
        Pemesanan = Pemesanan.objects.all()
        serializer = PemesananSerializer(Pemesanan, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PemesananSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Pemesanan_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Pemesanan = Pemesanan.objects.get(pk=pk)
    except Pemesanan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PemesananSerializer(Pemesanan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PemesananSerializer(Pemesanan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Pemesanan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Mobil_list(request, format=None):

    if request.method == 'GET':
        Mobil = Mobil.objects.all()
        serializer = MobilSerializer(Mobil, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MobilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Mobil_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Mobil = Mobil.objects.get(pk=pk)
    except Mobil.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MobilSerializer(Mobil)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MobilSerializer(Mobil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Mobil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Keuangan_list(request, format=None):

    if request.method == 'GET':
        Keuangan = Keuangan.objects.all()
        serializer = KeuanganSerializer(Keuangan, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = KeuanganSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Keuangan_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Keuangan = Keuangan.objects.get(pk=pk)
    except Keuangan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Keuangan(Keuangan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Keuangan(Keuangan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Keuangan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PemesananDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Pemesanan.objects.get(pk=pk)
        except Pemesanan.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        Pemesanan = self.get_object(pk)
        serializer = PemesananSerializer(Pemesanan)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        Pemesanan = self.get_object(pk)
        serializer = PemesananSerializer(Pemesanan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Pemesanan = self.get_object(pk=pk)
        Pemesanan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MobilDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Mobil.objects.get(pk=pk)
        except Mobil.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        Mobil = self.get_object(pk)
        serializer = MobilSerializer(Mobil)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        Mobil = self.get_object(pk)
        serializer = MobilSerializer(Mobil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Mobil = self.get_object(pk=pk)
        Mobil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class KeuanganDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Keuangan.objects.get(pk=pk)
        except Keuangan.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        Keuangan = self.get_object(pk)
        serializer = KeuanganSerializer(Keuangan)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        Keuangan = self.get_object(pk)
        serializer = KeuanganSerializer(Keuangan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Keuangan = self.get_object(pk=pk)
        Keuangan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)