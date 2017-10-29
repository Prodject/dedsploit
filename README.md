# dedsploit

Framework for attacking network protocols and network exploitation.

__Official Website:__ http://dedsploit.tech

![Logo](logo.png)

## CHANGELOG: v3.0.0 10/29/17

Introducing the newest version of dedsploit. While many of the modules that have been presented in the earlier versions have been removed, the overall quality of the framework has been improved and revamped for usability.

* Removed the protocol/attack vector system, and make it so that the pentester can select their attack vector immediately from the start. 
* Did some redesigning, and improved the overall code quality.

We hope that you enjoy this rendition of your favorite penetration testing framework!

### I. Introduction

This framework aims to exploit and attack some common every-day vulnerabilities, whether it is a misconfiguration of a SSH server, or even the utilization of `apache2` as a web server, which could be subjected to malicious __Slowloris__ DoS attacks.

The framework comprises of several attack vectors:

    http
    ==========
    * slowloris
    
    net
    ==========
    * arpspoof
    * hosts
    * pscan
    
    smtp
    ==========
    * smsbomb
    
More modules will be deployed on a rolling basis.

### II. Installation & Usage

In order to install this program, it is best that you are on a __Linux-based__ distro, preferably __Kali-Linux__. You may also be on macOS, but this rollout is tentative and may be buggy.

## Quick n' Dirty One-liner

    $ curl https://raw.githubusercontent.com/ex0dus-0x/dedsploit/master/installer | sudo /bin/bash 

## Building from Source

First, `git clone`.

    $ git clone https://github.com/ex0dus-0x/dedsploit

Change directory, and then run the installer script (Must be root or have superuser permissions):

    $ cd /path/to/dedsploit
    $ ./installer

The `installer` script will install of the necessary dependencies for you.


Once finished, execute with:

    $ dedsploit

If you decide to build from source, do keep in mind that you may remove the repository you clone after installation, since dedsploit has been reinstalled elsewhere and is now part of your `$PATH`.

---

Example of the __ssh__ bruteforce module in use (__TODO__: obsolete, replace video!):

[![asciicast](https://asciinema.org/a/atqn7b3j8j24qzgtfhz3flqho.png)](https://asciinema.org/a/atqn7b3j8j24qzgtfhz3flqho)

### III. TODO

* [] Misc. module - may include embedded and IOT attack vectors
* [] Automate `git pull` as an auto "updater"
* [] Modules:
  - driftnet
  - smtp enumeration
  - mimikatz
* [] Installer / Uninstaller

### IV. Issues?

If you ever have any issues regarding the source code of this framework, as well as any errors you have encountered, please do not hesitate to open a new issue!

Of course, suggestions for modules and attack vectors are always welcome. dedsploit is a young yet-to-mature framework,
and we wish to make the best for penetration testers.
