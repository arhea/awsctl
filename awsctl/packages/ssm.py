from awsctl.packages.common import PackageBase, OSDistrubtion
import click

class AmazonSystemsManager(PackageBase):

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
            self.install_snap()
        else:
            raise click.Abort("OS not supported by Amazon SSM Agent.")

    def install_debian(self):
        self.yum_install("https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm")
        self.systemctl_enable("amazon-ssm-agent")
        self.systemctl_start("amazon-ssm-agent")

    def install_rpm(self):
        self.yum_install("https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm")
        self.systemctl_enable("amazon-ssm-agent")
        self.systemctl_start("amazon-ssm-agent")

    def install_snap(self):
        self.snap_install("amazon-ssm-agent")
        self.snap_start("amazon-ssm-agent")
