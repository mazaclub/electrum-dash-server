from setuptools import setup

setup(
    name="electrum-dash-server",
    version="0.9",
    scripts=['run_electrum_dash_server','electrum-dash-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumserver':'src'
        },
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.server_processor',
        'electrumserver.processor',
        'electrumserver.version',
        'electrumserver.ircthread',
        'electrumserver.stratum_tcp',
        'electrumserver.stratum_http'
    ],
    description="Dashpay Electrum Server",
    author="Thomas Voegtlin, ELM4ever, Propulsion",
    author_email="thomasv1@gmx.de, Propulsion@DarkcoinTalk.org",
    license="GNU Affero GPLv3",
    url="https://github.com/spesmilo/electrum-server/, https://github.com/mazaclub/electrum-dash-server/",
    long_description="""Server for the Electrum Lightweight Dashpay Wallet"""
)


