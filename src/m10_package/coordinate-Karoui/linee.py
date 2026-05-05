from .punti import distanza_tra_punti, crea_punto

def crea_linea(p1: dict, p2: dict) -> dict:
    return {"p1": p1, "p2": p2}


def lunghezza_linea(linea: dict) -> float:
    return distanza_tra_punti(linea["p1"], linea["p2"])


def punto_medio(linea: dict) -> dict:
    x1, y1 = linea["p1"]["x"], linea["p1"]["y"]
    x2, y2 = linea["p2"]["x"], linea["p2"]["y"]
    
    return crea_punto((x1 + x2) / 2, (y1 + y2) / 2)


def info_linea(linea: dict) -> str:
    p1 = linea["p1"]
    p2 = linea["p2"]
    return f"Linea da ({p1['x']}, {p1['y']}) a ({p2['x']}, {p2['y']})"