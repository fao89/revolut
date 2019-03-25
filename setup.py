from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements:
    requirements = requirements.readlines()


setup(
    name='revolut',
    version='0.2.0',
    description="Revolut challenge",
    long_description=readme,
    author="Fabricio Aguiar",
    author_email='fabricio.aguiar@gmail.com',
    url='https://github.com/fabricio-aguiar',
    packages=[
        'revolut',
    ],
    package_dir={'revolut':
                 'revolut'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='revolut',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7.2',
    ],
    test_suite='tests',
    tests_require=requirements
)