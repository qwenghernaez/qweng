# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Donation(models.Model):
	_name = 'bcbp.donation'


	name = fields.Many2one(
         'bcbp.members', 'Members Name',  ondelete='cascade', required='True'
    )
	datetime_donate = fields.Datetime(string='Date and Time of Donation:')
	type_donation = fields.Selection([('cheque', 'Cheque'), ('cash', 'Cash')], string='Type of Donation')
	donation_amount = fields.Float(string='Donation Amount ')
