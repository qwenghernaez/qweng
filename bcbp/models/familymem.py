# -*- coding: utf-8 -*-

from odoo import models, fields, api



class FamilyMem(models.Model):
    _name = 'bcbp.family_members'
    _inherits = {'res.partner': 'partner_id', }

    id = fields.Integer('ID', readonly=True)
    partner_id = fields.Many2one(
        'res.partner', 'Related Partner', required=True, ondelete='cascade',
        help='User ID'
    )
    image = fields.Binary()
    birthdate = fields.Date(string="Birhtday")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')

    info = fields.Text(string='Extra info')
    civil_status = fields.Selection([('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced')], string='Married Status')
    #------------------------Family--------------------------#
    relation = fields.Selection([('mother', 'Mother'), ('father', 'Father'), ('sister', 'Sister'), ('brother', 'Brother'), ('daughter', 'Daughter'), ('son', 'Son'), ('wife', 'Wife'), ('husband', 'Husband')], string='Relation')
    @api.model
    def create(self, vals,):
        groups_proxy = self.env['res.groups']
        group_ids = groups_proxy.search([('name', '=', 'FamilyMem')])
        vals['groups_id'] = [(6, 0, group_ids)]
        return super(FamilyMem, self).create(vals)