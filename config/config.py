#namespace = 'KLIMETO'
namespace = 'AZO'
localhost = False
development = True
if namespace == 'KLIMETO':
    authapi = 'http://pproo.azo.hr/bifisic/services/httpbasicauth/auth'
    if localhost:
        host = 'localhost'
        appport = '5000'
        apiport = '5001'
        dbhost = "193.37.152.219"
        dbport = "5432"
        dbname = "cidedb"
        dbuser = "cideuser"
        dbpwd = "cidepwd"
        tempDataDir = '/scratch/cide-app/temp'
        logsDir = '/scratch/cide-app/logs'
        debug = True
if namespace == 'AZO':
    if localhost:
        host = 'localhost'
        appport = '5000'
        apiport = '5001'
        dbhost = "192.168.1.226"
        dbport = "5432"
        dbname = "BIFISIC"
        dbuser = "bifisic"
        dbpwd = "mypass"
        tempDataDir = '/scratch/cide-app/temp'
        logsDir = '/scratch/cide-app/logs'
        debug = True
        authapi = 'http://192.168.1.226/bifisic/services/httpbasicauth/auth'
    elif development:
        host = '192.168.1.66'
        appport = '80'
        apiport = '8080'
        dbhost = "192.168.1.226"
        dbport = "5432"
        dbname = "BIFISIC"
        dbuser = "bifisic"
        dbpwd = "mypass"
        tempDataDir = '/scratch/cide-app/temp'
        logsDir = '/scratch/cide-app/logs'
        debug = True
        authapi = 'http://192.168.1.226/bifisic/services/httpbasicauth/auth'
    else:
        host = 'http://pproo.azo.hr/cide'
        port = '80'
        dbhost = "localhost"
        dbport = "5432"
        dbname = "BIFISIC"
        dbuser = "bifisic"
        dbpwd = "mypass"
        tempDataDir = '/scratch/cide/temp'
        logsDir = '/scratch/cide/logs'
        debug = False
        authapi = 'http://pproo.azo.hr/bifisic/services/httpbasicauth/auth'