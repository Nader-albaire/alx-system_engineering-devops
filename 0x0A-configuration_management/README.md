Configuration Management Project
Overview


This project delves into the realm of configuration management, a crucial aspect of DevOps and system administration. Drawing inspiration from experiences like SlideShare's Skynet incident, where automated remediation proved invaluable, this project emphasizes the importance of tools like Puppet in managing infrastructure efficiently.
Project Timeline

    Start: Mar 22, 2024, 6:00 AM
    End: Mar 23, 2024, 6:00 AM
    Checker Release: Mar 22, 2024, 12:00 PM
    Auto Review: Scheduled for the deadline

Background Context

The project draws on real-world experiences, such as the Skynet incident, where misconfiguration caused significant disruptions. Utilizing Puppet, a powerful configuration management tool, helps streamline infrastructure management and remediation processes. Puppet allows for the declarative modeling of infrastructure, enabling efficient orchestration and rapid recovery from incidents.
Resources

To deepen your understanding, explore the following resources:

    Intro to Configuration Management
    Puppet resource type: file
    Puppet’s Declarative Language: Modeling Instead of Scripting
    Puppet lint
    Puppet emacs mode

Requirements
General

    Execution Environment: Ubuntu 20.04 LTS
    All files should end with a new line
    Mandatory README.md file at the project root
    Puppet manifests must pass puppet-lint version 2.1.1 without errors
    Puppet manifests must run without errors
    Puppet manifests should start with a comment explaining their purpose
    Puppet manifest files must end with the extension .pp

Versioning

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled. Ensure Puppet is installed using the provided instructions.

bash

# Install puppet
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet

Note: Upgrading versions is unnecessary for this project.
