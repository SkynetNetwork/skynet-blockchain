from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": ("skynet_harvester skynet_timelord_launcher skynet_timelord " "skynet_farmer skynet_full_node skynet_wallet").split(),
    "node": "skynet_full_node".split(),
    "harvester": "skynet_harvester".split(),
    "farmer": "skynet_harvester skynet_farmer skynet_full_node skynet_wallet".split(),
    "farmer-no-wallet": "skynet_harvester skynet_farmer skynet_full_node".split(),
    "farmer-only": "skynet_farmer".split(),
    "timelord": "skynet_timelord_launcher skynet_timelord skynet_full_node".split(),
    "timelord-only": "skynet_timelord".split(),
    "timelord-launcher-only": "skynet_timelord_launcher".split(),
    "wallet": "skynet_wallet skynet_full_node".split(),
    "wallet-only": "skynet_wallet".split(),
    "introducer": "skynet_introducer".split(),
    "simulator": "skynet_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
