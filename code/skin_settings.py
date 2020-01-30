DEFAULT_EMAIL = "webmaster@postgresql.us"
SERVER_EMAIL="webmaster@postgresql.us"

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'US/Central'

INVOICE_SENDER_EMAIL="treasurer@postgresql.us"
MEMBERSHIP_SENDER_EMAIL="contact@postgresql.us"

# Organization name
ORG_NAME="PostgreSQL US"
ORG_SHORTNAME="PgUS"

# Treasurer email address
TREASURER_EMAIL="treasurer@postgresql.us"

ENABLE_PG_COMMUNITY_AUTH = True

# Currency parameter
CURRENCY_ABBREV='USD'
CURRENCY_SYMBOL='$'
CURRENCY_ISO='USD'

# Module to build PDF invoices
INVOICE_PDF_BUILDER='pgusinvoices.PGUSInvoice'
REFUND_PDF_BUILDER='pgusinvoices.PGUSRefund'

# Base URLs for generating absolute URLs
SITEBASE="https://postgresql.us"

# Account numbers used for auto-accounting
ENABLE_AUTO_ACCOUNTING=True
ENABLE_MEMBERSHIP=True
ENABLE_ELECTIONS=True

