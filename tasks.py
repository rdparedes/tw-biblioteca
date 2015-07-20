from invoke import run, task

@task
def clean(docs=False, bytecode=False, extra=''):
	patterns = ['build']
	if docs:
		patterns.append('docs/_build')
	if bytecode:
		patterns.append('**/*.pyc')
	if extra:
		patterns.append(extra)
	for pattern in patterns:
		run('rm -rf %s' % pattern)

@task
def runserver():
	PORT = '5000'
	appName = 'app'
	run('gunicorn -b 0.0.0.0:' + PORT + ' twbiblioteca.wsgi:' + appName)