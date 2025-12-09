# 1. Clase Base para cualquier tipo de Dato (Encapsulamiento)
class DatoBase:
    """Clase base para encapsular un solo registro de datos."""
    def __init__(self, id_registro, timestamp, valor):
        # Atributos: Los datos del registro
        self.id_registro = id_registro
        self.timestamp = timestamp
        self._valor = valor  # Usamos '_' para indicar que es para uso interno (Encapsulamiento)

    def obtener_valor(self):
        """Método para obtener el valor del registro."""
        return self._valor
    
    def __str__(self):
        return f"ID: {self.id_registro}, Tiempo: {self.timestamp}, Valor: {self._valor}"

# 2. Clase Específica para Datos de Temperatura (Herencia)
class DatoTemperatura(DatoBase):
    """Clase hija que hereda de DatoBase y agrega lógica específica."""
    def __init__(self, id_registro, timestamp, valor, unidad="C"):
        # Llama al constructor de la clase padre
        super().__init__(id_registro, timestamp, valor)
        self.unidad = unidad

    # Polimorfismo: Sobreescribimos el método 'obtener_valor'
    def obtener_valor(self):
        """Devuelve el valor de la temperatura con su unidad."""
        return f"{self._valor} {self.unidad}"

# 3. Clase Procesador para manipular la colección de Objetos (Comportamiento)
class ProcesadorBigData:
    """Clase para manejar y procesar grandes colecciones de objetos DatoBase."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.registros = []

    def agregar_registro(self, registro):
        """Método para agregar un objeto de registro a la lista."""
        self.registros.append(registro)

    def calcular_promedio(self):
        """Calcula el valor promedio de todos los registros."""
        if not self.registros:
            return 0
        
        # Obtenemos los valores. Usamos el método 'obtener_valor' de cada objeto (Polimorfismo)
        # Aquí asumimos que todos los valores son numéricos para el cálculo.
        valores_numericos = []
        for reg in self.registros:
             # Intentamos obtener solo el número si es una cadena (como en DatoTemperatura)
            try:
                # Si es DatoTemperatura, obtener_valor devuelve "X C". Tomamos el X.
                valor_str = reg.obtener_valor().split()[0] 
                valores_numericos.append(float(valor_str))
            except ValueError:
                # Si es DatoBase, obtener_valor devuelve directamente el valor.
                valores_numericos.append(float(reg.obtener_valor()))
            except Exception:
                 # Manejar casos donde el valor no se puede convertir a float
                pass 
                
        if not valores_numericos:
            return 0
            
        return sum(valores_numericos) / len(valores_numericos)
        
    def mostrar_registros(self):
        """Imprime la información de todos los registros cargados."""
        print(f"\n--- Registros en {self.nombre} ---")
        for reg in self.registros:
            print(reg)

# --- Uso del Programa ---

# 1. Crear una instancia del procesador
procesador = ProcesadorBigData("Monitor de Sensores de Fábrica")

# 2. Crear objetos (datos)
dato_base_1 = DatoBase(id_registro="D001", timestamp="2025-12-09T10:00:00", valor=55.0)
temp_1 = DatoTemperatura(id_registro="T001", timestamp="2025-12-09T10:05:00", valor=22.5, unidad="C")
temp_2 = DatoTemperatura(id_registro="T002", timestamp="2025-12-09T10:10:00", valor=25.0, unidad="C")

# 3. Agregar los objetos al procesador
procesador.agregar_registro(dato_base_1)
procesador.agregar_registro(temp_1)
procesador.agregar_registro(temp_2)

# 4. Mostrar y procesar
procesador.mostrar_registros()

promedio = procesador.calcular_promedio()
print(f"\nEl valor promedio de todos los registros (numéricos) es: {promedio:.2f}")