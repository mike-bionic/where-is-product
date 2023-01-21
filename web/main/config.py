import sys
import json
from os import environ, path
from dotenv import load_dotenv

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath('.')
load_dotenv(path.join(basedir, '.env'))

class Config:
	SECRET_KEY = environ.get('SECRET_KEY') or "123123123"
	APP_PORT = int(environ.get('APP_PORT')) if environ.get('APP_PORT') else 5300
	APP_HOST = environ.get('APP_HOST') or "0.0.0.0"

	DEVICE_SECRET =  environ.get('DEVICE_SECRET') or "finger_device_secret"

	SQLALCHEMY_DATABASE_NAME = environ.get("SQLALCHEMY_DATABASE_NAME") or "bgn.db"
	SQLALCHEMY_DATABASE_URI = f'sqlite:///{path.join(basedir, SQLALCHEMY_DATABASE_NAME)}'
	print(SQLALCHEMY_DATABASE_URI)

	ADMIN_USERNAME = environ.get('ADMIN_USERNAME') or "admin"
	ADMIN_PIN = environ.get('ADMIN_PIN') or "123"

	OS_TYPE = sys.platform
	APP_BASEDIR = path.abspath('.')
	STATIC_FOLDER_PATH = path.join(*json.loads(environ.get('STATIC_FOLDER_PATH'))) if environ.get('STATIC_FOLDER_PATH') else path.join('main','static')
	STATIC_FOLDER_LOCATION = path.join(APP_BASEDIR, STATIC_FOLDER_PATH)
	STATIC_URL_PATH = environ.get('STATIC_URL_PATH') if environ.get('STATIC_URL_PATH') else '/app/static'
	TEMPLATE_FOLDER_PATH = path.join(*json.loads(environ.get('TEMPLATE_FOLDER_PATH'))) if environ.get('TEMPLATE_FOLDER_PATH') else path.join('main','templates')
	TEMPLATE_FOLDER_LOCATION = path.join(APP_BASEDIR, TEMPLATE_FOLDER_PATH)
