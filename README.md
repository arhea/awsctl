# AWSCTL

`awsctl` is a utility for installing AWS packages on servers in the cloud. AWS packages such as Systems Manager, Cloudwatch, etc. have different installation methods which can be hard to manage when setting up a simple server. This package aims to make this as simple as `awsctl install ssm`.

```bash
# debian based systems
apt-get update -y && apt-get install -y python3 python3-pip
pip install --upgrade awsctl-cli

# centos based systems
yum update -y && yum install -y python3 python3-pip
pip install --upgrade awsctl-cli
```

## Supported Agents

| Package | Command | Description |
|-|-|-|
| Cloudwatch | `awsctl install cloudwatch` | Installs the Cloudwatch agent and configures it to run on startup. |
| Cloudwatch Logs | `awsctl install cloudwatch --region="<region"> --config=<config file>` | Installs and configures Cloudwatch Logging Agent. |
| Inspector | `awsctl install inspector` | Installs the Inspector agent and configures it to run on startup. |
| Systems Manager | `awsctl install ssm` | Installs the SSM agent and configures it to run on startup. |\

## Supported Operating Systems

Due to different installation methods we only support a subset of operating systems. We welcome additional operating systems!

| Operating System | Supported |
|-|:-:|
| Amazon Linux | :x: |
| Amazon Linux 2 | :white_check_mark: |
| Debian | :white_check_mark: |
| CentOS | :white_check_mark: |
| Red Hat | :white_check_mark: |
| Ubuntu 16.04 | :x: |
| Ubuntu 18.04 | :white_check_mark: |
