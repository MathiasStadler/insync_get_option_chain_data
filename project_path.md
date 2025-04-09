## date today 

```bach
date
Tue Jan 28 04:19:03 PM CET 2025
```


## os- version

```bash
Linux debian 6.1.0-28-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.119-1 (2024-11-22) x86_64 GNU/Linux
```

# installed python version 

```bash
python3 --version
Python 3.11.2
```

# upgrade all installed packages

## -U, --upgrade               Upgrade all specified packages to the newest available version. The handling of dependencies depends on the upgrade-strategy used.

```bash
# -U, --upgrade               Upgrade all specified packages to the newest available version. The handling of dependencies depends on the upgrade-strategy used.
pip --upgrade <packages>
```

# create python venv

[install venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

```bash
python3 -m venv .venv
```

## enter .venv

```bash
source .venv//bin/activate
```

## exit/leave venv

```bash
deactivate
```

## install/upgrade  packages for these project inside .venv

> we are install both package ib_insync and ib_async

```bash
pip3 install ib_async
pip3 install --upgrade ib_async
pip3 install ib_insync
pip3 install --upgrade ib_insync
```
