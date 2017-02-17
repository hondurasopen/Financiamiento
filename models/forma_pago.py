# -*- encoding: utf-8 -*-
from odoo import models, fields, api


class Formapago(models.Model):
    _name = "comercial.loan.forma.pago"

    name = fields.Selection([('3 pagos', '3 pagos'), ('5 pagos', '5 pagos'), ('7 pagos', '7 pagos'), ('10 pagos', '10 pagos'), ('12 pagos', '12 pagos'), ('16 pagos', '16 pagos'), ('18 pagos', '18 pagos')], string='Terminos de pago', required=True)
    tasa_rate = fields.Float("Tasa %", required=True)
    notas = fields.Text("Notas Generales")
    numero_pagos = fields.Integer("Número de pagos", required=True)

    @api.onchange("name")
    def onhangenumeropago(self):
        if self.name == '3 pagos':
            self.numero_pagos = 3

        if self.name == '5 pagos':
            self.numero_pagos = 5

        if self.name == '7 pagos':
            self.numero_pagos = 7

        if self.name == '10 pagos':
            self.numero_pagos = 10

        if self.name == '12 pagos':
            self.numero_pagos = 12

        if self.name == '16 pagos':
            self.numero_pagos = 16

        if self.name == '18 pagos':
            self.numero_pagos = 18
