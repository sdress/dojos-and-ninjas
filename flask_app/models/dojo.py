from flask_app.config.mysqlconnection import connectToMySQL

db = 'dojos_and_ninjas_schema'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # create
    @classmethod
    def make_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES ( %(name)s, NOW(), NOW() );"
        return connectToMySQL(db).query_db(query, data)

    # read
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)
        all_dojos = []
        for dojo in results:
            all_dojos.append( cls(dojo) )
        return all_dojos
    
    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    # update
    @classmethod
    def update_dojo(cls, data):
        query = "UPDATE dojos SET name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    # delete
    def delete_dojo(cls, data):
        query = "DELETE * FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)