from awsctl.packages.common import PackageBase, OSDistrubtion
import click
import requests
import os

class AmazonCloudwatch(PackageBase):

    def install(self):
        if self.os == OSDistrubtion.AMAZON:
            self.install_rpm()
        elif self.os == OSDistrubtion.CENTOS:
            self.install_rpm()
        elif self.os == OSDistrubtion.DEBIAN:
            self.install_debian()
        elif self.os == OSDistrubtion.REDHAT:
            self.install_rpm()
        elif self.os == OSDistrubtion.UBUNTU_1604:
            self.install_debian()
        elif self.os == OSDistrubtion.UBUNTU_1804:
            self.install_debian()
        else:
            raise click.Abort("OS not supported by Amazon Cloudwatch Agent.")

    def install_debian(self):
        self.apt_install_deb("https://s3.amazonaws.com/amazoncloudwatch-agent/debian/amd64/latest/amazon-cloudwatch-agent.deb")
        self.systemctl_enable("amazon-cloudwatch-agent")
        self.systemctl_start("amazon-cloudwatch-agent")

    def install_rpm(self):
        self.yum_install("https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm")
        self.systemctl_enable("amazon-cloudwatch-agent")
        self.systemctl_start("amazon-cloudwatch-agent")

class AmazonCloudwatchLogs(PackageBase):

    def install(self, region: str, config: str):
        url = "https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/awslogs-agent-setup.py"
        filename = os.path.join("/tmp", "awslogs-agent-setup.py")

        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)

        self.run_shell(["chmod", "+x", filename])

        self.run_shell([filename, "-n", "-r", region, "-c", config])
