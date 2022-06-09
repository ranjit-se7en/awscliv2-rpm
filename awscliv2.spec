Summary: AWS CLI version 2
License: Apache License 2.0
Name: awscliv2
URL: https://docs.aws.amazon.com/cli/
Version: 2.4.18
Release: 1%{?dist}
Source0: https://awscli.amazonaws.com/awscli-exe-linux-%{_arch}.zip
Source1: awscli-exe-linux-%{_arch}.zip.sha256
NoSource: 0

# skip debuginfo
%define debug_package %{nil}

%description
The AWS Command Line Interface (AWS CLI) is an open
source tool that enables you to interact with AWS
services using commands in your command-line shell.

%prep
cp "%{S:0}" ./
sha256sum -c "%{S:1}"
%setup -q -n aws

%build

%install
sh -x ./install --install-dir %{buildroot}/usr/local/aws-cli --bin-dir %{buildroot}/usr/local/bin

# redo symlinks to avoid complaint about them containing RPM_BUILD_ROOT
ln -sf ../aws-cli/v2/current/bin/aws %{buildroot}/usr/local/bin/aws
ln -sf ../aws-cli/v2/current/bin/aws_completer %{buildroot}/usr/local/bin/aws_completer

rm -f %{buildroot}/usr/local/aws-cli/v2/current
ln -sf 2.7.6 %{buildroot}/usr/local/aws-cli/v2/current

rm -f %{buildroot}/usr/local/bin/aws
ln -sf ../aws-cli/v2/current/bin/aws %{buildroot}/usr/local/bin/aws2

%check
%{buildroot}/usr/local/bin/aws2 --version

%files
/usr/local/bin/aws2
/usr/local/bin/aws_completer
/usr/local/aws-cli
