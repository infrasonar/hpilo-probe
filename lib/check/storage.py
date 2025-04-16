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
    # cpqDaPhyDrvSSDEstTimeRemainingHours might be -1 in some cases, this value
    #   is provided as seconds on some devices, and minutes on other.
    #   Be careful with using this metric as the unit is not honored by many
    #   devices.
    # cpqDaPhyDrvPowerOnHours might be represented in minutes on some hardware
    #   while others return the value in hours.

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)

    for item in state.get('cpqDaPhyDrvEntry', []):
        if item.get('cpqDaLogDrvPercentRebuild') in (MAX_INT, -1):
            item.pop('cpqDaLogDrvPercentRebuild')
        if item.get('cpqDaLogDrvBlinkTime') in (MAX_INT, -1):
            item.pop('cpqDaLogDrvBlinkTime')
        if item.get('cpqDaLogDrvRPIPercentComplete') in (MAX_INT, -1):
            item.pop('cpqDaLogDrvRPIPercentComplete')

    for item in state.get('cpqDaPhyDrvEntry', []):
        if item.get('cpqDaPhyDrvFunctTest1') in (MAX_INT, -1):
            item.pop('cpqDaPhyDrvFunctTest1')
        if item.get('cpqDaPhyDrvFunctTest2') in (MAX_INT, -1):
            item.pop('cpqDaPhyDrvFunctTest2')
        if item.get('cpqDaPhyDrvFunctTest3') in (MAX_INT, -1):
            item.pop('cpqDaPhyDrvFunctTest3')
        if item.get('cpqDaPhyDrvDrqTimeouts') in (MAX_INT, -1):
            item.pop('cpqDaPhyDrvDrqTimeouts')
        if item.get('cpqDaPhyDrvPostErrs') in (MAX_INT, -1):
            item.pop('cpqDaPhyDrvPostErrs')
        if item.get('cpqDaPhyDrvBlinkTime') in (MAX_INT, -1):
            item.pop('cpqDaPhyDrvBlinkTime')
        if item.get('cpqDaPhyDrvPowerOnHours') in (MAX_INT, -1):
            item.pop('cpqDaPhyDrvPowerOnHours')
        if item.get('cpqDaPhyDrvSSDPercntEndrnceUsed') in (MAX_INT, -1):
            item.pop('cpqDaPhyDrvSSDPercntEndrnceUsed')
        if item.get('cpqDaPhyDrvSSDEstTimeRemainingHours') in (MAX_INT, -1):
            item.pop('cpqDaPhyDrvSSDEstTimeRemainingHours')
        if item.get('cpqDaPhyDrvBusNumber') == -1:
            item.pop('cpqDaPhyDrvBusNumber')
        if item.get('cpqDaPhyDrvBoxOnConnector') == -1:
            item.pop('cpqDaPhyDrvBoxOnConnector')
        if item.get('cpqDaPhyDrvPhyCount') == -1:
            item.pop('cpqDaPhyDrvPhyCount')
        if item.get('cpqDaPhyDrvCurrentTemperature') == -1:
            item.pop('cpqDaPhyDrvCurrentTemperature')
        if item.get('cpqDaPhyDrvTemperatureThreshold') == -1:
            item.pop('cpqDaPhyDrvTemperatureThreshold')
        if item.get('cpqDaPhyDrvMaximumTemperature') == -1:
            item.pop('cpqDaPhyDrvMaximumTemperature')
    return state
