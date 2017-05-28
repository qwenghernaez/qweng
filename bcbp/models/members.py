# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Members(models.Model):
    _name = 'bcbp.members'
    _inherits = {'res.partner': 'partner_id', }

    id = fields.Integer('ID', readonly=True)
    partner_id = fields.Many2one(
        'res.partner', 'Related Partner', required=True, ondelete='cascade',
        help='User ID'
    )
    image = fields.Binary()
    position = fields.Selection([('active_group_member', 'Active Group Member'), ('action_group_leader', 'Action Group Leader'), ('unit_head', 'Unit Head'), ('chapter_head', 'Chapter Head')], default='active_group_member', string='Position')
    birthdate = fields.Date(string="Birhtday")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    family = fields.Many2many('bcbp.family_members', string='Family Information',  ondelete='cascade')
    info = fields.Text(string='Extra info')
    # active = fields.Boolean(
    #     'Active', default=True,
    #     help='If unchecked, it will allow you to hide contact without '
    #          'removing it.'
    # )
    civil_status = fields.Selection([('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced')], string='Married Status')
    #------------------------Family--------------------------#
    
    @api.model
    def create(self, vals,):
        groups_proxy = self.env['res.groups']
        group_ids = groups_proxy.search([('name', '=', 'Members')])
        vals['groups_id'] = [(6, 0, group_ids)]
        return super(Members, self).create(vals)