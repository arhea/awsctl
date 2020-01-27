import click
from awsctl.packages.ssm import AmazonSystemsManager
from awsctl.packages.cloudwatch import AmazonCloudwatch, AmazonCloudwatchLogs
from awsctl.packages.inspector import AmazonInspector

@click.group("install")
def install_group():
    pass

@install_group.command("ssm")
def install_ssm():
    ssm = AmazonSystemsManager()
    ssm.install()

@install_group.command("cloudwatch")
def install_cloudwatch():
    cloudwatch = AmazonCloudwatch()
    cloudwatch.install()

@install_group.command("cloudwatch-logs")
@click.argument('region')
@click.argument('config')
def install_cloudwatch_logs(region, config):
    cloudwatch = AmazonCloudwatchLogs()
    cloudwatch.install(region, config)

@install_group.command("inspector")
def install_inspector():
    inspector = AmazonInspector()
    inspector.install()
