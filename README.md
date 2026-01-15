# 🚀 Fuente de la Verdad: Automatización SQL Server a BI

> **Sistema ETL Automatizado para democratizar datos empresariales**  
> Convierte tu SQL Server local en una fuente de datos universal accesible desde cualquier lugar.

---

## 📖 Introducción

**¿Qué es este proyecto?**

Este es un sistema de **ETL Automatizado (Extract, Transform, Load)** que funciona como un "Robot de Datos" inteligente. Su misión es tomar información almacenada en un servidor SQL Server local y transformarla en datos universales y accesibles para herramientas modernas de Business Intelligence como Power BI, aplicaciones web, dashboards móviles y análisis en Excel.

**¿Por qué existe?**

En muchas organizaciones, los datos valiosos están atrapados en bases de datos locales, inaccesibles para equipos remotos o herramientas en la nube. Este proyecto rompe esa barrera automatizando todo el proceso de extracción, transformación y sincronización.

---

## 🎯 Planteamiento del Problema

### Los desafíos que resuelve:

🔒 **Datos Encerrados**  
Los datos críticos del negocio viven en SQL Server local, inaccesibles para analistas remotos o herramientas cloud.

⏰ **Actualizaciones Manuales**  
Exportar datos manualmente consume tiempo valioso y genera errores humanos.

📊 **Incompatibilidad de Formatos**  
Power BI necesita CSV, los desarrolladores quieren JSON, y la gerencia usa Excel. Generar múltiples formatos es tedioso.

🔄 **Falta de Sincronización**  
Los reportes se desactualizan rápidamente y no reflejan la realidad del negocio en tiempo real.

🛠️ **Complejidad Técnica**  
Implementar pipelines ETL profesionales requiere infraestructura costosa y conocimientos especializados.

---

## ✨ La Solución

### Un Robot de Datos Inteligente

Este proyecto implementa un sistema automatizado que:

**🔍 Extrae**  
Conecta automáticamente a SQL Server y consulta las vistas configuradas.

**🔄 Transforma**  
Convierte los datos simultáneamente a tres formatos universales:
- **CSV** → Optimizado para Power BI y análisis ligero
- **JSON** → Perfecto para APIs y aplicaciones web
- **XLSX** → Listo para Excel y presentaciones ejecutivas

**☁️ Sincroniza**  
Detecta cambios y los sube automáticamente a GitHub, creando una fuente de verdad accesible globalmente.

**⚡ Automatiza**  
Se ejecuta en intervalos configurables (cada 30 segundos por defecto) sin intervención humana.

### Arquitectura Tecnológica

```
┌─────────────────┐
│  SQL Server     │  ← Base de datos local
│  (Local)        │
└────────┬────────┘
         │
         ↓ Extracción (Python + SQLAlchemy)
         │
┌────────┴────────┐
│  Robot de Datos │  ← Transformación Multi-formato
│  (robot_datos.py)│
└────────┬────────┘
         │
         ↓ Generación de Archivos
         │
┌────────┴────────────────────┐
│  Sales_Data.csv             │
│  Sales_Data.json            │  ← Formatos Universales
│  Sales_Data.xlsx            │
└────────┬────────────────────┘
         │
         ↓ Git Push Automático
         │
┌────────┴────────┐
│    GitHub       │  ← Fuente de la Verdad
│  (Repositorio)  │
└────────┬────────┘
         │
         ↓ Consumo Directo
         │
┌────────┴────────────────────┐
│ Power BI │ Apps Web │ Excel │  ← Herramientas de BI
└─────────────────────────────┘
```

---

## 🎁 ¿Qué Esperar?

### Beneficios Inmediatos

✅ **Datos Siempre Actualizados**  
Tus reportes de Power BI reflejan la realidad del negocio en tiempo casi real.

✅ **Acceso Universal**  
Cualquier persona con acceso al repositorio puede consumir los datos desde cualquier lugar del mundo.

