import socket

class Resolver:

#Initialises the Resolver class with a callable function eg. resolve = Resolver()// resolve._cache
    def __init__(self):
        self._cache = {}

#Adds a callable function which resolve('hostname.com') will return the IP of hostname and add hostname into cache
    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

#Clears the list of cache created by __call__
    def clear(self):
        self._cache.clear()

#Checks if resolver.has_host(hostname.com) is in cache - returns boolean
    def has_host(self, host):
        return host in self._cache