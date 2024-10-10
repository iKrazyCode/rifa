from django.contrib import admin
from .models import Rifa, Comprador



class CompradorAdminInline(admin.TabularInline):
    model = Comprador
    extra = 1
    verbose_name = 'Comprador'
    verbose_name_plural = 'Compradores'


# Register your models here.
@admin.register(Rifa)
class RifaAdmin(admin.ModelAdmin):
    verbose_name = 'Rifa'
    verbose_name_plural = 'Rifas'
    list_display = ['titulo', 'valor_da_rifa', 'custom_fechada']
    list_display_links = ['titulo',]

    inlines = [CompradorAdminInline,]

    @admin.display(description='Status da Rifa')
    def custom_fechada(self, obj):
        if obj.fechada == True:
            if obj.vencedor == None:
                return f"Fechada - Nenhum vencedor selecionado"
            else:
                return f"Fechada - Vencedor: {obj.vencedor.nome}"
            
        else:
            return "Ativa"
    


