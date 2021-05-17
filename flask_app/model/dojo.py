from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    
    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos(name, location, language, comment, created_at, updated_at) VALUES(%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        print(query)
        dojo_id = connectToMySQL("dojo_survey_schema").query_db(query,data)
        print(dojo_id)
        return dojo_id

    @classmethod
    def show_input(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL("dojo_survey_schema").query_db(query, data)
    

        return results[0]

    
    @staticmethod
    def validate_data(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash("name must be at least 3 characters")
            is_valid = False
        if len(dojo['location']) < 3:
            flash("location must be at least 3 characters")
            is_valid = False
        if len(dojo['language']) <1:
            flash("please choose a valid language")
            is_valid = False
        return is_valid
        
        

