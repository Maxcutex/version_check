class VersionChecker:
    def __init__(self):
        pass

    def check_version(self, r, s):
        r = int(r.replace(".", ""))
        s = int(s.replace(".", ""))

        return r > s