#Marvel_api

[![Docker pullS](https://img.shields.io/docker/pulls/luisfersh/marvel_api.svg)](https://hub.docker.com/r/luisfersh/marvel_api)

Proyecto Copple de microservicios usando Flask para comunicarse con Marvel api y administrar usuarios usando MongoDB.


##Configuracion 

##pull
Ejecute los comandos del repositorio y muevase a la carpeta del proyecto

```console
git clone 

cd marvel-comics
```

Cree un archivo .env en el la raíz con la siguiente estructura:

```
PUBLIC_KEY="YOUR_PUBLIC_KEY"
PRIVATE_KEY="YOUR_PRIVATE_KEY"
SECRET_KEY= "RANDOM_LONG_STRING"  #Tan larga o corta como quieras
```
La clave pública y privada proviene de esta documentación de API. [API documentation](https://developer.marvel.com/)Cree sus propias claves y guárdelas en el archivo .env

Estructura del archivo en este punto:
```
marvel-comics
└───app
│   └ ...
│   .env
│   app.py
│   docker-compose-dev.yml
│   docker-compose.yml
│   Dockerfile
│   Dockerfile.dev
│   README.md
│   requirements.txt
```

##Entorno de ejecución el

```
docker compose -f docker-compose-dev.yml up
```
# Marvel-comics: End-point documentation

## End-point: Search Characters

### Method: POST

> ```
> http://127.0.0.1:5000/searchComics
> ```
### Body (**raw**)

```json
{
  "type": "character",  Atributo opcional, acepta carácter o cómic como valor.
  "filter": "%Spider-Man%" Obligatorio si está presente el atributo "type".
}
```
### Response

```json
{
  "action": "", Descripción de la acción realizada.
  "result": []  Caracteres relacionados encontrados
}
```

-------------------------------------------------------------------------------------------------------
# End-point: Users Add

### Method: POST

> ```
> http://127.0.0.1:5000/users/add
> ```
### Body (**raw**)

```json
{
  "email": "lfs@email.com",  Campo obligatorio
  "password": "a_fancy_password:123", Campo obligatorio

  "name": "My Name", Cualquier otro campo es personalizado, puede crear sus propios campos
  "age": 25
}
```
### Response

```json
{
  "action": "", //Action performed description.
  "result": [] //New user info without password
}
```
-----------------------------------------------------------------------------------------

## End-point: Users Login

### Method: POST

> ```
> http://127.0.0.1:5000/users/login
> ```

### Body (**raw**)

```json
{
  "email": "lfs@email.com",
  "password": "a_fancy_password:123"
}
```

### Response

```json
{
  "action": "", Descripción de la acción realizada.
  "result": []  Información de usuario y su TOKEN
}
```

--------------------------------------------------------------------------------------------------------

## End-point: addToLayaway

### Method: POST

> ```
> http://127.0.0.1:5000/addToLayaway
> ```

### Headers

| Content-Type | Value                          |
| ------------ | ------------------------------ |
| token        | YOUR_TOKEN_FROM_LOGIN_ENDPOINT |

### Body (**raw**)

```json
{
  "comics_to_add": [59551, 102588, 98309] Marvel comics ids.
}
```

### Response

```json
{
  "action": "", Descripción de la acción realizada.
  "result": []  Información de cómics insertada
}
```
