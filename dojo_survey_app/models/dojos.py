from werkzeug.utils import redirect
from dojo_survey_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @classmethod
    def get_info_by_id(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @classmethod
    def get_id_by_name(cls, data):
        query = "SELECT id FROM dojos WHERE name = %(name)s;"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @staticmethod
    def validate_survey(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if len(dojo['location']) < 3:
            flash("Location must be at least 3 characters")
            is_valid = False
        if len(dojo['language']) < 2:
            flash("Language must be at least 2 characters")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("Comment is required and must be at least 2 characters")
            is_valid = False
        return is_valid