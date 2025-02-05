from flask import Flask
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from  db import db
from flask_migrate import Migrate #Es la ingnorancia de las migraciones

#Crear una instancias
app = Flask(__name__)  

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/db_blogs_flask'
#vamos a ejecutar SQLAlchemy
db.init_app(app)
migrate = Migrate(app, db)

#para crear una tabla usando SQLAlchemy
class CategoriasTable(db.Model):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))  

class PostTable(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(250))
    contenido =Column(Text)
    fecha = Column(DateTime)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))    


#levantar mi servidor
if __name__ == "__main__":
    app.run(debug=True)

























