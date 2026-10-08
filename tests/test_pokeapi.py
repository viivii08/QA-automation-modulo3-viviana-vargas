import requests

BASE_URL = "https://pokeapi.co/api/v2"


def test_berry_1_tiene_size_soil_dryness_y_firmness_correctos():
    # Paso 1: hacer un GET a berry/1
    respuesta = requests.get(f"{BASE_URL}/berry/1", timeout=10)
    assert respuesta.status_code == 200, f"Se esperaba status 200 y se obtuvo {respuesta.status_code}"

    berry = respuesta.json()

    # Paso 2: verificar que el size sea 20
    assert berry["size"] == 20, f"Se esperaba size 20 y se obtuvo {berry['size']}"

    # Paso 3: verificar que el soil_dryness sea 15
    assert berry["soil_dryness"] == 15, f"Se esperaba soil_dryness 15 y se obtuvo {berry['soil_dryness']}"

    # Paso 4: verificar que en firmness, el name sea soft
    assert berry["firmness"]["name"] == "soft", (
        f"Se esperaba firmness 'soft' y se obtuvo '{berry['firmness']['name']}'"
    )
