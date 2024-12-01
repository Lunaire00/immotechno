# -*- coding: utf-8 -*-
{
    'name': "Immotechno Helpdesk",
    'summary': "Centralizes support requests and ticket management",
    'description': """
    This module, Immotechno Helpdesk, is designed to streamline and centralize the management of support 
    requests and tickets within an organization. It integrates with the maintenance and property management 
    modules to provide a comprehensive solution for handling customer issues, maintenance tasks, and property-related inquiries. 
    The module includes features for creating, tracking, and resolving helpdesk tickets, 
    as well as generating reports and managing access permissions. It is an essential tool for improving customer 
    service efficiency and ensuring timely resolution of support requests.
    """,
    'author': "Arnaud Delhaye, Evrard Sibomana, Joey Remy, Sebastien Lalune, Timothy Huchon",
    'website': "https://technocite.be/",
    'category': 'Maintenance',
    'version': '17.0.3.0',
    'depends': ['maintenance', 'helpdesk','immotechno_property'],
    'data': [
        'data/immotechno_maintenance_data.xml',
        'security/maintenance.xml',
        'security/ir.model.access.csv',
        'views/immotechno_helpdesk_menus.xml',
        'views/maintenance_views.xml',
        'views/helpdesk_ticket_views.xml',
        'report/maintenance_report.xml',
        'views/immotechno_property_views.xml',
        'views/immotechno_building_views.xml',
        'wizard/helpdesk_ticket_to_maintenance_views.xml',
],
    'demo': [
        ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
