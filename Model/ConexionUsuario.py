from typing import Any
import mariadb as sql


class ConexionUsuario():
    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        self.__password = ""
        self.__database = "banco"
        self.__port = 3306
    
    def crearConexion(self):
        self.__conexion = sql.connect(
            host = self.__host,
            user = self.__user,
            password = self.__password,
            database = self.__database,
            port = self.__port)
    def cerrarConexion(self):
        self.__conexion.close()
    
    def getHost(self):
        return self.__host
    
    def getUser(self):
        return self.__user
    
    def getPassword(self):
        return self.__password
    
    def getDataBase(self):
        return self.__database
    
    def getPort(self):
        return self.__port
    
    def getConexion(self):
        return self.__conexion
    

    def setHost(self, host):
        self.__host = host

    def setUser(self, user):
        self.__user = user
    
    def setPassword(self, password):
        self.__password = password

    def setDataBase(self, database):
        self.__database = database

    def setPort(self, port):
        self.__port = port
    
    def setConexion(self, conexion):
        self.__conexion = conexion

