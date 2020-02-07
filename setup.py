from setuptools import setup


setup(
    name='web2db',
    version='0.1',
    description='Fetch webpage full-text, persist link and full text to SQLITE3 db, resumable with tqdm progressbar.',
    url='https://github.com/pushkarparanjpe/web2db',
	author='Pushkar Paranjpe',
	author_email='pushkarparanjpe@gmail.com',
	license='MIT',
	packages=['web2db'],
	zip_safe=False
)
