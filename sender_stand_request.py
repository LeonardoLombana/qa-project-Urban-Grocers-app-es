import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # inserta la dirección url completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())



def get_users_table(body):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # inserta la dirección url completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


response = get_users_table(data.user_body)
print(response.status_code)
print(response.json())


def get_user_body(first_name):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        # inserta la dirección url completa
                        json=first_name,  # inserta el cuerpo de solicitud
                        headers=data.headers)  # inserta los encabezados

    response = get_user_body(data.user_body)
    print(response.status_code)
    print(response.json())

