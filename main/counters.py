from .utils import get_redis_client

PLAYLIST_COUNTER_KEY = "counter:playlists"


def incr_playlist_counter():
    get_redis_client().incr(PLAYLIST_COUNTER_KEY)


def get_playlist_count():
    return int(get_redis_client().get(PLAYLIST_COUNTER_KEY) or 0)
