from odoo import models,fields
from datetime import timedelta

class Book(models.Model):
    _name = 'books'
    
    title = fields.Char()
    description = fields.Char()
    genre = fields.Char()
    pages = fields.Integer()
    quantity = fields.Integer()
    author_name = fields.Char()
    
    def _book_available(self):
        for book in self:
            borrowed_count = self.env['borrowed_books'].search_count([
                ('book_id', '=', book.id),
                ('is_returned', '=', False),
                ('borrow_date', '>=', fields.Date.today()),
                ('return_date', '<=', fields.Date.today() + timedelta(days=15))
            ])
            
            return max(0, book.quantity + 1 - borrowed_count) != 0