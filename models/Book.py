from odoo import models,fields

class Book(models.Model):
    _name = 'books'
    
    title = fields.Char()
    description = fields.Char()
    genre = fields.Char()
    pages = fields.Integer()
    quantity = fields.Integer()
    author_name = fields.Char()