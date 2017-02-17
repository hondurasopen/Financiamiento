# -*- encoding: utf-8 -*-
from odoo import models, fields, api 


class Loanfees(models.Model):
    _name = "comercial.loan.management.fees"

    contrato_id = fields.Many2one("comercial.loan.management.fees", "Número de contrato")
    partner_id = fields.Many2one("res.partner", "Cliente")
    fecha_pago = fields.Date("Fecha de Pago")
    monto_cuota = fields.Float("Monto de Cuota")
    monto_mora = fields.Float("Monto de mora")
    saldo_prestamo = fields.Float("Saldo Pendiente")
    state = fields.Selection([('cotizacion', 'Cotización'), ('novigente', 'No vigente'), ('vigente', 'Vigente'), ('pagada', 'Pagada'), ('cancelada', 'Cencelada')], string='Estado de cuota', readonly=True, default='cotizacion')
    notas = fields.Text("Notas Generales")

    @api.multi
    def action_cancelar(self):
        self.write({'state': 'cancelada'})

