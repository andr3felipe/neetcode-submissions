class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sTable = dict()
        tTable = dict()

        for l in s:
            sTable[l] = sTable.get(l, 0) + 1

        for l in t:
            tTable[l] = tTable.get(l, 0) + 1

        if (len(sTable) != len(tTable)):
            return False

        for key, value in sTable.items():
            tValue = tTable.get(key, 0)
            if (sTable[key] != tValue):
                return False
        return True
        