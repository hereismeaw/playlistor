from .utils import get_redis_client

PLAYLIST_COUNTER_KEY = "counter:playlists"


class Counters:
    def incr(self, key):
        get_redis_client().incr(key)

    def incr_playlist_counter(self, key=PLAYLIST_COUNTER_KEY):
        self.incr(key)
