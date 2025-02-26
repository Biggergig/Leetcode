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
from queue import Queue # thread safe
import threading

class Solution:
    def __init__(self):
        self.queue = Queue()
        self.res = set()
        self.res_lock = threading.Lock()
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        with self.res_lock:
            self.res.add(startUrl)
        self.queue.put(startUrl)
    
        def getHost(url):return url.split('/')[2]

        host = getHost(startUrl)

        def helper(url):
            for u in htmlParser.getUrls(url):
                with self.res_lock:
                    if getHost(u) == host and u not in self.res:
                        self.res.add(u)
                        self.queue.put(u)
        
        p = ThreadPool(18)
        while not self.queue.empty():
            urls = []
            while not self.queue.empty():
                urls.append(self.queue.get())
            pool_output = p.map(helper, urls)
        return list(self.res)