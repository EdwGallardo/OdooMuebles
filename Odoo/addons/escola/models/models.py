# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import * #importacion para realizar la funcion que calcula la edad 
from datetime import date            #importacion para realizar la funcion que calcula la edad 


class escola_student(models.Model):
     _name = 'escola.student'
     _description = 'School student'

     name = fields.Char('Nom', required = True)
     last_name = fields.Char(string="Cognom", required=True)
     birthdate = fields.Date('Aniversari')
     id_number = fields.Char('DNI/NIE', size=64, required=True)
     active = fields.Boolean('Actiu', default=True,
                             help = "Is the student currently part of the class")
     age = fields.Integer('Edat', compute='_age_compute')
     class_id = fields.Many2one('escola.class')
     events_ids = fields.Many2many('escola.event', string="Events")

     _sql_constraints = [('id_number_uniq', 'unique (id_number)', "Student ID already exist !")] #restriccion para que solo exista un unico identificador de estudiante
    
     def _age_compute(self): #funcion que me devuele la edad en base a el aniversario del estudiante
          for record in self:
               today = date.today()
               record.age = relativedelta(today, record.birthdate).years
    

class escola_class(models.Model):
     _name = 'escola.class'
     _description = 'School class'

     name = fields.Char('Denominacio', size=64, required=True)
     grade = fields.Selection([('first','Primer grau'), ('second', 'Segon grau'),('third', 'Tercer grau'),('fourth','Quart grau')], default = 'first') 
     date_begin = fields.Date('Data inici')
     date_end = fields.Date('Data fi')
     tutor_id = fields.Many2one('hr.employee', string='Tutor')
     students_ids = fields.One2many('escola.student', 'class_id', string ='Estudiants')
     student_number = fields.Integer('Nombre estudiants')
     description = fields.Text('Descripcio')


class escola_event(models.Model):
     _name = 'escola.event'
     _order = 'datetime_begin'
 
     type = fields.Selection([('absence','Absencia'), ('delay', 'Retard'),('felicitacio', 'Felicitacio'),('behavior','Comportament')], string='Tipus', default = 'absence')  
     class_id = fields.Many2one('escola.class', 'Classe')
     datetime_begin = fields.Datetime('Data i hora', default = fields.datetime.now()) #esta funcion me devuelve la hora y fecha 
     students_ids = fields.Many2many('escola.student', string ='Estudiants')
     description = fields.Text('Descripcio')
     teacher_id = fields.Many2one('hr.employee', string= 'Professor') #hr.employee es la tabla empleados de odoo
     
     # def name_get(self): #funcion que me permite obtener el nombre del tipo para mostarlo en las formas
     #      result = []
     #      for record in self:
     #           name = '(' + record.class_id.name + ') ' + record.type
     #           result.append((record.id, name))
     #      return result     