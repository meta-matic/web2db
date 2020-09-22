from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='web2db',
    version='0.1.5',
    description='Fetch webpage full-text, persist link and full text to SQLITE3 db, resumable with tqdm progressbar.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/pushkarparanjpe/web2db',
    author='Pushkar Paranjpe',
    author_email='pushkarparanjpe@gmail.com',
    license='MIT',
    packages=['web2db'],
    zip_safe=False
)
