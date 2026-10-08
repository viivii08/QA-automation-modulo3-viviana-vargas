import requests

BASE_URL = "https://pokeapi.co/api/v2"


def obtener_berry(id_berry):
    # Hace el GET a berry/{id}, verifica que responda bien y devuelve el JSON
    respuesta = requests.get(f"{BASE_URL}/berry/{id_berry}", timeout=10)
    assert respuesta.status_code == 200, (
        f"GET berry/{id_berry}: se esperaba status 200 y se obtuvo {respuesta.status_code}"
    )
    return respuesta.json()


def test_berry_1_tiene_size_soil_dryness_y_firmness_correctos():
    # Paso 1: hacer un GET a berry/1
    berry = obtener_berry(1)

    # Paso 2: verificar que el size sea 20
    assert berry["size"] == 20, f"Se esperaba size 20 y se obtuvo {berry['size']}"

    # Paso 3: verificar que el soil_dryness sea 15
    assert berry["soil_dryness"] == 15, f"Se esperaba soil_dryness 15 y se obtuvo {berry['soil_dryness']}"

    # Paso 4: verificar que en firmness, el name sea soft
    assert berry["firmness"]["name"] == "soft", (
        f"Se esperaba firmness 'soft' y se obtuvo '{berry['firmness']['name']}'"
    )


def test_berry_2_comparada_con_berry_1():
    # Se obtiene berry/1 para comparar con los datos del punto anterior
    berry_1 = obtener_berry(1)

    # Paso 1: hacer un GET a berry/2
    berry_2 = obtener_berry(2)

    # Paso 2: verificar que en firmness, el name sea super-hard
    assert berry_2["firmness"]["name"] == "super-hard", (
        f"Se esperaba firmness 'super-hard' y se obtuvo '{berry_2['firmness']['name']}'"
    )

    # Paso 3: verificar que el size sea mayor al del punto anterior
    assert berry_2["size"] > berry_1["size"], (
        f"El size de berry/2 ({berry_2['size']}) no es mayor al de berry/1 ({berry_1['size']})"
    )

    # Paso 4: verificar que el soil_dryness sea igual al del punto anterior
    assert berry_2["soil_dryness"] == berry_1["soil_dryness"], (
        f"El soil_dryness de berry/2 ({berry_2['soil_dryness']}) no es igual al de berry/1 ({berry_1['soil_dryness']})"
    )


def test_pikachu_experiencia_base_y_tipo():
    # Paso 1: hacer un GET a pikachu
    respuesta = requests.get(f"{BASE_URL}/pokemon/pikachu/", timeout=10)
    assert respuesta.status_code == 200, f"Se esperaba status 200 y se obtuvo {respuesta.status_code}"
    pikachu = respuesta.json()

    # Paso 2: verificar que su experiencia base es mayor a 10 y menor a 1000
    experiencia = pikachu["base_experience"]
    assert 10 < experiencia < 1000, f"La experiencia base ({experiencia}) no esta entre 10 y 1000"

    # Paso 3: verificar que su tipo es "electric"
    # "types" es una lista, porque un pokemon puede tener mas de un tipo
    tipos = [t["type"]["name"] for t in pikachu["types"]]
    assert "electric" in tipos, f"Se esperaba el tipo 'electric' y se obtuvo {tipos}"
