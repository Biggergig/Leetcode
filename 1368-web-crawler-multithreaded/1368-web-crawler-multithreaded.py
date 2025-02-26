# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from multiprocessing.pool import ThreadPool
class Solution:
    def __init__(self):
        self.to_process = set()
        self.res = set()
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        self.res.add(startUrl)
        self.to_process.add(startUrl)
    
        def getHost(url):return url.split('/')[2]

        host = getHost(startUrl)

        def helper(url):
            self.to_process.remove(url)
            for u in htmlParser.getUrls(url):
                if getHost(u) == host and u not in self.res:
                    self.res.add(u)
                    self.to_process.add(u)
        
        p = ThreadPool(18)
        while self.to_process:
            pool_output = p.map(helper, list(self.to_process))
        return list(self.res)