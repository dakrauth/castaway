from setuptools import setup

django_extras = ['dj-email-url==1.0.2', 'dj-database-url==0.5.0']
test_extras = ['pytest-cov']

setup(
    name='castaway',
    version='0.1.0',
    description='Simple wrapper for dotenv, with casting',
    url='http://github.com/dakrauth/castaway',
    author='David Krauth',
    author_email='dakrauth@gmail.com',
    license='MIT',
    zip_safe=False,
    py_modules=['castaway'],
    install_requires=['python-dotenv[cli]==0.16.0'],
    extras_require={
        'django': django_extras,
        'test': test_extras,
        'all': django_extras + test_extras
    }
)
