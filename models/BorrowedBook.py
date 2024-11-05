from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class BorrowedBook(models.Model):
    _name = 'borrowed_books'

    student_id = fields.Many2one('students', string='Student', required=True)
    book_id = fields.Many2one('books', string='Book', required=True)
    borrow_date = fields.Date(string='Borrow Date', default=fields.Date.today())
    return_date = fields.Date(string='Expected Return Date', compute='_compute_return_date', store=True)
    actual_return_date = fields.Date(string='Actual Return Date')
    is_returned = fields.Boolean(string='Returned', default=False)
    days_late = fields.Integer(string='Days Late', compute='_compute_days_late', store=True)
    late_indicator = fields.Char(string='Late', compute='_compute_late_indicator', store=True)

    @api.depends('borrow_date')
    def _compute_return_date(self):
        for record in self:
            record.return_date = record.borrow_date + timedelta(days=15)

    @api.depends('actual_return_date', 'return_date')
    def _compute_days_late(self):
        for record in self:
            if record.actual_return_date and record.actual_return_date > record.return_date:
                record.days_late = (record.actual_return_date - record.return_date).days
            else:
                record.days_late = 0
    
    @api.depends('is_returned', 'days_late')
    def _compute_late_indicator(self):
        for record in self:
            if not record.is_returned:
                record.late_indicator = ''
            else:
                record.late_indicator = f'{record.days_late} days late'
    
    @api.constrains('book_id')
    def _check_book_availability(self):
        for record in self:
            if not record.book_id._book_available():
                raise ValidationError(f"Book `{record.book_id.title}` is not available for borrowing.")
    
    @api.constrains('student_id')
    def _can_student_borrow_book(self):
        for record in self:
            if not record.student_id._allowed_to_borrow():
                raise ValidationError(f"Sorry you have reached the maximum books you can borrow.")
    
    def mark_as_returned(self):
        for record in self:
            record.is_returned = True
            record.actual_return_date = fields.Date.today()