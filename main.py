from libprobe.probe import Probe
from lib.check.controller import CheckController
from lib.check.eventlog import CheckEventLog
from lib.check.storage import CheckStorage
from lib.check.system import CheckSystem
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckController,
        CheckEventLog,
        CheckStorage,
        CheckSystem,
    )

    probe = Probe("hpilo", version, checks)

    probe.start()
