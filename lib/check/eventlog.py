from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.check import Check
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['CPQHLTH-MIB']['cpqHeEventLogEntry'], True),
)


class CheckEventLog(Check):
    key = 'eventlog'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        snmp = get_snmp_client(asset, local_config, config)
        state = await snmpquery(snmp, QUERIES)
        for item in state.get('cpqHeEventLogEntry', []):
            item.pop('cpqHeEventLogFreeFormData', None)
            if item.get('cpqDaLogDrvRebuildingPhyDrv') == -1:
                item.pop('cpqDaLogDrvRebuildingPhyDrv')
            if item.get('cpqDaLogDrvCacheVolIndex') == -1:
                item.pop('cpqDaLogDrvCacheVolIndex')

        return state
