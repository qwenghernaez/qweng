# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Event(models.Model):
	_name = 'bcbp.event'


	name = fields.Many2one(
         'bcbp.members', 'Members Name',  ondelete='cascade', required='True'
    )
	datetime_attend = fields.Datetime.now(string='Date and Time Event:')
	event_type = fields.Char(string='Type of Event')

