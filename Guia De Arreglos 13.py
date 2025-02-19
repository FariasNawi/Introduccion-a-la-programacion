temperaturas = [22.5, 30.1, 18.9, 25.4, 28.3, 20.0, 15.2, 24.7, 26.8, 19.5]
volumenes = [10.5, 12.3, 9.8, 11.0, 13.5, 10.8, 8.9, 12.0, 11.8, 10.2]

temp_max = max(temperaturas)
temp_min = min(temperaturas)

vol_max = volumenes[temperaturas.index(temp_max)]
vol_min = volumenes[temperaturas.index(temp_min)]

temperaturas_ordenadas = sorted(temperaturas, reverse=True)

print(f"Temperatura máxima registrada: {temp_max}°C")
print(f"Temperatura mínima registrada: {temp_min}°C")
print(f"Volumen correspondiente a la temperatura máxima: {vol_max} unidades")
print(f"Volumen correspondiente a la temperatura mínima: {vol_min} unidades")
print("Temperaturas ordenadas de mayor a menor:")
print(temperaturas_ordenadas)