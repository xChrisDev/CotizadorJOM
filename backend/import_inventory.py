"""
Script para importar datos de inventario categorizado a Django
Ejecutar desde la raíz del proyecto Django: python import_inventory.py
"""
import os
import sys
import django
import pandas as pd
from decimal import Decimal

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
django.setup()

from articles.models import Category, Family, Brand, Article, PriceType, ArticlePrice

# Definición de familias, categorías y marcas del script original
FAMILIAS = {
    'FILTRACION Y LUBRICACION': [
        'FILTROS ACEITE', 'FILTROS AIRE', 'FILTROS COMBUSTIBLE', 'FILTROS CABINA',
        'ACEITES MOTOR', 'FLUIDOS FRENOS', 'FLUIDOS TRANSMISION', 'GRASAS Y LUBRICANTES'
    ],
    'SISTEMA ELECTRICO Y ELECTRONICO': [
        'ILUMINACION', 'BATERIAS Y CARGA', 'FUSIBLES Y CONEXIONES', 
        'SENSORES Y SWITCHES', 'CABLEADO'
    ],
    'MOTOR Y SISTEMA DE ENFRIAMIENTO': [
        'SISTEMA ENCENDIDO', 'DISTRIBUCION', 'JUNTAS Y RETENES', 'REFACCIONES MOTOR',
        'SISTEMA ENFRIAMIENTO'
    ],
    'SISTEMA DE FRENOS': [
        'BALATAS Y ZAPATAS', 'COMPONENTES FRENOS', 'SISTEMA HIDRAULICO'
    ],
    'SUSPENSION, DIRECCION Y CHASIS': [
        'AMORTIGUADORES', 'ROTULAS Y TERMINALES', 'BUJES Y SOPORTES', 'DIRECCION'
    ],
    'TRANSMISION Y TREN MOTRIZ': [
        'EMBRAGUE', 'TRANSMISION MANUAL', 'TRANSMISION AUTOMATICA',
        'CARDAN Y HOMOCINETICA'
    ],
    'CARROCERIA Y ACCESORIOS': [
        'PROTECCION', 'ESPEJOS Y CALAVERAS', 'LIMPIEZA VISIBILIDAD',
        'ASIENTOS Y TAPICERIA', 'CLIMATIZACION'
    ],
    'SEGURIDAD INDUSTRIAL Y EPP': [
        'PROTECCION RESPIRATORIA', 'PROTECCION VISUAL', 'PROTECCION AUDITIVA', # --- CORREGIDO (era AUDITIVO)
        'PROTECCION CORPORAL', 'SEÑALIZACION'
    ],
    'HERRAMIENTAS Y EQUIPOS': [
        'HERRAMIENTAS MANUALES', 'HERRAMIENTAS ELECTRICAS', 
        'EQUIPO MEDICION', 'EQUIPO SOLDADURA'
    ],
    'SEGURIDAD Y EMERGENCIA': [
        'EXTINTORES', 'SEGURIDAD VEHICULAR'
    ],
    'QUIMICOS Y LIMPIEZA': [
        'QUIMICOS AUTOMOTRICES', 'LIMPIEZA'
    ],
    'FERRETERIA Y CONSTRUCCION': [
        'FERRETERIA', 'MATERIALES'
    ]
}

