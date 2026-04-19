def get_next_group(grupos):
    if not grupos:
        return None

    # menor nível = maior prioridade
    return min(grupos, key=grupos.get)