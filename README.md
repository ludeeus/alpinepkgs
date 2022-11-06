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

