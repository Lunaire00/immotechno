# -*- coding: utf-8 -*-
{
    'name': "Immotechno Property",
    'version': '17.0.3.0',
    'summary': "Centralizes real estate management",
    'description': """
    This "Real Estate" app is the central place to manage all property-related features. 
    It allows you to view interactions with the Sales app for selling and renting properties, 
    and with Maintenance and Helpdesk for managing related equipment and handling support tickets.
    The app opens by default in Kanban view for an intuitive overview of properties and their statuses.
    """,
    'category': 'Property',
    'author': "Arnaud Delhaye, Evrard Sibomana, Joey Remy, Sebastien Lalune, Timothy Huchon",
    'website': "https://technocite.be/",
    'depends': ['contacts','mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/immotechno_property_type_demo.xml',
        'data/immotechno_building_demo.xml',
        'data/immotechno_partner_type_demo.xml',
        'data/immotechno_room_type_demo.xml',
        'data/immotechno_property_demo.xml',
        'data/immotechno_property_type_business_demo.xml',
        'views/immotechno_menu.xml',
        'views/immotechno_property_views.xml',
        'views/immotechno_building_views.xml',
        'views/res_partner_views.xml',
        'views/immotechno_property_type_views.xml',
        'views/immotechno_partner_type_views.xml',
        'views/immotechno_room_type_views.xml',
        'views/report/property_report.xml',
        'views/immotechno_property_business_type_view.xml',
        'views/immotechno_settings_views.xml',        
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',        
}
