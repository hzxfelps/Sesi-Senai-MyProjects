from priority_queue import get_next_group
from robot_client import send_to_robot

grupos = {}

def process_data(data):
    grupo = data["grupo"]
    nivel = data["nivel"]

    grupos[grupo] = nivel

    print(f"Grupo {grupo} -> nível {nivel}")

    proximo = get_next_group(grupos)

    if proximo is not None:
        send_to_robot(proximo)