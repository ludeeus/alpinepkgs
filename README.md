# alpinepkgs

_Give you information about packages from pkgs.alpinelinux.org._

**NOTE!: This package uses web scraping to gather the information.**

## Install

```bash
pip install alpinepkgs
```

### Example

```python
from alpinepkgs.packages import get_package
print(get_package('python3'))

> {'package': 'python3', 'branch': 'v3.16', 'x86_64': {'version': '3.10.5-r0', 'date': '2022-07-25', 'licence': 'PSF-2.0', 'maintainer': 'Natanael Copa', 'url': 'https://www.python.org/'}, 'x86': {'version': '3.10.5-r0', 'date': '2022-07-25', 'licence': 'PSF-2.0', 'maintainer': 'Natanael Copa', 'url': 'https://www.python.org/'}, 'aarch64': {'version': '3.10.5-r0', 'date': '2022-07-25', 'licence': 'PSF-2.0', 'maintainer': 'Natanael Copa', 'url': 'https://www.python.org/'}, 'armhf': {'version': '3.10.5-r0', 'date': '2022-07-25', 'licence': 'PSF-2.0', 'maintainer': 'Natanael Copa', 'url': 'https://www.python.org/'}, 's390x': {'version': '3.10.5-r0', 'date': '2022-07-25', 'licence': 'PSF-2.0', 'maintainer': 'Natanael Copa', 'url': 'https://www.python.org/'}, 'armv7': {'version': '3.10.5-r0', 'date': '2022-07-25', 'licence': 'PSF-2.0', 'maintainer': 'Natanael Copa', 'url': 'https://www.python.org/'}, 'ppc64le': {'version': '3.10.5-r0', 'date': '2022-07-25', 'licence': 'PSF-2.0', 'maintainer': 'Natanael Copa', 'url': 'https://www.python.org/'}, 'versions': ['3.10.5-r0']}
```

