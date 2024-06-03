from dotenv import load_dotenv
import os


load_dotenv()


SECRET_KEY=os.environ.get('SECRET_KEY')

DEBUG=os.environ.get('DEBUG')

SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
