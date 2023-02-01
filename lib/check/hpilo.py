from asyncsnmplib.mib.mib_index import MIB_INDEX
from asyncsnmplib.exceptions import SnmpNoAuthParams, SnmpNoConnection
from asyncsnmplib.utils import InvalidConfigException, snmp_queries
from libprobe.asset import Asset
from libprobe.exceptions import CheckException, IgnoreResultException

QUERIES = (
    MIB_INDEX['UBNT-UniFi-MIB']['hpiloApSystem'],
    MIB_INDEX['UBNT-UniFi-MIB']['hpiloRadioEntry'],
    MIB_INDEX['UBNT-UniFi-MIB']['hpiloVapEntry'],
)


async def check_hpilo(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    address = check_config.get('address')
    if address is None:
        address = asset.name
    try:
        state = await snmp_queries(address, asset_config, QUERIES)
    except SnmpNoConnection:
        raise CheckException('unable to connect')
    except (InvalidConfigException, SnmpNoAuthParams):
        raise IgnoreResultException
    except Exception:
        raise
    for item in state.get('hpiloRadioEntry', []):
        item.pop('hpiloRadioIndex')
        item['name'] = item.pop('hpiloRadioName')
    for item in state.get('hpiloVapEntry', []):
        item.pop('hpiloVapIndex')
        item['name'] = item.pop('hpiloVapName')
    return state
