# -*- coding: utf-8 -*-
{
    'name': "Gestión de Plaiaundi",
    'summary': "Sistema de gestión académica y de recursos para el instituto irunés Plaiaundi",
    'author': "Alumnos 2DAM3",
    'website': "https://www.plaiaundi.com",
    'version': '18.0.1.0.0',
    'depends': ['base'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/cycle_views.xml',
        'views/student_views.xml',
        'views/teacher_views.xml',
        'views/classroom_views.xml',
        'views/equipment_views.xml',
        'views/grades_views.xml',
        'views/menu_views.xml',
        'views/attendance_views.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}