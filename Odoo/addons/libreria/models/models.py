# -*- coding: utf-8 -*-

# from odoo import models, fields, api

from odoo import models, fields, api

class libreria_gallardo_categoria(models.Model):
    _name = "libreria.gallardo.categoria"

    name =fields.Char(string="Nombre", required=True,help="Introduce el nombre de la categoria")
    descriptio = fields.Text(string="Descripcion", help="Introduce una descripción")
    libros = fields.One2many("libreria.alvarez.libro","categoria", string="Libros")

class libreria_alvarez_libro(models.Model):  
    _name = "libreria.alvarez.libro"  
    name = fields.Char(string="Titulo", required=True, help="Introduce un titulo")
    precio = fields.Float(string="Precio")
    ejemplares = fields.Integer(string="Ejemplares")
    fecha = fields.Date(string="Fecha de compra")
    segunda_mano = fields.Boolean(string = "Segunda mano")
    estado = fields.Selection ([('0', 'Bueno'),('1', 'Regular'),('2', 'Malo')], string="Estado", default="0")

    categoria = fields.Many2one("libreria.gallardo.categoria", string="Categoria", required=True, ondelete="cascade")





# class libreria(models.Model):
#     _name = 'libreria.libreria'
#     _description = 'libreria.libreria'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
