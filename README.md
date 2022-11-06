# alpinepkgs

_Give you information about packages from pkgs.alpinelinux.org._
**NB!: This package uses web scraping to gather the information.**

## Install

```bash
pip install alpinepkgs
```

### Example

```python
from alpinepkgs.packages import get_package
print(get_package('nginx'))

> {'x86_64': {'date': '2018-12-11', 'licence': 'BSD-2-Clause', 'url': 'http://www.nginx.org/en', 'version': '1.14.2-r0', 'maintainer': 'Jakub Jirutka'}, 'armhf': {'date': '2018-12-11', 'licence': 'BSD-2-Clause', 'url': 'http://www.nginx.org/en', 'version': '1.14.2-r0', 'maintainer': 'Jakub Jirutka'}, 's390x': {'date': '2018-12-11', 'licence': 'BSD-2-Clause', 'url': 'http://www.nginx.org/en', 'version': '1.14.2-r0', 'maintainer': 'Jakub Jirutka'}, 'x86': {'date': '2018-12-11', 'licence': 'BSD-2-Clause', 'url': 'http://www.nginx.org/en', 'version': '1.14.2-r0', 'maintainer': 'Jakub Jirutka'}, 'aarch64': {'date': '2018-12-11', 'licence': 'BSD-2-Clause', 'url': 'http://www.nginx.org/en', 'version': '1.14.2-r0', 'maintainer': 'Jakub Jirutka'}, 'ppc64le': {'date': '2018-12-11', 'licence': 'BSD-2-Clause', 'url': 'http://www.nginx.org/en', 'version': '1.14.2-r0', 'maintainer': 'Jakub Jirutka'}, 'package': 'nginx', 'branch': 'v3.8'}
```

### CLI Example

```bash
alpinepkgs --package nginx --branch v3.8
{
    "aarch64": {
        "date": "2018-12-11",
        "licence": "BSD-2-Clause",
        "maintainer": "Jakub Jirutka",
        "url": "http://www.nginx.org/en",
        "version": "1.14.2-r0"
    },
    "armhf": {
        "date": "2018-12-11",
        "licence": "BSD-2-Clause",
        "maintainer": "Jakub Jirutka",
        "url": "http://www.nginx.org/en",
        "version": "1.14.2-r0"
    },
    "branch": "v3.8",
    "package": "nginx",
    "ppc64le": {
        "date": "2018-12-11",
        "licence": "BSD-2-Clause",
        "maintainer": "Jakub Jirutka",
        "url": "http://www.nginx.org/en",
        "version": "1.14.2-r0"
    },
    "s390x": {
        "date": "2018-12-11",
        "licence": "BSD-2-Clause",
        "maintainer": "Jakub Jirutka",
        "url": "http://www.nginx.org/en",
        "version": "1.14.2-r0"
    },
    "x86": {
        "date": "2018-12-11",
        "licence": "BSD-2-Clause",
        "maintainer": "Jakub Jirutka",
        "url": "http://www.nginx.org/en",
        "version": "1.14.2-r0"
    },
    "x86_64": {
        "date": "2018-12-11",
        "licence": "BSD-2-Clause",
        "maintainer": "Jakub Jirutka",
        "url": "http://www.nginx.org/en",
        "version": "1.14.2-r0"
    }
}
```
