import math

def crea_punto(x: float, y: float) -> dict:
    return {"x": x, "y": y}


def distanza_tra_punti(p1: dict, p2: dict) -> float:
    return math.sqrt((p2["x"] - p1["x"])**2 + (p2["y"] - p1["y"])**2)


def info_punto(punto: dict) -> str:
    return f"({punto['x']}, {punto['y']})"