MARCAS = [
    'WD-40', 'BARDAHL', 'LOCTITE', 'TRUPER', '3M', 'CRC', 'MTR', 'DEVCON', 'LUCAS',
    'TF QUIMICA', 'QUIMIKLEAN', 'FRAM', 'UNIFIL', 'MOBIL', 'AKRON', 'HELLA',
    'ROLCAR', 'MEXLUB', 'REPSOL', 'VALVOLINE', 'FLEETGUARD', 'WIX', 'STP', 'ROADSTAR',
    'BOSCH', 'NGK', 'DENSO', 'STAR', 'IOL', 'TOTAL PARTS', 'VOLTECK',
    'ECCO', 'FIAMM', 'MSA', 'GATES', 'TIMKEN', 'LUK', 'SACHS', 'EXEDY',
    'KOYO', 'NACHI', 'FAI', 'MATZKA', 'LUSAC', 'YOKOMITSU',
    'RAYBESTOS', 'CARTEK', 'PROMAX', 'XTOP', 'CANO', 'FRITEC', 'BIOCERAMIC',
    'MOOG', 'SYD', 'KYB', 'GROB', 'TRACKONE', 'ISAKA', 'TKM', 'VALUE', 'TREAD SAVER',
    'NISSAN', 'FORD', 'CHEVROLET', 'VW', 'TOYOTA', 'MITSUBISHI', 'MOPAR',
    'DIFORZA', 'OPTIMO', 'HILFY', 'HIFLY', 'GO WEST', 'SOLDEN', 'MASTODON', 'VIBACO',
    'ANSELL', 'DERMACARE', 'DRYPRO', 'CLIFF', 'TAMARA', 'MAGNO', 'SANIVO',
    'MASTER LOCK', 'URREA', 'PRETUL', 'KLINTEK', 'SURTEK', 'FLUKE', 'MOTOROLA',
    'DOGOTULS', 'ACUARIO', 'SIKA', 'HOLCIM', 'CLEVITE', 'ITP CLASSIC', 'GENERICA'
]


def crear_tipos_precio():
    """Crear los 5 tipos de precio si no existen"""
    print("\n=== Creando tipos de precio ===")
    tipos = [
        ('LISTA', 'Precio de lista estándar'),
        ('DESCUENTO', 'Precio con descuento'),
        ('MAYOREO', 'Precio para mayoreo'),
        ('MINIMO', 'Precio mínimo de venta'),
        ('CREDITO', 'Precio para venta a crédito'),
    ]
    
    created_count = 0
    tipos_dict = {}
    
    for nombre, descripcion in tipos:
        obj, created = PriceType.objects.get_or_create(
            name=nombre,
            defaults={'description': descripcion}
        )
        tipos_dict[nombre] = obj
        if created:
            created_count += 1
            print(f"✓ Tipo de precio creado: {obj.name} (ID: {obj.id})") # Corregido para mostrar el nombre
        else:
            print(f"- Tipo de precio ya existe: {obj.name} (ID: {obj.id})") # Corregido para mostrar el nombre
    
    print(f"\nTotal tipos de precio creados: {created_count}")
    print(f"Total tipos de precio disponibles: {len(tipos_dict)}")
    return tipos_dict


def crear_familias():
    """Crear todas las familias"""
    print("\n=== Creando familias ===")
    created_count = 0
    familias_dict = {}
    
    for familia_nombre in FAMILIAS.keys():
        obj, created = Family.objects.get_or_create(name=familia_nombre)
        familias_dict[familia_nombre] = obj
        if created:
            created_count += 1
            print(f"✓ Familia creada: {familia_nombre} (ID: {obj.id})")
        else:
            print(f"- Familia ya existe: {familia_nombre} (ID: {obj.id})")
    
    # Crear familia genérica
    obj, created = Family.objects.get_or_create(name='GENERAL')
    familias_dict['GENERAL'] = obj
    if created:
        created_count += 1
        print(f"✓ Familia genérica creada: GENERAL (ID: {obj.id})")
    
    print(f"\nTotal familias creadas: {created_count}")
    print(f"Total familias disponibles: {len(familias_dict)}")
    return familias_dict


def crear_categorias():
    """Crear todas las categorías"""
    print("\n=== Creando categorías ===")
    created_count = 0
    categorias_dict = {}
    
    # Extraer todas las categorías únicas
    todas_categorias = set()
    for categorias_list in FAMILIAS.values():
        todas_categorias.update(categorias_list)
    
    for categoria_nombre in sorted(todas_categorias):
        obj, created = Category.objects.get_or_create(name=categoria_nombre)
        categorias_dict[categoria_nombre] = obj
        if created:
            created_count += 1
            print(f"✓ Categoría creada: {categoria_nombre} (ID: {obj.id})")
        else:
            print(f"- Categoría ya existe: {categoria_nombre} (ID: {obj.id})")
    
    # Crear categoría genérica
    obj, created = Category.objects.get_or_create(name='OTROS')
    categorias_dict['OTROS'] = obj
    if created:
        created_count += 1
        print(f"✓ Categoría genérica creada: OTROS (ID: {obj.id})")
    
    print(f"\nTotal categorías creadas: {created_count}")
    print(f"Total categorías disponibles: {len(categorias_dict)}")
    return categorias_dict


