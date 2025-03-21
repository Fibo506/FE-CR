{
    'name': 'Instalador de FE CR',
    'version': '17.0.0.0.0',
    'author': 'Singulary',
    'license': 'AGPL-3',
    'website': 'https://singulary.online',
    'category': 'Accounting/Accounting',
    'description':
        '''
        Facturación electronica Costa Rica.
        ''',
    'depends': [
        'cr_electronic_invoice',
        'cabys',
        'cr_import_vendor_bills'
        ],
    'external_dependencies': {
        "python": [
            'cryptography',
            'xmlsig',
            'OpenSSL',
            'phonenumbers',
            'jsonschema',
        ],
    },
    'installable': True,
    'application': True
}
