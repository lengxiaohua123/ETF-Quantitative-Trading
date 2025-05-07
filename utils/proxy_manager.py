class ProxyManager:
    def __init__(self, proxies):
        self.proxies = proxies
        self.index = 0

    def get_proxy(self):
        proxy = self.proxies[self.index]
        self.index = (self.index + 1) % len(self.proxies)
        return proxy