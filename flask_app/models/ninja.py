from flask_app.config.mysqlconnection import connectToMySQL

db = 'dojos_and_ninjas_schema'

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # create
    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES ( %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s );"
        return connectToMySQL(db).query_db(query, data)

    # read
    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(db).query_db(query)
        all_ninjas = []
        for ninja in results:
            all_ninjas.append( cls(ninja) )
        return all_ninjas
    
    @classmethod
    def get_dojo_ninjas(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL(db).query_db(query, data)
        dojo_ninjas = []
        for ninja in results:
            dojo_ninjas.append( cls(ninja) )
        return dojo_ninjas

    
    @classmethod
    def get_one_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    # update
    @classmethod
    def update_ninja(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW(), dojo_id = %(dojo_id)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    # delete
    def delete_ninja(cls, data):
        query = "DELETE * FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)