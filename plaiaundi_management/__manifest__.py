# -*- coding: utf-8 -*-
{
    'name': "Plaiaundi Management",
    'summary': "Sistema de gestión académica y de recursos para el centro Plaiaundi",
    'description': """
        Módulo especializado para la administración de centros educativos, permitiendo la gestión integral de:
        - Expedientes de Alumnos y Calificaciones
        - Plantilla de Profesores
        - Ciclos Formativos y Aulas
        - Inventario de Equipamiento Informático y Mantenimiento
    """,
    'author': "Erika Martin",
    'website': "https://www.plaiaundi.com",
    'category': 'Education',
    'version': '17.0.1.0.0',
    'depends': ['base'],

    # LA CLAVE ESTÁ AQUÍ: EL ORDEN IMPORTA
    'data': [
        'views/cycle_views.xml',
        'security/ir.model.access.csv',
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