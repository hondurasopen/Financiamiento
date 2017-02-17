# -*- encoding: utf-8 -*-
##############################################################################

{
    "name": "Modulo de financiamiento",
    "version": "1.0",
    "depends": [
        "account",
         "sale",
	"base",
    ],
    "author": "Cesar Alejandro Rodriguez",
    "category": "Sale",
    "description": """
    Este modulo se desarrollo en español para colaborar con la comunidad de Honduras""",
    'data': [
		"views/menu_principal_view.xml",
        "views/cliente_view.xml",
		"views/loan_view.xml",
		"views/loan_cuota_view.xml",
		"views/contracto_sale_sequence.xml",
		"views/comercial_settings_view.xml",
    ],
    #'update_xml' : [
     #       'security/groups.xml',
      #      'security/ir.model.access.csv'
    #],
    'demo': [],
    'installable': True,
}
