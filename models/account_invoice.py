# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import Warning


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    contrato_id = fields.Many2one("comercial.loan.management", "Contrato")