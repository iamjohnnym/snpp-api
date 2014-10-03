from os.path import abspath, dirname, join

_cwd = dirname(abspath(__file__))

class BaseConfiguration(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'This-is-HOW-we-do-IT'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'database/snpp.db')
    SQLALCHEMY_ECHO = False
    HASH_ROUNDS = 100000
    SNPP_HOST = '65.115.133.137'
    SNPP_PORT = 444

class TestConfiguration(BaseConfiguration):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    HASH_ROUNDS = 1
    SNPP_HOST = '65.115.133.137'
    SNPP_PORT = 444

class DebugConfiguration(BaseConfiguration):
    DEBUG = True
