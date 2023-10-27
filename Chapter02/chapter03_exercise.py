# apply map() to a sequance of values


from collections.abc import Callable
from typing import Tuple


def actual_rpm(observed_rpm: int) -> int:
    return int(0.9 * observed_rpm - 90)


def table_rpm() -> None:
    rpm_range = range(800, 2600, 100)
    actual_rpms = map(actual_rpm, rpm_range)
    print("{:>10} {:>10}".format("Observed", "Actual"))
    zipped = zip(rpm_range, actual_rpms)
    for rpms in zipped:
        print("{:>10} {:>10}".format(rpms[0], rpms[1]))


def rpm_range(lower: int, upper: int) -> Tuple:
    return tuple(range(lower, upper + 100, 100))


def pair_rpms(model: Callable, rpm_range: Tuple) -> Tuple:
    return tuple((x, model(x)) for x in rpm_range)


def table_rpm2(rpms: Tuple) -> None:
    print("{:>10} {:>10}".format("Observed", "Actual"))
    paired = pair_rpms(actual_rpm, rpm_range(800, 2500))
    for pairs in paired:
        print("{:>10} {:>10}".format(pairs[0], pairs[1]))
