from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['CPQIDA-MIB']['cpqDaLogDrvEntry'], True),
    (MIB_INDEX['CPQIDA-MIB']['cpqDaPhyDrvEntry'], True),
)


async def check_storage(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)
    return state
