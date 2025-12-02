import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración para mejorar la visualización de los gráficos
sns.set_style('whitegrid')

# --- 1. Carga del Dataset ---
nombre_archivo = 'titanic.csv'
try:
    # Cargar el archivo con el nombre especificado
    df = pd.read_csv(nombre_archivo)
    print(f"✅ Dataset '{nombre_archivo}' cargado exitosamente.")
except FileNotFoundError:
    print(f"❌ Error: El archivo '{nombre_archivo}' no se encontró en el directorio actual.")
    print("Asegúrate de que el archivo 'titanic.csv' esté en la misma ubicación que tu script de Python.")
    exit()

# --- 2. Exploración Inicial ---
print("\n--- Exploración Inicial del Dataset ---")
print(f"Dimensiones del dataset: {df.shape}")
print("\nPrimeras 5 filas:")
print(df.head())
print("\nInformación de tipos de datos y valores nulos ANTES de la limpieza:")
# Muestra los valores nulos (NaN) por columna
print(df.isnull().sum())
print("-" * 30)

# --- 3. Limpieza y Preparación de Datos (Imputación y Feature Engineering) ---

# Renombrar las columnas largas para simplificar su uso
df.rename(columns={'Siblings/Spouses Aboard': 'SibSp',
                   'Parents/Children Aboard': 'Parch'}, inplace=True)

# Imputar 'Age': Rellenar valores nulos con la mediana
df['Age'].fillna(df['Age'].median(), inplace=True)

# **IMPORTANTE:** Se elimina la línea de 'Embarked' porque no existe en tu archivo CSV.

# Eliminar columnas no útiles. 'Cabin' y 'Ticket' no están en tu archivo, pero 'Name' sí.
# Eliminamos 'Name' por limpieza de datos
df.drop(['Name'], axis=1, inplace=True)

# Crear una nueva característica 'FamilySize' (tamaño de la familia)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Convertir 'Survived' a texto para mejor interpretación en gráficos
df['Survived_Label'] = df['Survived'].map({0: 'No Sobrevivió', 1: 'Sobrevivió'})
df.drop('Survived', axis=1, inplace=True) # Eliminamos la columna numérica original

# --- 4. Análisis Descriptivo (Estadísticas) ---
print("\n--- Análisis Descriptivo de variables numéricas ---")
print(df[['Age', 'Fare', 'FamilySize']].describe().T)

print("\n--- Tasa de Supervivencia General ---")
sobrevivencia_rate = df['Survived_Label'].value_counts(normalize=True) * 100
print(sobrevivencia_rate)

# --- 5. Visualizaciones Clave ---
print("\n--- Generando Visualizaciones Clave ---")

# 5.1 Supervivencia por Género
plt.figure(figsize=(7, 5))
sns.countplot(x='Sex', hue='Survived_Label', data=df, palette='viridis')
plt.title('Supervivencia por Género')
plt.xlabel('Género')
plt.ylabel('Número de Pasajeros')
plt.legend(title='Supervivencia')
plt.savefig('5_1_Supervivencia_por_Genero.png')
plt.close()

# 5.2 Supervivencia por Clase de Pasajero (Pclass)
plt.figure(figsize=(7, 5))
sns.countplot(x='Pclass', hue='Survived_Label', data=df, palette='magma')
plt.title('Supervivencia por Clase de Pasajero')
plt.xlabel('Clase de Pasajero (1=Primera, 2=Segunda, 3=Tercera)')
plt.ylabel('Número de Pasajeros')
plt.legend(title='Supervivencia')
plt.savefig('5_2_Supervivencia_por_Clase.png')
plt.close()

# 5.3 Distribución de Edad (Age) por Supervivencia
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='Age', hue='Survived_Label', fill=True, alpha=.5, palette='plasma')
plt.title('Distribución de Densidad de Edad por Supervivencia')
plt.xlabel('Edad')
plt.ylabel('Densidad')
plt.savefig('5_3_Distribucion_Edad.png')
plt.close()

# 5.4 Distribución de Tarifa (Fare) y Supervivencia
plt.figure(figsize=(7, 5))
sns.boxplot(x='Survived_Label', y='Fare', data=df, palette='cividis')
plt.title('Tarifa (Fare) vs. Supervivencia')
plt.xlabel('Supervivencia')
plt.ylabel('Tarifa Pagada')
plt.ylim(0, 200) # Limitar el eje Y para enfocarse en la mayoría de los datos
plt.savefig('5_4_Tarifa_vs_Supervivencia.png')
plt.close()

print("\n✅ Análisis y Gráficos completados. Revisa los archivos de imagen generados.")