✅ **Cero Mantenimiento Diario**  
Una vez configurado, el robot trabaja 24/7 sin supervisión.

✅ **Multi-Plataforma**  
Los mismos datos alimentan Power BI, aplicaciones móviles, dashboards web y reportes en Excel.

✅ **Historial de Cambios**  
Git mantiene un registro completo de cómo han evolucionado tus datos.

### Métricas de Rendimiento

| Métrica | Valor |
|---------|-------|
| ⚡ Frecuencia de actualización | Cada 30 segundos (configurable) |
| 📦 Formatos generados | 3 simultáneos (CSV, JSON, XLSX) |
| ☁️ Sincronización | Automática con GitHub |
| 🔧 Mantenimiento | Cero intervención diaria |

---

## 📋 Características Técnicas

### 🎯 Funcionalidades Principales

**Extracción Automática**  
Conecta a SQL Server Local (`SUPERMERCADO_JPV_V5`) usando Windows Authentication o credenciales configurables.

**Generación Multi-Formato**  
Produce simultáneamente:
- `Sales_Data.csv` → Optimizado para Power BI Web (ligero y rápido)
- `Sales_Data.json` → Para aplicaciones Web/Móviles (estructura API)
- `Sales_Data.xlsx` → Para usuarios de Excel/Gerencia (formato enriquecido)

**Sincronización Git Inteligente**  
Detecta cambios automáticamente y hace *Push* al repositorio solo cuando hay datos nuevos.

**Resiliencia y Recuperación**  
Configurado para encontrar rutas de Git en Windows y manejar errores de conexión sin fallar.

**Logging Detallado**  
Consola con emojis y mensajes claros para monitorear el estado en tiempo real.

### 🛠️ Stack Tecnológico

| Tecnología | Propósito |
|------------|-----------|
| 🐍 **Python 3.9+** | Motor de procesamiento |
| 🗄️ **SQL Server** | Base de datos origen |
| 📊 **Pandas** | Manipulación de datos |
| 🔗 **SQLAlchemy** | Conexión a base de datos |
| 📝 **OpenPyXL** | Generación de Excel |
| 🐙 **Git** | Control de versiones |
| ☁️ **GitHub** | Almacenamiento en la nube |
| 💼 **Power BI** | Visualización de datos |

---

## 🛠️ Requisitos Previos

Antes de comenzar, asegúrate de tener:

### Sistema Operativo
- ✅ Windows 10 o Windows 11

### Base de Datos
- ✅ SQL Server (Local o Remoto)
- ✅ Acceso a la base de datos configurada
- ✅ Una vista SQL creada con los datos a exportar

