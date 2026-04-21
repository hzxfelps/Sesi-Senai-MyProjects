from storage import grupos

def update_group(data):
    grupo = data["grupo"]
    nivel = data["nivel"]

    grupos[grupo] = nivel
    print(f"[SERVER] Grupo {grupo} -> nível {nivel}")

def get_next_group():
    if not grupos:
        return None, None

    g = min(grupos, key=grupos.get)
    return g, grupos[g]