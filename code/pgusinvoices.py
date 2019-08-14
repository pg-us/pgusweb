import os
from django.conf import settings

from postgresqleu.util.misc.baseinvoice import BaseInvoice,BaseRefund

class PGUSBase(object):
    logo = os.path.join(settings.PROJECT_ROOT, '../media/img/PostgreSQL_logo.1color_blue.300x300.png')
    headertext = """United States PostgreSQL Association
9450 SW Gemini Dr #62635
Beaverton, OR, 97008-7105
"""
    sendertext = """Your contact: Mark Wong
Function: United States PostgreSQL Association Treasurer
E-mail: treasurer@postgresql.us"""

    bankinfotext = """Contact treasurer@postgresql.us
"""

    paymentterms = """
"""


class PGUSInvoice(PGUSBase, BaseInvoice):
    pass


class PGUSRefund(PGUSBase, BaseRefund):
    pass
