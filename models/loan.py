# -*- encoding: utf-8 -*-
from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo import models, fields, api


class Loan(models.Model):
    _name = "comercial.loan.management"

    name = fields.Char("Numero de registro", required=True, default=lambda self: self.env['ir.sequence'].get('contrato'))
    partner_id = fields.Many2one("res.partner", "Cliente", required=True)
    request_date = fields.Date("Fecha de solicitud", required=True)
    approval_date = fields.Date("Fecha de aprobación")
    currency_id = fields.Many2one("res.currency", "Moneda", related='product_id.currency_id')
    payment_term = fields.Many2one("comercial.loan.forma.pago", "Plazo de pago", required=True)
    product_id = fields.Many2one("product.product", "Articulo", required=True)
    # Precios de contrato
    monthly_payment = fields.Monetary("Cuota de pago", required=True)
    prima_pago = fields.Monetary("Prima de crédito", required=True)
    price_financiado = fields.Monetary("Precio financiado")
    product_value = fields.Monetary("Precio de contado", required=True)
    credito_con_prima = fields.Boolean("Crédito con prima", default=True)
    state = fields.Selection([('quotation', 'Cotizacion'), ('progress', 'Esperando aprobación'), ('rejected', 'Rechazado'), ('approved', 'Aprobado'), ('done', 'Terminado')], string='State', readonly=True, default='quotation')
    cuota_ids = fields.One2many("comercial.loan.management.fees", "contrato_id", "Cuotas de pago")
    # Campos seran utilizados en el contrato no aqui
    referencias1 = fields.Char("Referencia 1")
    tel_referencia_amistad1 = fields.Char("Tel. referencia")
    referencias2 = fields.Char("Referencia 2")
    tel_referencia_amistad2 = fields.Char("Tel. referencia")
    # Campos seran utilizados en contrato aval
    nombre_aval = fields.Char("Nombre de aval")
    identidad_aval = fields.Char("Identidad aval")
    sexo = fields.Selection([('masculino', 'Masculino'), ('femenino', 'Femenino')], string='Sexo')
    dir_domicilio = fields.Char("Dirección de domicilio")
    lugar_trabajo_aval = fields.Char("Lugar de trabajo")
    dir_trabajo_aval = fields.Text("Dirección de trabajo")
    notas = fields.Text("Observaciones")
    casa = fields.Selection([('propia', 'Propia'), ('pagando', 'Pagando'), ('alquila', 'Alquila')], string='Casa')

    # Facturas
    invoice_ids = fields.One2many("account.invoice", "contrato_id", "Facturas")

    @api.multi
    def getprice(self):
        if self.product_id and self.payment_term:
            values = {}
            if self.payment_term.name == '3 pagos':
                values['price_financiado'] = self.product_id.lst_price * (1 + (self.payment_term.tasa_rate / 100.0))
                values["prima"] = values['price_financiado'] / 3
                values["cuota"] = (values['price_financiado'] - values["prima"]) / 2
                return values
            if self.payment_term.name == '5 pagos':
                values['price_financiado'] = (self.product_id.lst_price * (1 + (self.payment_term.tasa_rate / 100.0))) * (1 + (self.payment_term.tasa_rate / 100.0))
                values["prima"] = values['price_financiado'] / 5
                return values

    @api.onchange("product_id", "payment_term")
    def onchangecomputeprice(self):
        if self.product_id and self.payment_term:
            values = self.getprice()
            self.product_value = self.product_id.lst_price
            self.price_financiado = values['price_financiado']
            self.prima_pago = values['prima']
            self.monthly_payment = values["cuota"]
        elif self.product_id:
            self.product_value = self.product_id.lst_price



    @api.multi
    def action_rejected(self):
        for cuota in self.cuota_ids:
            cuota.write({'state': 'cancelada'})
            self.write({'state': 'rejected'})

    @api.multi
    def action_quotation(self):
        for cuota in self.cuota_ids:
            cuota.write({'state': 'cotizacion'})
            self.write({'state': 'quotation'})

    @api.multi
    def action_progress(self):
        self.write({'state': 'progess'})

    @api.multi
    def action_approved(self):
        for cuota in self.cuota_ids:
            cuota.write({'state': 'novigente'})
            self.write({'state': 'approved'})
