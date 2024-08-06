import sender_stand_request
import data

#Pruebas a realizar

def get_user_kit(user_kit):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = user_kit
    return current_kit_body


def positive_assert(user_kit):
    user_kit_body = get_user_kit(user_kit)
    sender_stand_request.post_new_user(data.user_body)
    response_new_kit = sender_stand_request.post_new_kit(user_kit_body)

    assert response_new_kit.status_code == 201
    assert response_new_kit.json()["name"] == user_kit_body["name"]


def negative_assert_symbol(user_kit):
    user_kit_body = get_user_kit(user_kit)
    sender_stand_request.post_new_user(data.user_body)
    response_new_kit = sender_stand_request.post_new_kit(user_kit_body)

    assert response_new_kit.status_code == 400


def negative_assert_no_name(kit_body):
    sender_stand_request.post_new_user(data.user_body)
    response_new_kit = sender_stand_request.post_new_kit(kit_body)

    assert response_new_kit == 400


def test_numero_permitido_caracteres_1():
    positive_assert(data.prueba_1)


def test_numero_permitido_caracteres_511():
    positive_assert(data.prueba_2)


def test_numero_menor_caracteres():
    negative_assert_symbol(data.prueba_3)


def test_numero_mayor_caracteres_512():
    negative_assert_symbol(data.prueba_4)


def test_caracteres_especiales():
    positive_assert(data.prueba_5)


def test_se_permiten_espacios():
    positive_assert(data.prueba_6)


def test_se_permiten_numeros():
    positive_assert(data.prueba_7)


def test_parametro_no_se_pasa_en_la_solicitud():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)


def test_se_ha_pasado_un_tipo_de_parametro_diferente():
    negative_assert_symbol(data.prueba_9)
