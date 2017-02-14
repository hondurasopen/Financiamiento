# -*- encoding: utf-8 -*-
from odoo import models, fields, api


class Cliente(models.Model):
    _inherit = "res.partner"

    numero_identidad = fields.Char("Identidad", translate=True)
    codigo = fields.Char("Codigo", translate=True)
    sexo = fields.Selection([('masculino', 'Masculino'), ('femenino', 'Femenino')], string='Sexo')
    casa = fields.Selection([('propia', 'Propia'), ('pagando', 'Pagando'), ('alquila', 'Alquila')], string='Casa', default='propia')
    empresa_labora = fields.Char("Lugar de trabajo")
    dir_trabajo = fields.Text("Dirección de trabajo")
    tel_trabajo = fields.Char("Telefono de trabajo")
    nombre_conyuge = fields.Char("Nombre de conyuge")
    id_conyuge = fields.Char("Identidad de conyuge")
    dir_trabajo_conyuge = fields.Text("Dirección de trabajo")
    empresa_labora_conyuge = fields.Char("Lugar de trabajo")
    tel_trabajo_conyuge = fields.Char("Telefono de trabajo")
