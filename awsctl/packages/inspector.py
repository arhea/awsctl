from awsctl.packages.common import PackageBase, OSDistrubtion
import click
import requests
import os

class AmazonInspector(PackageBase):

    def install(self):
        url = "https://inspector-agent.amazonaws.com/linux/latest/install"
        filename = os.path.join("/tmp", "inspector-install.bash")

        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)

        self.run_shell(["chmod", "+x", filename])
        self.run_shell(["bash", filename])

