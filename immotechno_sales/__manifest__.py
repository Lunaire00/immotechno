# -*- coding: utf-8 -*-
{
    'name': "Immotechno Sales",
    'summary': "Centralizes sales and transaction management",
    'description': """
    This module, Immotechno Sales, is designed to centralize and streamline the management of sales and transactions within the 
    Immotechno system. It integrates with various sales-related modules to provide a comprehensive solution for handling sales orders, 
    subscriptions, and property-related transactions. Key features include automated quotation generation, 
    scheduled tasks for sales processes, and customizable sales settings. This module aims to enhance efficiency and accuracy in sales 
    operations, making it an essential tool for businesses using the Immotechno platform.
    """,
    'author': "Arnaud Delhaye, Evrard Sibomana, Joey Remy, Sebastien Lalune, Timothy Huchon",
    'website': "https://technocite.be/",
    'category': 'Uncategorized',
    'version': '17.0.3.0',
    'depends': ['sale_management', 'sale_subscription', 'sale','immotechno_property'],
    "data": [
        "security/ir.model.access.csv",
        "data/product_data.xml",
        "data/quotation_template.xml",
        "data/cron.xml",
        "views/immotechno_sales_menu.xml",
        "views/sale_order_views.xml",
        "views/immotechno_property_views.xml",
        "views/immotechno_sale_settings_views.xml",
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
