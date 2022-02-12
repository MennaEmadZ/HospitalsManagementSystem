{
    'name': 'HMS',
    'summary': 'Hospitals Management System',
    'depends': ['base','crm'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/dept_view.xml',
        'views/log_history_view.xml',
        'views/cust_view.xml',
        "reports/report.xml",
        "reports/template.xml",


    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}