from http.cookiejar import MozillaCookieJar

import requests


def download_file(url, output, cookie_jar: MozillaCookieJar):
    s = requests.Session()
    for cookie in cookie_jar:
        s.cookies.set(cookie.name, cookie.value)

    local_filename = output
    # NOTE the stream=True parameter below
    with s.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename
