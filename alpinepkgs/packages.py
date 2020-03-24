"""
Give you information about packages from pkgs.alpinelinux.org.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
import logging
import requests
from alpinepkgs.const import BASE_URL, BRANCHES

_LOGGER = logging.getLogger(__name__)


def get_package(package=None, branch=BRANCHES[-2]):
    """Get package information."""
    if package is None:
        _LOGGER.error("You need to specify a package!")
        return None

    if branch is None:
        branch = BRANCHES[-2]

    if branch not in BRANCHES:
        _LOGGER.error("Only %s are supported as the branch!", BRANCHES)
        return None

    data = {"package": package, "branch": branch}

    versions = []

    if "+" in package:
        package = package.replace("+", "%2B")

    url = BASE_URL.format(package, branch)

    get = requests.get(url)

    packages = get.text.replace("\n", "")
    packages = packages.split("<tbody>")[1]
    packages = packages.split("</tbody>")[0]
    packages = packages.split('<td class="package">')

    for architecture in packages:
        if architecture.replace(" ", "") != "<tr>":
            try:
                arch = architecture.split('<td class="arch">')[1]
                arch = arch.split("</td>")[0]
                arch = arch.split(">")[1]
                arch = arch.split("<")[0]
                arch = arch.strip()

                version = architecture.split('<td class="version">')[1]
                version = version.split("</td>")[0]
                if branch == "edge":
                    version = version.split(">")[2]
                    version = version.split("<")[0]

                if version not in versions:
                    versions.append(version)

                date = architecture.split('<td class="bdate">')[1]
                date = date.split("</td>")[0]
                date = date.split(" ")[0]

                licence = architecture.split('<td class="license">')[1]
                licence = licence.split("</td>")[0]

                maintainer = architecture.split('<td class="maintainer">')[1]
                maintainer = maintainer.split("</td>")[0]
                maintainer = maintainer.split(">")[1]
                maintainer = maintainer.split("<")[0]
                maintainer = maintainer.strip()

                url = architecture.split('<td class="url">')[1]
                url = url.split("</td>")[0]
                url = url.split('"')[1]
                url = url.replace("&#x2F;", "/")

                data[arch] = {
                    "version": version,
                    "date": date,
                    "licence": licence,
                    "maintainer": maintainer,
                    "url": url,
                }
            except IndexError:
                _LOGGER.error("Package %s not found on %s", package, branch)

    data["versions"] = versions

    return data
