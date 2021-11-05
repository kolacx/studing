

class ATGearboxModes:
    neutral = 0
    parking = 1
    drive = 2
    reverse = 3
    manual = 4


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class CarStatus:
    started = 'Engine is Started. Bo-Bo-Bo-Bo-Bo-Bo-Bo'
    stoped = 'Engine is Stoped...'
    run_engine = bcolors.FAIL + 'First Start Engine <S>' + bcolors.ENDC
    rpm_cutoff = bcolors.FAIL + 'RATA-TA-TA-TA-TA-TA-TA-TA' + bcolors.ENDC
    rpm_up = 'RPM UP'
    rpm_down = 'RPM DOWN'
    engine_down = bcolors.FAIL + 'Engine is down. See you at retake' + bcolors.ENDC