"""
A component to install the mysqlclient to support recorder on MariaDB
"""
import logging

VERSION = '1.0.1'

_LOGGER = logging.getLogger(__name__)

REQUIREMENTS = ['mysqlclient==1.4.2.post1', 'PyMySQL==0.9.3']

DOMAIN = 'custom_dependencies'

async def async_setup(hass, config):
    try:
        import mysqlclient
        import pymysql
        _LOGGER.info("mysqlclient available")
    except ImportError:
        _LOGGER.error("mysqlclient failed to import")
        
    return True