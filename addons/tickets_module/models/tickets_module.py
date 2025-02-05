from odoo import models, fields, api

class TicketsModule(models.Model):
    _name = 'tickets_module.tickets_module'
    _description = 'tickets_module.tickets_module'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date_open = fields.Datetime(string='Date Opened')
    date_closed = fields.Datetime(string='Date Closed')
    status = fields.Selection([
        ('open', 'Open'),
        ('closed', 'Closed')
    ], string='Status', default='open')
    assigned_user_id = fields.Many2one('res.users', string='Assigned User')