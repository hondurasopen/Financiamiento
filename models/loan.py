# -*- encoding: utf-8 -*-
from dateutil.relativedelta import relativedelta
from datetime import datetime
from openerp import models, fields, api


class Loan(models.Model):
    _name = "comerical.loan.management"

    name = fields.Char("Numero de registro", required=True)
    partner_id = fields.Many2one("res.partner", "Cliente", required=True)
    request_date = fields.Date("Fecha de solicitud", required=True)
    approval_date = fields.Date("Fecha de aprobación")
    product_value = fields.Float("Precio de contado", required=True)
    interest_rate = fields.Float("Tasa de interes % (anual)", required=True)
    payment_term = fields.Integer("Terminos de pago", required=True)
    product_id = fields.Many2one("product.product", "Articulo", required=True)
    monthly_payment = fields.Float("Cuota de pago")
    notes = fields.Text("Notes")
    state = fields.Selection([('quotation', 'Cotizacion'), ('progress', 'Esperando aprobación'), ('rejected', 'Rechazado'), ('approved', 'Aprobado'), ('done', 'Terminado')], string='State', readonly=True, default='quotation')
    # cuota_ids = fields.One2many("comercial.loan.management.fees", "contrato_id", "Cuotas de pago")
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

    # @api.one
    # def get_calculadora_emi(self):
        # obj_loan_fees = self.env["comercial.loan.management.fees"]
        # obj_loan_cuota_unlink = obj_loan_fees.search([('contrato_id', '=', self.id)])
        # if self.cuota_ids:
            # for delete in obj_loan_cuota_unlink:
                # delete.unlink()
            # self.total_interes = self.monto_solicitado * ( self.tasa_interes /100.0)
            # self.total_monto = self.monto_solicitado + self.total_interes
