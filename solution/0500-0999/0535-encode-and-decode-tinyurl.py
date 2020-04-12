import random
import string

class Codec:
    def __init__(self):
        self.url_db = dict()
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.url_db:
            return self.url_db[longUrl]
        
        def gen_shortUrl():
            char = string.ascii_letters + string.digits
            s = "".join(random.choice(char) for x in range(6))
            shortUrl = self.base_url + s
        
        shortUrl = gen_shortUrl()
        while shortUrl in self.url_db.values():
            shortUrl = shortUrl = gen_shortUrl()
        
        self.url_db[longUrl] = shortUrl 
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        for k, v in self.url_db.items():
            if v == shortUrl:
                return k
        return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))