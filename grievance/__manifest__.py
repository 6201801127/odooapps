{
    'name': "Grievance Management",

    'summary': """
        This is grievance management module """,

    'description': """
        Grievance management module is developed for any
        kinds of complain we can raise agaist other employee in an organigation
    """,

    'author': "ASK-Technologies",
    'website': "https://ASK-Technologies.odoo.com",
    'category': 'Web Application',
    'version': '0.1',
    'depends': ['base', 'hr'],
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'wizard/forward_wiz.xml',
        'views/grievance.xml',
        'views/category.xml',
        'views/dashboard.xml',
        'views/stage.xml',
        'views/sub_category.xml',
        'views/grievance_menu.xml',
    ],
    'demo': [],
    'qweb': [],
    'auto_install': False,
    'application': True,
    'installable': True,
    'sequence': 1,

}