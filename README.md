JadeBot
====
A modular bot designed to work with hierarchial platforms.

Requirements
---
#

This project requires **python 3.3 or higher**.

Running
----
#

To run Jadebot, you need a provider module in the **providers** module. The configuration for the each provider must be at **config/*provider_module_name***, and any modules configured in this configuration need to be in the **modules** module.

### Linux/MacOS
```
python3 -m jadebot [provider module name]
```

### Windows
```
py -3 -m jadebot [provider module name]
```
