from django.contrib import admin
from .models import Pembeli, Laptop, Membeli, DetailMembeli

# Kustomisasi model Pembeli di antarmuka admin
class PembeliAdmin(admin.ModelAdmin):
    list_display = ('idPembeli', 'nama', 'alamat')
    search_fields = ('nama', 'alamat')
    list_filter = ('alamat',)
    list_per_page = 10
    ordering = ('nama',)
    list_display_links = ('idPembeli', 'nama')

# Kustomisasi model Laptop di antarmuka admin 
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('idLaptop', 'namaLaptop', 'processor', 'storage', 'ram', 'layar', 'gpu', 'harga')
    search_fields = ('namaLaptop', 'processor', 'gpu', 'storage')
    list_filter = ('ram', 'gpu', 'processor')
    list_per_page = 10
    ordering = ('namaLaptop',)
    list_display_links = ('idLaptop', 'namaLaptop')
    fieldsets = (
        ('Informasi Utama', {
            'fields': ('namaLaptop', 'harga')
        }),
        ('Spesifikasi', {
            'fields': ('processor', 'ram', 'storage', 'gpu', 'layar'),
            'classes': ('collapse',)
        }),
    )

# Inline model untuk DetailMembeli
class DetailMembeliInline(admin.TabularInline):
    model = DetailMembeli
    extra = 1
    raw_id_fields = ('id_laptop',)
    
# Kustomisasi model Membeli di antarmuka admin
class MembeliAdmin(admin.ModelAdmin):
    list_display = ('id_membeli', 'id_pembeli', 'total_harga', 'tanggal_beli', 'jumlahPcs')
    search_fields = ('id_pembeli__nama', 'id_membeli')
    list_filter = ('tanggal_beli', 'id_pembeli')
    date_hierarchy = 'tanggal_beli'
    list_per_page = 10
    inlines = [DetailMembeliInline]
    raw_id_fields = ('id_pembeli',)

    def jumlahPcs(self, obj):
        return sum(detail.jumlahPcs for detail in obj.detailmembeli_set.all())
    jumlahPcs.short_description = 'Total Pcs'
    jumlahPcs.admin_order_field = 'jumlahPcs'

# Kustomisasi model DetailMembeli di antarmuka admin
class DetailMembeliAdmin(admin.ModelAdmin):
    list_display = ('id_membeli', 'id_laptop', 'jumlahPcs', 'subtotal')
    search_fields = ('id_membeli__id_membeli', 'id_laptop__namaLaptop')
    list_filter = ('id_membeli__tanggal_beli',)
    list_per_page = 10
    raw_id_fields = ('id_membeli', 'id_laptop')

# Registrasi model ke antarmuka admin
admin.site.register(Pembeli, PembeliAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Membeli, MembeliAdmin)
admin.site.register(DetailMembeli, DetailMembeliAdmin)


# Register your models here.
