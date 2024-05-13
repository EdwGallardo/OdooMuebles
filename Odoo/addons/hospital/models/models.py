# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import * #importacion para realizar la funcion que calcula la edad 
from datetime import date            #importacion para realizar la funcion que calcula la edad 



class paciente(models.Model):
    _name = 'hospital.paciente'
    # _description = 'hospital.hospital'

    name = fields.Char('Nom paciente', required = True)
    cognom = fields.Char(string="Cognom", required=True)
    aniversari = fields.Date('Data naixement')
    dni = fields.Char('DNI/NIE', required=True)
    age = fields.Integer('Edat', compute='_age_compute')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    medico_id = fields.Many2many('hospital.medico', string='Médico')
    ingresados_ids = fields.One2many('hospital.ingreso', 'paciente_id', string='Ingresos')


    # _sql_constraints = [('dni_uniq', 'unique (dni)', "Pacient DNI ja existeix!")]
    
    def _age_compute(self): #funcion que me devuele la edad en base a el aniversario del estudiante
          for record in self:
               today = date.today()
               record.age = relativedelta(today, record.aniversari).years
    



class ingreso(models.Model):
    _name = 'hospital.ingreso'

    fecha_ingreso = fields.Date(string='Fecha de Ingreso', required = True)
    fecha_alta = fields.Date(string='Fecha de Alta')
    habitacion = fields.Char(string='Habitación')
    causa = fields.Selection([('accidente','Accidente'), ('analisis', 'Analisis'),('urgencia', 'Urgencia'),('parto','Parto'), ('traslado','Traslado')], default = 'accidente')
    paciente_id = fields.Many2one('hospital.paciente', string='Paciente', ondelete='cascade')
    hospital_id = fields.Many2one('hospital', string='Hospital')


class medico(models.Model):
    _name = 'hospital.medico'

    name = fields.Char(string='Nombre', required = True)
    apellido = fields.Char(string='Apellido')
    dni = fields.Char('DNI/NIE', required=True)
    especialidad = fields.Char(string='Especialidad')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    hospital_id = fields.Many2one('hospital', string='Hospital')
    pacientes_ids = fields.Many2many('hospital.paciente', 'medico_id', string='Pacientes')
    


class hospital(models.Model):
    _name = 'hospital'

    name = fields.Char(string='Nombre', required = True)
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    medicos_ids = fields.One2many('hospital.medico', 'hospital_id', string='Médicos')

