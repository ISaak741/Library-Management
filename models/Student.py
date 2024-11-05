from odoo import models, fields

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
    