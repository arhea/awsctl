import subprocess
import click
import requests
import os
import platform
from typing import List
from enum import Enum

class OSDistrubtion(Enum):
    AMAZON = "amzn"
    CENTOS = "centos"
    DEBIAN = "debian"
    REDHAT = "redhat"
    UBUNTU_1804 = "ubuntu1804"
    UBUNTU_1604 = "ubuntu1604"

class PackageBase(object):
    """The base class for AWS Packages.

    This class contains utilities for running commands via
    package managers and managing systemd agents.
    """

    def __init__(self):
        self.os = self.get_os_distribution()

    def apt_update(self) -> bool:
        """Update the Apt Cache
        
        Returns:
            bool: True if the command executed successfully
        """

        args = ["apt-get", "update", "-y"]
        return self.run_shell(args)

    def apt_install(self, package: str) -> bool:
        """Install a package with Apt
        
        Args:
            package (str): -- The name of the package

        Returns:
            bool: True if the command executed successfully
        """

        args = ["apt-get", "install", "-y", package]
        return self.run_shell(args)

    def apt_remove(self, package: str) -> bool:
        """Remove a package with Apt
        
        Args:
            package (str): -- The name of the package

        Returns:
            bool: True if the command executed successfully
        """

        args = ["apt-get", "remove", "-y", package]
        return self.run_shell(args)

    def apt_install_deb(self, url: str) -> bool:
        """Install a debian package from a URL.
        
        Args:
            package (str): -- The name of the package
        
        Returns:
            bool: True if the command executed successfully
        """

        filename = os.path.join("/tmp", os.path.basename(url))
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)

        args = ["dpkg", "-i", filename]
        return self.run_shell(args)

    def yum_update(self) -> bool:
        """Update the operating system with Yum

        Returns:
            bool: True if the command executed successfully
        """

        args = ["yum", "update", "-y"]
        return self.run_shell(args)

    def yum_install(self, package: str) -> bool:
        """Install a package with Yum
        
        Args:
            package (str): -- The name of the package

        Returns:
            bool: True if the command executed successfully
        """

        args = ["yum", "install", "-y", package]
        return self.run_shell(args)

    def yum_remove(self, package: str) -> bool:
        """Remove a package with Yum
        
        Args:
            package (str): -- The name of the package

        Returns:
            bool: True if the command executed successfully
        """
    
        args = ["yum", "remove", "-y", package]
        return self.run_shell(args)

    def systemctl_status(self, name: str) -> bool:
        """Check the status of an agent in Systemd
        
        Args:
            name (str): -- The name of the agent
        
        Returns:
            bool: True if the command executed successfully
        """

        args = ["systemctl", "status", name]
        return self.run_shell(args)

    def systemctl_enable(self, name: str) -> bool:
        """Enable an agent in Systemd
        
        Args:
            name (str): -- The name of the agent
        
        Returns:
            bool: True if the command executed successfully
        """

        args = ["systemctl", "enable", name]
        return self.run_shell(args)

    def systemctl_start(self, name: str) -> bool:
        """Start an agent in Systemd
        
        Args:
            name (str): -- The name of the agent
        """

        args = ["systemctl", "start", name]
        return self.run_shell(args)

    def systemctl_stop(self, name: str) -> bool:
        """Stop an agent in Systemd
        
        Args:
            name (str): -- The name of the agent
        
        Returns:
            bool: True if the command executed successfully
        """

        args = ["systemctl", "stop", name]
        return self.run_shell(args)

    def snap_install(self, package: str, is_classic=True) -> bool:
        """Install a package via Snap
        
        Args:
            package (str): the name of the package
            is_classic (bool): include the --classic flag (default: True)

        Returns:
            bool: True if the command executed successfully
        """

        args = ["snap", "install", package]

        if is_classic:
            args.append("--classic")

        return self.run_shell(args)

    def snap_start(self, package: str) -> bool:
        """Start a Snap package
        
        Args:
            package (str): -- The name of the package
        
        Returns:
            bool: True if the command executed successfully
        """

        args = ["snap", "start", package]
        return self.run_shell(args)

    def run_shell(self, args: list) -> bool:
        """Run a shell command on the operating system
        
        Args:
            args (list) -- a list of command components

        Returns:
            bool: True if the command executed successfully

        Raises:
            click.Abort: If the command fails to execute
        """

        click.secho(" ".join(args), fg="white")
        result = subprocess.run(args)

        if result.returncode == 0:
            return True
        else:
            message = "Error Running Process: {}".format(result.stderr)
            click.secho(message, color="Red")
            raise click.Abort(message)

    def get_os_info(self):
        with open("/etc/os-release") as f:
            info = {}
            for line in f:
                k,v = line.rstrip().split("=")
                info[k] = v.strip('"')

        return info
    
    def get_os_distribution(self):
        info = self.get_os_info()
        id = info.get('ID').lower()
        version = info.get('VERSION_ID')

        if id == "amzn" and version == "2":
            return OSDistrubtion.AMAZON
        elif id == "centos":
            return OSDistrubtion.CENTOS
        elif id == "debian":
            return OSDistrubtion.DEBIAN
        elif id == "redhat":
            return OSDistrubtion.REDHAT
        elif id == "ubuntu" and version == "18.04":
            return OSDistrubtion.UBUNTU_1804
        elif id == "ubuntu" and version == "16.04":
            return OSDistrubtion.UBUNTU_1604
        else:
            raise Exception("Operating System Not Supported!")
