{
  'name': 'The Tickets Module',
  'version': '2.0',
  'author': 'Maximiliano Retana',
  'license': 'LGPL-3',  # Agrega una licencia (LGPL-3 es común para módulos de Odoo)
  'depends': ['base'],
  'data': [
    'views/tickets_module_view.xml',
    'views/security.xml',
  ],
  'installable': True,
  'auto_install': False,
  'application': True,
}