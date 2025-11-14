from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.check import Check
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

MAX_INT = 2 ** 32 - 1
QUERIES = (
    (MIB_INDEX['CPQIDA-MIB']['cpqDaCntlrEntry'], True),
)


class CheckController(Check):
    key = 'controller'

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        snmp = get_snmp_client(asset, local_config, config)
        state = await snmpquery(snmp, QUERIES)

        for item in state.get('cpqDaCntlrEntry', []):
            if item.get('cpqDaCntlrBlinkTime') in (MAX_INT, -1):
                item.pop('cpqDaCntlrBlinkTime')
            if item.get('cpqDaCntlrPartnerSlot') == -1:
                item.pop('cpqDaCntlrPartnerSlot')
            if item.get('cpqDaCntlrCurrentTemp') == -1:
                item.pop('cpqDaCntlrCurrentTemp')
        return state