### Software Necesario
- ✅ Python 3.9 o superior ([Descargar](https://www.python.org/downloads/))
- ✅ Git for Windows ([Descargar](https://git-scm.com/download/win))
- ✅ Editor de código (VS Code recomendado)

### Conocimientos Básicos
- 📚 Uso de terminal/CMD
- 📚 Conceptos básicos de Git
- 📚 SQL básico (para crear vistas)

---

## ⚙️ Instalación y Configuración

Sigue estos pasos para levantar el proyecto en tu entorno:

### 📥 Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/JUANCITOPENA/FUENTE_DE_LA_VERDAD_DATOS_SQL_SERVER_AUTOMATIZADOS_CSV_XLSX_JSON_BI.git
cd FUENTE_DE_LA_VERDAD_DATOS_SQL_SERVER_AUTOMATIZADOS_CSV_XLSX_JSON_BI
```

### 🐍 Paso 2: Crear Entorno Virtual (Recomendado)

```bash
# Crear el entorno virtual
python -m venv venv

# Activar en Windows (CMD)
.\venv\Scripts\activate

# Activar en Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

### 📦 Paso 3: Instalar Dependencias

```bash
pip install pandas sqlalchemy pyodbc openpyxl
```

### 🔧 Paso 4: Configurar el Robot

Abre el archivo `robot_datos.py` y ajusta las variables de configuración:

```python
# ════════════════════════════════════════
# 📌 CONFIGURACIÓN DEL ROBOT
# ════════════════════════════════════════

SERVER = 'localhost'                 # Tu servidor SQL
DB = 'SUPERMERCADO_JPV_V5'           # Tu Base de Datos
VIEW = 'VISTA_ANALITICA_DETALLADA'   # La vista a consultar
TIEMPO = 30                          # Segundos entre actualizaciones

# RUTA DE GIT (Importante)
# Usa 'where git' en CMD para verificar la ubicación
UBICACION_GIT = r"C:\Program Files\Git\cmd\git.exe"
```

### 🔍 Paso 5: Verificar la Ruta de Git

Abre CMD o PowerShell y ejecuta:

```bash
where git
```

Copia la ruta que aparece y pégala en la variable `UBICACION_GIT` del script.

---

## 🚀 Uso del Sistema

### Iniciar el Robot

Con el entorno virtual activado, ejecuta:

```bash
python robot_datos.py
```

### Salida Esperada en Consola

```
🤖 ROBOT DE DATOS ACTIVO...
⏰ Sincronizando cada 30 segundos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Conectado a SQL Server
📊 Consultando: VISTA_ANALITICA_DETALLADA
📝 1,245 registros extraídos

💾 Generando archivos...
   ✓ Sales_Data.csv
   ✓ Sales_Data.json
   ✓ Sales_Data.xlsx

🔍 Detectando cambios en Git...
📤 Cambios encontrados, subiendo a GitHub...
🚀 ¡Subido a GitHub con éxito!

⏳ Esperando 30 segundos para la próxima actualización...
```

### Detener el Robot

Presiona `CTRL + C` en la terminal para detener el proceso de forma segura.

---

## 📊 Conexión con Power BI

### Método 1: URL Directa desde GitHub

1. Ve a tu repositorio en GitHub
2. Navega al archivo deseado (ej: `Sales_Data.csv`)
3. Haz clic en el botón **"Raw"**
4. Copia la URL completa del navegador

5. En Power BI Desktop:
   - `Obtener Datos` > `Web`
   - Pega la URL
   - Haz clic en **Aceptar**

### Método 2: Actualización Automática

Configura el refresco automático en Power BI Service:

1. Publica tu reporte a Power BI Service
2. Ve a Configuración del conjunto de datos
3. Configura **Actualización programada**
4. ¡Listo! Tus reportes se actualizan solos

### Ventajas de este Método

✅ Sin necesidad de Gateways empresariales  
✅ Datos accesibles desde cualquier lugar  
✅ Actualizaciones casi en tiempo real  
✅ Compatible con Power BI Free  

---

## 📂 Estructura del Proyecto

```
FUENTE_DE_LA_VERDAD/
│
├── 📄 Sales_Data.csv          # Datos crudos (Ligero, rápido)
├── 📄 Sales_Data.json         # Datos estructurados (API style)
├── 📄 Sales_Data.xlsx         # Datos formateados (Excel)
│
├── 🐍 robot_datos.py          # El cerebro de la automatización
├── 📖 README.md               # Esta documentación
│
├── 📁 venv/                   # Entorno virtual (ignorado por Git)
└── 📁 .git/                   # Historial de versiones
```

### Descripción de Archivos

| Archivo | Peso Aprox. | Propósito | Mejor Para |
|---------|-------------|-----------|------------|
| **CSV** | ~500 KB | Datos tabulares sin formato | Power BI, Python, R |
| **JSON** | ~800 KB | Datos estructurados jerárquicos | APIs, JavaScript, Apps |
| **XLSX** | ~400 KB | Datos formateados con estilos | Excel, Gerencia, Reportes |

---

## ⚠️ Solución de Problemas

### ❌ Error: `[WinError 2] The system cannot find the file specified`

**Causa:**  
Python no encuentra el ejecutable de Git.

**Solución:**
```bash
# 1. En CMD, ejecuta:
where git

# 2. Copia la ruta completa que aparece
# 3. Pégala en la variable UBICACION_GIT del script
UBICACION_GIT = r"C:\Program Files\Git\cmd\git.exe"
```

---

### ❌ Error: `ModuleNotFoundError: No module named 'pandas'`

**Causa:**  
No has activado el entorno virtual o no instalaste las librerías.

**Solución:**
```bash
# Activa el entorno virtual
.\venv\Scripts\activate

# Instala las dependencias
pip install pandas sqlalchemy pyodbc openpyxl
```

---

### ❌ Error: `Login failed for user`

**Causa:**  
Problema de autenticación con SQL Server.

**Solución:**
```python
# Si usas autenticación de Windows (recomendado):
engine = create_engine(f'mssql+pyodbc://{SERVER}/{DB}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes')

# Si usas usuario y contraseña:
engine = create_engine(f'mssql+pyodbc://usuario:password@{SERVER}/{DB}?driver=ODBC+Driver+17+for+SQL+Server')
```

---

### ❌ El Robot no sube cambios a GitHub

**Causa:**  
Puede que no estés autenticado en Git o no tengas permisos.

**Solución:**
```bash
# Verifica tu configuración de Git
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Si usas 2FA en GitHub, necesitas un Personal Access Token
# Genera uno en: GitHub > Settings > Developer settings > Personal access tokens
```

---

## 🔒 Seguridad y Mejores Prácticas

### 🛡️ Recomendaciones de Seguridad

**No subas credenciales al repositorio**  
Usa variables de entorno para información sensible:

```python
import os
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
```

**Repositorio Privado**  
Si tus datos son sensibles, mantén el repositorio como privado en GitHub.

**Permisos de Vista SQL**  
Crea una vista con solo los datos necesarios, nunca expongas tablas completas.

**Actualiza dependencias**  
Mantén tus librerías de Python actualizadas para evitar vulnerabilidades.

---

## 🚀 Próximas Mejoras

### Roadmap

- [ ] 📧 Notificaciones por email en caso de errores
- [ ] 🐳 Dockerización para despliegue fácil
- [ ] 📊 Dashboard web para monitoreo
- [ ] 🔐 Encriptación de archivos sensibles
- [ ] ⚡ Soporte para múltiples bases de datos
- [ ] 🌐 API REST para consultas en tiempo real

---

## 👨‍💻 Contribuciones

¿Quieres mejorar este proyecto? ¡Las contribuciones son bienvenidas!

1. Haz un Fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📞 Soporte y Contacto

**Autor:** Juancito Peña  
**GitHub:** [@JUANCITOPENA](https://github.com/JUANCITOPENA)  
**Licencia:** MIT

### ¿Necesitas ayuda?

- 🐛 Reporta bugs abriendo un [Issue](https://github.com/JUANCITOPENA/FUENTE_DE_LA_VERDAD_DATOS_SQL_SERVER_AUTOMATIZADOS_CSV_XLSX_JSON_BI/issues)
- 💡 Sugiere mejoras en las [Discussions](https://github.com/JUANCITOPENA/FUENTE_DE_LA_VERDAD_DATOS_SQL_SERVER_AUTOMATIZADOS_CSV_XLSX_JSON_BI/discussions)
- ⭐ Si te gustó el proyecto, ¡deja una estrella!

---

## 📜 Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para más detalles.

```
MIT License

Copyright (c) 2025 Juancito Peña

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
de este software y archivos de documentación asociados, para usar el software
sin restricciones, incluyendo sin limitación los derechos de usar, copiar,
modificar, fusionar, publicar, distribuir, sublicenciar y/o vender copias del
software, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas
las copias o porciones sustanciales del software.
```

---

<div align="center">

**🎉 ¡Gracias por usar Fuente de la Verdad!**

Si este proyecto te ayudó, considera darle una ⭐ en GitHub

[⬆ Volver arriba](#-fuente-de-la-verdad-automatización-sql-server-a-bi)

</div>
