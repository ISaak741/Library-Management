from odoo import models, fields
from datetime import timedelta

class Student(models.Model): 
    _name = 'students'
    
    name = fields.Char()
    email = fields.Char()
    sex = fields.Selection([
        ('M','Male'),
        ('F','Female')
    ])
    study_level = fields.Selection([
        ('L','Licence'),
        ('M','Master'),
        ('D','Doctorat')
    ])
    allowed_books = fields.Integer(string='Allowed Books', compute='_set_allowed', store=False)
    
    def _set_allowed(self):
        for student in self:
            match student.study_level:
                case 'L':
                    student.allowed_books = 2
                case 'M':
                    student.allowed_books = 4
                case 'D':
                    student.allowed_books = 6
    
    def _allowed_to_borrow(self):
        for student in self:
            borrowed_count = self.env['borrowed_books'].search_count([
                ('student_id', '=', student.id),
                ('is_returned', '=', False),
                ('borrow_date', '>=', fields.Date.today()),
                ('return_date', '<=', fields.Date.today() + timedelta(days=15))
            ])
            
            return max(0, student.allowed_books + 1 - borrowed_count) != 0
    