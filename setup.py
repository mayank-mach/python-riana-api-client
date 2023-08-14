import setuptools


setuptools.setup(
    name='riana_api',
    version='0.5.0',
    description='RIANA API Python Client',
    author='DCO-Delivery-Automation',
    author_email='dco-delivery-automation@thomsonreuters.com',
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        riana-api=riana_api.v1.scripts.cli:cli
    ''',
)
