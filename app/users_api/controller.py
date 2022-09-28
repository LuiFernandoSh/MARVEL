from werkzeug.security import generate_password_hash, check_password_hash
from app.users_api.database import Database
from bson.json_util import dumps
from app.utilities import json
from decouple import config
import datetime
import jwt


def add(request):
    data =request.json

    email = json.get_or_error(data, 'email')
    json.get_or_error(data, 'password')

    db = Database()

    if db.read({"email": email}) != None:
        raise Exception("Correo electrónico ya en uso")

    data['password'] =generate_password_hash(
        data['password'], method='sha256')
    

    return 'Usuario creado', db.write(data)

def login(request):
    data =request.json

    email = json.get_or_error(data, 'email')
    password = json.get_or_error(data, 'password')

    db = Database()

    user_db = db.read({"email": email})

    if None in user_db or not check_password_hash(user_db['password'], password):
        
        return 'No iniciado sesión. La contraseña o el correo electrónico son incorrectos.'
    expires_at =str(datetime.datetime.utcnow() +
                    datetime.timedelta(minutes=60*24*30))
    token = jwt.encode(
        {'id': str(user_db['_id']), 'exp': expires_at}, config('SECRET_KEY'))
    
    user_db.pop('password', None)
    user_db.pop('_id', None)
    user_db['token'] = token

    return 'Iniciado sesión', dumps(user_db)

def find_by_id(id):
    db = Database()
    user_db = db.read({"_id": id})
    
    return user_db
       

