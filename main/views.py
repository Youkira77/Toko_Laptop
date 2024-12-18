from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Sum, F
from .models import Membeli, DetailMembeli, Laptop, Pembeli
from datetime import datetime

def index(request):
    return render(request, 'main/index.html')

def laporan_pembelian(request):
    # Get filter parameters
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Base query with all necessary related data
    queryset = Membeli.objects.select_related('id_pembeli').prefetch_related(
        'detailmembeli_set',
        'detailmembeli_set__id_laptop'
    ).order_by('-tanggal_beli')

    # Apply date filters if provided
    if start_date:
        queryset = queryset.filter(tanggal_beli__gte=start_date)
    if end_date:
        queryset = queryset.filter(tanggal_beli__lte=end_date)

    # Calculate total transactions and total sales
    total_transaksi = queryset.count()
    total_penjualan = DetailMembeli.objects.filter(
        id_membeli__in=queryset
    ).aggregate(
        total=Sum(F('jumlahPcs') * F('id_laptop__harga'))
    )['total'] or 0

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 10)  # Show 10 items per page
    try:
        transaksi = paginator.page(page)
    except:
        transaksi = paginator.page(1)

    context = {
        'transaksi': transaksi,
        'total_transaksi': total_transaksi,
        'total_penjualan': total_penjualan,
        'start_date': start_date,
        'end_date': end_date,
    }

    return render(request, 'main/laporan_pembelian.html', context)

def laptop_list(request):
    laptops = Laptop.objects.all().order_by('namaLaptop')
    return render(request, 'laptop_list.html', {'laptops': laptops})

def pembeli_list(request):
    pembelis = Pembeli.objects.all().order_by('nama')
    return render(request, 'pembeli_list.html', {'pembelis': pembelis})

def membeli_detail(request, pk=None):
    if pk:
        membeli = get_object_or_404(Membeli, id_membeli=pk)
        details = membeli.detailmembeli_set.select_related('id_laptop').all()
    else:
        # Jika tidak ada PK, ambil transaksi terbaru
        membeli = Membeli.objects.select_related('id_pembeli').first()
        if membeli:
            details = membeli.detailmembeli_set.select_related('id_laptop').all()
        else:
            details = []

    context = {
        'membeli': membeli,
        'details': details,
    }
    return render(request, 'membeli_detail.html', context)