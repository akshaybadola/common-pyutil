import time
import magic
import requests
from common_pyutil import net


def test_get_progress():
    get = net.Get()
    url = "https://arxiv.org/pdf/2009.02773.pdf"
    get(url)
    time.sleep(.5)
    assert get.progress(url) is not None
    get.abort(url)
    get.reset()


def test_get_download():
    get = net.Get()
    url = "https://arxiv.org/pdf/1510.03055.pdf"
    get(url)
    time.sleep(.5)
    while not get.finished(url):
        time.sleep(1)
    _, _, result = get.result(url)
    assert "pdf" in magic.detect_from_content(bytes(result)).mime_type