def crear_marcas():
    """Crear todas las marcas"""
    print("\n=== Creando marcas ===")
    created_count = 0
    marcas_dict = {}
    
    for marca_nombre in sorted(MARCAS):
        obj, created = Brand.objects.get_or_create(name=marca_nombre)
        marcas_dict[marca_nombre] = obj
        if created:
            created_count += 1
            print(f"✓ Marca creada: {marca_nombre} (ID: {obj.id})")
        else:
            print(f"- Marca ya existe: {marca_nombre} (ID: {obj.id})")
    
    print(f"\nTotal marcas creadas: {created_count}")
    print(f"Total marcas disponibles: {len(marcas_dict)}")
    return marcas_dict


def importar_articulos(csv_file, categorias_dict, familias_dict, marcas_dict, tipos_precio_dict):
    """Importar artículos desde el CSV generado"""
    print("\n=== Importando artículos desde CSV ===")
    
    try:
        # --- CAMBIO ---
        # Rellenar columnas clave vacías con una cadena vacía al cargar
        # Esto evita errores con pd.isna() en números que se interpretan como float
        df = pd.read_csv(csv_file).fillna({
            'SKU': '',
            'CLAVE_PRIMARIA': '',
            'CATEGORIA_ID': 0,
            'FAMILIA_ID': 0,
            'MARCA_ID': 0
        })
        print(f"✓ Archivo CSV cargado: {len(df)} registros encontrados")
    except FileNotFoundError:
        print(f"✗ Error: No se encontró el archivo '{csv_file}'")
        return
    except Exception as e:
        print(f"✗ Error al cargar CSV: {str(e)}")
        return
    
    # Estadísticas
    stats = {
        'creados': 0,
        'actualizados': 0,
        'errores': 0,
        'omitidos': 0,
        'sin_sku': 0
    }
    
    print("\nProcesando artículos...")
    for idx, row in df.iterrows():
        try:
            # Validar descripción (campo obligatorio)
            article_name = str(row.get('Descripción Producto', '')).strip() 
            if not article_name or pd.isna(row.get('Descripción Producto')):
                print(f"⚠ Fila {idx + 2}: Descripción vacía - OMITIDO")
                stats['omitidos'] += 1
                continue
            
            # --- CAMBIO PRINCIPAL: LÓGICA DE IDENTIFICADOR ÚNICO ---
            
            # 1. Priorizar SKU
            item_code = str(row.get('SKU', '')).strip()
            
            # 2. Si SKU está vacío, usar CLAVE_PRIMARIA como respaldo
            if not item_code:
                item_code = str(row.get('CLAVE_PRIMARIA', '')).strip()
                
                if item_code:
                    # Se usará CLAVE_PRIMARIA, contar como 'sin_sku' para estadísticas
                    stats['sin_sku'] += 1
                    if stats['sin_sku'] % 50 == 1: # Mostrar cada 50 para no saturar
                        print(f"ℹ Fila {idx + 2}: Sin SKU. Usando CLAVE_PRIMARIA ({item_code}) como identificador.")
                else:
                    # 3. Si ambos están vacíos, no podemos identificar el artículo
                    print(f"⚠ Fila {idx + 2}: Sin SKU ni CLAVE_PRIMARIA. No se puede identificar unívocamente - OMITIDO")
                    stats['omitidos'] += 1
                    continue
            
            # --- FIN DEL CAMBIO PRINCIPAL ---
            
            
            unit_of_measure = str(row.get('UM', 'PZA')).strip() if not pd.isna(row.get('UM')) else 'PZA'
            
            # Obtener IDs del CSV. Asegurarse de que no sean nulos.
            categoria_id = int(row.get('CATEGORIA_ID', 0))
            familia_id = int(row.get('FAMILIA_ID', 0))
            marca_id = int(row.get('MARCA_ID', 0))

            # Validar que los IDs existan (El ID 0 o nulo fallará la FK)
            if not categoria_id or not familia_id or not marca_id:
                print(f"⚠ Fila {idx + 2} (ID: {item_code}): IDs de Cat/Fam/Marca inválidos (Cat: {categoria_id}, Fam: {familia_id}, Mar: {marca_id}) - OMITIDO")
                stats['omitidos'] += 1
                continue

            # Crear o actualizar artículo
            # 'item_code' ahora es el SKU o la CLAVE_PRIMARIA
            article, created = Article.objects.update_or_create(
                item_code=item_code, 
                defaults={
                    'article_name': article_name,
                    'unit_of_measure': unit_of_measure,
                    'category_id': categoria_id, # Usar el ID numérico
                    'family_id': familia_id,     # Usar el ID numérico
                    'brand_id': marca_id         # Usar el ID numérico
                }
            )
            
            # Eliminar precios existentes si es actualización
            if not created:
                article.prices.all().delete()
            
            # Crear los 5 precios
            precios_data = [
                ('LISTA', row.get('PRECIO1', 0)),
                ('DESCUENTO', row.get('PRECIO2', 0)),
                ('MAYOREO', row.get('PRECIO3', 0)),
                ('MINIMO', row.get('PRECIO4', 0)),
                ('CREDITO', row.get('PRECIO5', 0)),
            ]
            
            for tipo_nombre, precio_valor in precios_data:
                try:
                    precio = Decimal(str(precio_valor)) if not pd.isna(precio_valor) else Decimal('0.00')
                    if precio < 0:
                        precio = Decimal('0.00')
                    
                    ArticlePrice.objects.create(
                        article=article,
                        price_type=tipos_precio_dict[tipo_nombre],
                        price=precio
                    )
                except Exception as e:
                    print(f"⚠ Error al crear precio {tipo_nombre} para {item_code}: {str(e)}")
            
            if created:
                stats['creados'] += 1
                if stats['creados'] % 100 == 0:
                    print(f"  Procesados: {stats['creados']} creados, {stats['actualizados']} actualizados...")
            else:
                stats['actualizados'] += 1
                if stats['actualizados'] % 100 == 0:
                    print(f"  Procesados: {stats['creados']} creados, {stats['actualizados']} actualizados...")
            
        except Exception as e:
            stats['errores'] += 1
            print(f"✗ Error en fila {idx + 2} (ID: {row.get('SKU', 'N/A')}): {str(e)}")
    
    # Resumen final
    print("\n" + "="*60)
    print("RESUMEN DE IMPORTACIÓN")
    print("="*60)
    print(f"✓ Artículos creados: 	 	 {stats['creados']}")
    print(f"↻ Artículos actualizados: 	 {stats['actualizados']}")
    print(f"ℹ Usando CLAVE_PRIMARIA: 	 {stats['sin_sku']} (Artículos sin SKU)")
    print(f"⚠ Artículos omitidos: 	 	 {stats['omitidos']} (Descripción vacía o sin ID único)")
    print(f"✗ Errores: 	 	 	 	 {stats['errores']}")
    print(f"─────────────────────────────────────")
    print(f"   TOTAL procesado (BD): 	 {stats['creados'] + stats['actualizados']}")
    print("="*60)


def main():
    """Función principal"""
    print("="*60)
    print("SCRIPT DE IMPORTACIÓN DE INVENTARIO")
    print("="*60)
    
    # Paso 1: Crear tipos de precio y mapearlos
    tipos_precio_dict = crear_tipos_precio()
    
    # Paso 2: Crear familias y mapearlas
    familias_dict = crear_familias()
    
    # Paso 3: Crear categorías y mapearlas
    categorias_dict = crear_categorias()
    
    # Paso 4: Crear marcas y mapearlas
    marcas_dict = crear_marcas()
    
    # Paso 5: Importar artículos desde CSV
    # --- CAMBIO: Apuntar al archivo CSV correcto
    csv_file = 'inventario.csv' 
    print(f"\n¿Importar artículos desde '{csv_file}'? (s/n): ", end='')
    respuesta = input().strip().lower()
    
    if respuesta == 's':
        importar_articulos(csv_file, categorias_dict, familias_dict, marcas_dict, tipos_precio_dict)
    else:
        print("Importación de artículos cancelada.")
    
    print("\n✅ ¡Proceso completado!")


if __name__ == '__main__':
    main()