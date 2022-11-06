"""Give you information about packages from pkgs.alpinelinux.org."""
import logging
import requests

_LOGGER = logging.getLogger(__name__)

PACKAGE_URL = "https://pkgs.alpinelinux.org/packages?name={}&branch={}"
RELEASE_URL = "https://www.alpinelinux.org/releases/"


def get_package(package: str, branch: str = None):
    """Get package information."""
    if package is None:
        _LOGGER.error("You need to specify a package!")
        return None

    if branch is None:
        try:
            branch = get_latest_branch()
        except Exception: ## pylint: disable=broad-except
            _LOGGER.error("Could not determine latest Alpine release.")


    data = {"package": package, "branch": branch, "versions": []}

    if "+" in package:
        package = package.replace("+", "%2B")

    get = requests.get(PACKAGE_URL.format(package, branch), timeout=20)

    packages = (
        get.text.replace("\n", "")
        .split("<tbody>")[1]
        .split("</tbody>")[0]
        .split('<td class="package">')
    )

    for architecture in packages:
        if architecture.replace(" ", "") == "<tr>":
            continue

        try:
            arch = (
                architecture.split('<td class="arch">')[1]
                .split("</td>")[0]
                .split(">")[1]
                .split("<")[0]
                .strip()
            )
            version = architecture.split('<td class="version">')[1].split("</td>")[0]

            if version not in data["versions"]:
                data["versions"].append(version)

            data[arch] = {
                "version": version
                if branch != "edge"
                else version.split(">")[2].split("<")[0],
                "date": (
                    architecture.split('<td class="bdate">')[1]
                    .split("</td>")[0]
                    .split(" ")[0]
                    .strip()
                ),
                "licence": architecture.split('<td class="license">')[1]
                .split("</td>")[0]
                .strip(),
                "maintainer": (
                    architecture.split('<td class="maintainer">')[1]
                    .split("</td>")[0]
                    .split(">")[1]
                    .split("<")[0]
                    .strip()
                ),
                "url": (
                    architecture.split('<td class="url">')[1]
                    .split("</td>")[0]
                    .split('"')[1]
                    .replace("&#x2F;", "/")
                    .strip()
                ),
            }
        except IndexError:
            _LOGGER.error("Package %s not found on %s", package, branch)

    return data


def get_latest_branch():
    """Scrape the latest branch from https://www.alpinelinux.org/releases/."""
    return (
        requests.get(RELEASE_URL, timeout=20)
        .text.replace("\n", "")
        .split("<tr>")[3]
        .split("<td>")[1]
        .split(">")[1]
        .split("<")[0]
    )
