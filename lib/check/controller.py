from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

MAX_INT = 2 ** 32 - 1
QUERIES = (
    (MIB_INDEX['CPQIDA-MIB']['cpqDaCntlrEntry'], True),
)


async def check_controller(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)

    for item in state.get('cpqDaCntlrEntry', []):
        if item.get('cpqDaCntlrBlinkTime') == MAX_INT:
            item.pop('cpqDaCntlrBlinkTime')
        if item.get('cpqDaCntlrPartnerSlot') == -1:
            item.pop('cpqDaCntlrPartnerSlot')
        if item.get('cpqDaCntlrCurrentTemp') == -1:
            item.pop('cpqDaCntlrCurrentTemp')
    return state
