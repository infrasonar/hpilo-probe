from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    MIB_INDEX['CPQHLTH-MIB']['cpqHeEventLogEntry'],
)


async def check_eventlog(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)
    for item in state.get('cpqHeEventLogEntry', []):
        item.pop('cpqHeEventLogFreeFormData', None)
    return state
