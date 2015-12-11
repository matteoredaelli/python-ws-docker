from flask import Flask
import dns.resolver
import nmap
import json

def getIP(hostname):
    try:
        answers = dns.resolver.query(hostname)
        ip = answers[0].address
    except:
        ip = "none"
        
    return {'ip': ip}

def scanPorts(hostname, max_port):
    range = "0-%s" % max_port
    nm = nmap.PortScanner()
    try:
        nm.scan(hostname, range)
        result = nm[nm.all_hosts()[0]]['tcp']
    except:
        result = "none"
    return {'tcp': result}
    
app = Flask(__name__)

@app.route('/infra')
def hello():
    return 'Infrastructure tools, release 0.1\n'

@app.route('/infra/hostname/<hostname>/<upper_port>')
def hostname(hostname, upper_port):
    host = {'hostname': hostname}
    ip = getIP(hostname)
    scan = scanPorts(hostname, upper_port)
    result = dict(dict(host, **ip), **scan)
    return json.dumps(result, sort_keys=True, indent=4)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

