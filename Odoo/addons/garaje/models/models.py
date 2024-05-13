# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class garaje(models.Model):
#     _name = 'garaje.garaje'
#     _description = 'garaje.garaje'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100




from odoo import models, fields, api

class aparcamiento_edwin(models.Model):
     _name = 'garaje.aparcamiento.edwin'
     _description = 'Permite definir caracteristicas de un aparcamiento'

     name = fields.Char(string='Direccion', required=True)
     plazas = fields.Integer(string='Plazas', required=True)

     #relaciones entre tablas
     coche_ids =fields.One2many('garaje.coche.edwin', 'aparcamiento_id', string ='Coches')

class coche_edwin(models.Model):
     _name = 'garaje.coche.edwin'
     _description = 'Permite definir caracteristicas de un coche'
     _order = 'name'

     name = fields.Char(string='Matricula', required=True, size=7)
     modelo = fields.Char(string='Modelo', required=True)
     construido = fields.Date(string='Fecha de construccion')
     consumo = fields.Float('Consumo',(4,1),default=0.0)
     averiado = fields.Boolean(string='Averiado', defaul=False)
     annos = fields.Integer('Años', compute='_get_annos')
     descripcion = fields.Text('Descripcion')

     #relaciones entre tablas
     aparcamiento_id = fields.Many2one('garaje.aparcamiento.edwin', string='Aparcamiento')
     mantenimientos_ids = fields.Many2many('garaje.mantenimiento.edwin', string='Mantenimientos')

     @api.depends('construido')
     def _get_annos(self):
          #TODO: lo dejamos para mas adelante 
          for coche in self:
               coche.annos = 0

class mantenimiento_edwin(models.Model):
     _name = 'garaje.mantenimiento.edwin'
     _description = 'Permite definir mantenimientos sobre conjuntos de coches'
     _order ='fecha'

     #name = fields.Char(string='Direccion', required=True)
     fecha = fields.Date('Fecha', required =True, default = fields.date.today())
     tipo = fields.Selection(string='Tipo', selection=[('l','Lavar'),('r','Revision'),('m','Mecanica'),('p','Pintura')], default='l')
     coste = fields.Float('Coste',(8,2), help = 'Coste total del mantenimiento')

     #relaciones entre tablas
     coche_ids = fields.Many2many('garaje.coche.edwin', string ='Coches')