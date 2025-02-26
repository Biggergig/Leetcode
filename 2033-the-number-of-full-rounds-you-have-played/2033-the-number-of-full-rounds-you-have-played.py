from math import ceil
class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        def toMin(time):
            hours,mins = map(int,time.split(":"))
            return hours*60+mins
        login = toMin(loginTime)
        logout = toMin(logoutTime)
        if logout < login:
            logout += 24*60
        r = range(ceil(login/15) * 15, logout-15+1, 15)
        # print([((n//60)%24, n%60) for n in r])
        return len(r)