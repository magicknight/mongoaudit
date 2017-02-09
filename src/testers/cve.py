from src.tools import in_range

# https://www.mongodb.com/alerts


def alerts_dec012015(test):
    if "modules" in test.tester.info:
        enterprise = "enterprise" in test.tester.info["modules"]
        version = test.tester.info["version"]
        return not (enterprise and in_range(version, "3.0.0", "3.0.6"))
    else:
        return True

def alerts_mar272015(test):
    return test.tester.info["version"] != "3.0.0"

def alerts_mar252015(test):
    version = test.tester.info["version"]
    return version > "2.6.8" and version != "3.0.0"

def alerts_feb252015(test):
    version = test.tester.info["version"]
    return version > "2.6.7" or version == "2.4.13"

def alerts_jun172014(test):
    version = test.tester.info["version"]
    return version not in ["2.6.0", "2.6.1"]

def alerts_may052014(test):
    version = test.tester.info["version"]
    return version != "2.6.0"

def alerts_jun202013(test):
    version = test.tester.info["version"]
    return not in_range(version, "2.4.0", "2.4.4") and version != "2.5.1"

def alerts_jun052013(test):
    version = test.tester.info["version"]
    return not in_range(version, "2.4.0", "2.4.4")

def alerts_mar062014(test):
    version = test.tester.info["version"]
    return version > "2.3.1"


def alerts_oct012013(test):
    version = test.tester.info["version"]
    return version > "2.2.3"


def alerts_aug152013(test):
    version = test.tester.info["version"]
    return version > "2.5.1"