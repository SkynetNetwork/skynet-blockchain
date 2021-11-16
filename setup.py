from setuptools import setup

dependencies = [
    "blspy==1.0.6",  # Signature library
    "skynetvdf==1.0.3.dev8",  # timelord and vdf verification
    "skynetbip158==1.1.dev3",  # bip158-style wallet filters
    "skynetpos==1.0.4.dev14",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.12",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.4",  # Colorizes terminal output
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "fasteners==0.16.3",  # For interprocess file locking
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the skynet processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    #  "dnspython==2.1.0",  # Query DNS seeds
    "async-dns==2.0.0", # Async query DNS seeds
    "watchdog==2.1.3",  # Filesystem event watching - watches keyring.yaml
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "types-setuptools",
]

kwargs = dict(
    name="skynet-blockchain",
    author="SkynetNetwork",
    author_email="support@skynet-network.org",
    description="Skynet blockchain full node, farmer, timelord, and wallet.",
    url="https://skynet-network.org/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="skynet blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "skynet",
        "skynet.cmds",
        "skynet.clvm",
        "skynet.consensus",
        "skynet.daemon",
        "skynet.full_node",
        "skynet.timelord",
        "skynet.farmer",
        "skynet.harvester",
        "skynet.introducer",
        "skynet.plotting",
        "skynet.pools",
        "skynet.protocols",
        "skynet.rpc",
        "skynet.server",
        "skynet.simulator",
        "skynet.types.blockchain_format",
        "skynet.types",
        "skynet.util",
        "skynet.wallet",
        "skynet.wallet.puzzles",
        "skynet.wallet.rl_wallet",
        "skynet.wallet.cc_wallet",
        "skynet.wallet.did_wallet",
        "skynet.wallet.settings",
        "skynet.wallet.trading",
        "skynet.wallet.util",
        "skynet.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "skynet = skynet.cmds.skynet:main",
            "skynet_wallet = skynet.server.start_wallet:main",
            "skynet_full_node = skynet.server.start_full_node:main",
            "skynet_harvester = skynet.server.start_harvester:main",
            "skynet_farmer = skynet.server.start_farmer:main",
            "skynet_introducer = skynet.server.start_introducer:main",
            "skynet_timelord = skynet.server.start_timelord:main",
            "skynet_timelord_launcher = skynet.timelord.timelord_launcher:main",
            "skynet_full_node_simulator = skynet.simulator.start_simulator:main",
        ]
    },
    package_data={
        "skynet": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp", "py.typed"],
        "skynet.util": ["initial-*.yaml", "english.txt"],
        "skynet.ssl": ["skynet_ca.crt", "skynet_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
