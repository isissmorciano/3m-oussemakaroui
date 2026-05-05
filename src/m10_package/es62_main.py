from coordinate import punti, linee

print("=== Coordinate e Linee ===\n")

# Creazione punti
pA = punti.crea_punto(0.0, 0.0)
pB = punti.crea_punto(3.0, 4.0)
pC = punti.crea_punto(6.0, 0.0)

print("Punti:")
print(f"- Punto A: {punti.info_punto(pA)}")
print(f"- Punto B: {punti.info_punto(pB)}")
print(f"- Punto C: {punti.info_punto(pC)}")

# Creazione linee
l1 = linee.crea_linea(pA, pB)
l2 = linee.crea_linea(pB, pC)

print("\nLinee:")

for linea in [l1, l2]:
    lunghezza = round(linee.lunghezza_linea(linea), 2)
    medio = linee.punto_medio(linea)
    
    print(
        f"- {linee.info_linea(linea)} | "
        f"Lunghezza: {lunghezza:.2f} | "
        f"Punto medio: {punti.info_punto(medio)}"
    )