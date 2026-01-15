import pandas as pd
from sqlalchemy import create_engine
import os
import subprocess
import time
from datetime import datetime

# ================= CONFIGURACIÓN =================
SERVER = 'localhost'       
DB = 'SUPERMERCADO_JPV_V5'
VIEW = 'VISTA_ANALITICA_DETALLADA'
TIEMPO = 30                

# --- RUTA DE GIT (Ya configurada con tu dirección) ---
UBICACION_GIT = r"C:\Program Files\Git\cmd\git.exe"
# =====================================================

# Detectar carpeta actual
REPO_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_CSV = os.path.join(REPO_PATH, 'Sales_Data.csv')
FILE_XLSX = os.path.join(REPO_PATH, 'Sales_Data.xlsx')
FILE_JSON = os.path.join(REPO_PATH, 'Sales_Data.json')

def ejecutar_git(comando):
    """Función auxiliar para llamar a Git usando la ruta completa"""
    comando_completo = f'"{UBICACION_GIT}" {comando}'
    subprocess.run(comando_completo, shell=True, check=True)

def ciclo_robot():
    print(f"--- Iniciando ciclo: {datetime.now().strftime('%H:%M:%S')} ---")
    try:
        # 1. SQL
        conn_str = f"mssql+pyodbc://{SERVER}/{DB}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
        engine = create_engine(conn_str)
        df = pd.read_sql(f"SELECT * FROM {VIEW}", engine)
        
        # 2. Guardar Archivos
        df.to_csv(FILE_CSV, index=False, encoding='utf-8')
        df.to_excel(FILE_XLSX, index=False, engine='openpyxl')
        df.to_json(FILE_JSON, orient='records', date_format='iso', indent=4)
        print("✅ Archivos generados correctamente.")

        # 3. GitHub Push
        os.chdir(REPO_PATH)
        
        # Añadir archivos
        ejecutar_git("add .")
        
        # Verificar estado
        comando_status = f'"{UBICACION_GIT}" status --porcelain'
        status = subprocess.run(comando_status, shell=True, capture_output=True, text=True)
        
        if status.stdout.strip():
            print("📤 Detectados cambios, subiendo a la nube...")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ejecutar_git(f'commit -m "Auto-update {timestamp}"')
            ejecutar_git("push")
            print("🚀 ¡Subido a GitHub con éxito!")
        else:
            print("💤 No hay datos nuevos, esperando...")

    except subprocess.CalledProcessError as e:
        print(f"⚠️ Error de Git: {e}")
    except Exception as e:
        print(f"❌ Error General: {e}")

if __name__ == "__main__":
    print("🤖 ROBOT ACTIVO (Ctrl + C para salir)")
    # Verificación de seguridad
    if not os.path.exists(UBICACION_GIT):
        print(f"⛔ ERROR: Python no encuentra Git en: {UBICACION_GIT}")
        exit()
        
    while True:
        ciclo_robot()
        time.sleep(TIEMPO)