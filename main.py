from libprobe.probe import Probe
from lib.check.hpilo import check_hpilo
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'hpilo': check_hpilo
    }

    probe = Probe("hpilo", version, checks)

    probe.start()
