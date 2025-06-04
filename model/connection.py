import psycopg as postgres

class Connection: 
    __instance = None 
    __connection = None

    def __new__(cls): 
        if cls.__instance is None: 
            cls.__instance = super().__new__(cls)
            cls.__connection = postgres.connect( 
                host = 'localhost', dbname = 'biblioteca' , user = 'postgres', password  = 'admin'
            )
            
            return cls.__instance
        
    def cursor(self):
        return self.__connection.cursor()
    
    def commit(self):
        self.__connection.commit()
    
    def close(self): 
        return self.__connection.close()