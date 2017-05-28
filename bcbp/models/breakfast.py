# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Breakfast(models.Model):
	_name = 'bcbp.breakfast'


	name = fields.Many2one(
         'bcbp.members', 'Members Name',  ondelete='cascade', required='True'
    )
	datetime_breakfast = fields.Datetime.now(string='Date and Time Breakfast:')
	type_breakfast = fields.Selection([('joint', 'Joint'), ('men', 'Men'), ('ladies', 'Ladies')], string='Type of Breakfast')



 
# Akhil P Sivan  
# On 2/17/15, 3:28 PM
# Hi Ramanan,

# It is possible in v8. You can use domain attribute in that many2one field, for giving the criteria

# For example:

# class Session(models.Model):
#     _name = 'model.name'
#     employee_id = fields.Many2one('hr.employee', string="Employee", domain=[('field_name','=',value)])