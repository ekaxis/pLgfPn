import json
import urllib2
import sys


def error(msg):
	print(msg); sys.exit(1)


class Zabbix:

	def __init__(self):
		self.url = 'http://zabbix.ncl.intranet/api_jsonrpc.php'
		self.api_user = ''
		self.api_password = ''
		self.token = self.login(self.api_user, self.api_password)
		if self.token is None:
			error('unable to authenticate user')

	def login(self, user, password):
		data = {
			'jsonrpc': '2.0', 
			'method': 'user.login',
			'params': {
				'user': self.api_user,
				'password': self.api_password
			},
			'id': 1, 'auth': None }
		req = urllib2.Request(self.url)
		req.add_header('Content-Type', 'application/json')
		try:
			response = urllib2.urlopen(req, json.dumps(data))
			return json.loads(response.read())['result']
		except Exception as e:
			print 'error: '+str(e)
			return None

	def save(self, hostname, ip):
		data = {
			'jsonrpc': '2.0',
			'method': 'host.create',
			'params': {
				'host': hostname,
				'interfaces':
					[{'type': 1, 'main': 1, 'useip': 1, 'ip': ip, 'dns': '', 'port': '10050'}],
				'groups': [{'groupid': '52'}],
				'templates': [{'templateid': '10001'}]
			},
			'auth': self.token, 'id': 1 }
		req = urllib2.Request(self.url)
		req.add_header('Content-Type', 'application/json')
		try:
			response = urllib2.urlopen(req, json.dumps(data))
			return json.loads(response.read())
		except Exception as e:
			print 'error: '+str(e)
			return None


if __name__ == '__main__':
	if len(sys.argv) >= 3:
		zb = Zabbix()
		print zb.save(sys.argv[1], sys.argv[2])
	else:
		print 'usage: ' + sys.argv[0] + ' hostname ip_address'

