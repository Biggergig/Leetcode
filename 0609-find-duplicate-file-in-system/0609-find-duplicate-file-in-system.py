from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)
        for p in paths:
            dirname, *files = p.split()
            for f in files:
                name,content = f.split('(')
                contents[content].append(dirname+"/"+name)
        return [l for l in contents.values() if len(l)>1]

        