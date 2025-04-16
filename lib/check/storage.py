from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

MAX_INT = 2 ** 32 - 1
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

    for item in state.get('cpqDaPhyDrvEntry', []):
        if item.get('cpqDaLogDrvPercentRebuild') == MAX_INT:
            item['cpqDaLogDrvPercentRebuild'] = None
        if item.get('cpqDaLogDrvBlinkTime') == MAX_INT:
            item['cpqDaLogDrvBlinkTime'] = None
        if item.get('cpqDaLogDrvRPIPercentComplete') == MAX_INT:
            item['cpqDaLogDrvRPIPercentComplete'] = None

    for item in state.get('cpqDaPhyDrvEntry', []):
        if item.get('cpqDaPhyDrvFunctTest1') == MAX_INT:
            item['cpqDaPhyDrvFunctTest1'] = None
        if item.get('cpqDaPhyDrvFunctTest2') == MAX_INT:
            item['cpqDaPhyDrvFunctTest2'] = None
        if item.get('cpqDaPhyDrvFunctTest3') == MAX_INT:
            item['cpqDaPhyDrvFunctTest3'] = None
        if item.get('cpqDaPhyDrvDrqTimeouts') == MAX_INT:
            item['cpqDaPhyDrvDrqTimeouts'] = None
        if item.get('cpqDaPhyDrvPostErrs') == MAX_INT:
            item['cpqDaPhyDrvPostErrs'] = None
        if item.get('cpqDaPhyDrvBlinkTime') == MAX_INT:
            item['cpqDaPhyDrvBlinkTime'] = None
        if item.get('cpqDaPhyDrvPowerOnHours') == MAX_INT:
            item['cpqDaPhyDrvPowerOnHours'] = None
        if item.get('cpqDaPhyDrvSSDPercntEndrnceUsed') == MAX_INT:
            item['cpqDaPhyDrvSSDPercntEndrnceUsed'] = None
        if item.get('cpqDaPhyDrvSSDEstTimeRemainingHours') == MAX_INT:
            item['cpqDaPhyDrvSSDEstTimeRemainingHours'] = None
        if item.get('cpqDaPhyDrvBusNumber') == -1:
            item['cpqDaPhyDrvBusNumber'] = None
        if item.get('cpqDaPhyDrvBoxOnConnector') == -1:
            item['cpqDaPhyDrvBoxOnConnector'] = None
        if item.get('cpqDaPhyDrvPhyCount') == -1:
            item['cpqDaPhyDrvPhyCount'] = None
        if item.get('cpqDaPhyDrvCurrentTemperature') == -1:
            item['cpqDaPhyDrvCurrentTemperature'] = None
        if item.get('cpqDaPhyDrvTemperatureThreshold') == -1:
            item['cpqDaPhyDrvTemperatureThreshold'] = None
        if item.get('cpqDaPhyDrvMaximumTemperature') == -1:
            item['cpqDaPhyDrvMaximumTemperature'] = None
    return state
