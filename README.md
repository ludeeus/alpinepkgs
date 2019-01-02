# alpinepkgs [![Build Status](https://travis-ci.com/ludeeus/alpinepkgs.svg?branch=master)](https://travis-ci.com/ludeeus/alpinepkgs)

_Give you information about packages from pkgs.alpinelinux.org._  
**NB!: This package uses web scraping to gather the information.**

## Install

```bash
pip install alpinepkgs
```

### Example

```python
from alpinepkgs.packages import Packages

pkgs = Packages('nginx', 'v3.8')
print(pkgs.get_package())
```

***

[![BuyMeCoffee](https://camo.githubusercontent.com/cd005dca0ef55d7725912ec03a936d3a7c8de5b5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6275792532306d6525323061253230636f666665652d646f6e6174652d79656c6c6f772e737667)](https://www.buymeacoffee.com/ludeeus)