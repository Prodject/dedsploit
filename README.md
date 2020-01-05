# dedsploit

Network protocol auditing framework

## intro

__dedsploit__ is an open-sourced network protocol auditing framework that supports the use of various plugin modules for
attacking various network-based protocols.

> NOTE: This is a project made from my earliest days, so development will be inactive, with sparse changes over time for consistency.

## usage

In order to use __dedsploit__ you can either install through `pip`:

```
$ pip3.6 install dedsploit --user
```

or install manually:

```
$ python setup.py install
# .. or `develop` for a local build for development
```

To run:

```
$ dedsploit

    .___         .___             .__         .__  __
  __| _/____   __| _/____________ |  |   ____ |__|/  |_
 / __ |/ __ \ / __ |/  ___/\____ \|  |  /  _ \|  \   __|
/ /_/ \  ___// /_/ |\___ \ |  |_> >  |_(  <_> )  ||  |
\____ |\___  >____ /____  >|   __/|____/\____/|__||__|
     \/    \/     \/    \/ |__|



         [   Version: 3.0.0                     ]
         [   Modules: 3                         ]

For available commands, type 'help'.
For available modules, enter 'modules'. Exit with Ctrl + C or 'exit'.

[>>] help

[Commands Available:]

help                    Display available commands and modules
modules                 Show modules that can be used
clear                   Move the screen up to clear it
update                  Update dedsploit!
exit                    Exit the program or current module
use ...                 Select a module for use
[>>]
```

## contributions

While this project is largely inactive, it will be very beneficial for someone to adopt and continue its development, with focuses oriented on
usage during CTF/wargames and/or bughunting. This can be in the form of supporting new attack vectors and modules, building support for new features
like a plugin manager, and etc.

## license

[mit](https://codemuch.tech/license.txt)
