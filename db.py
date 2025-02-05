# SQL Alchemy se usa en todo el proyecto y lo correcto para no tener que crear instancias varias veces dentro de cada carpeta, es necesario tenerlo en un solo archivo para que este pueda ser llamado desde cuaquier paete de mi aplicativo

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()