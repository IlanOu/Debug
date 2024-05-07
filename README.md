# Debugger

Simple debugger Python to show colored text in command prompt.

## Installation

```bash
pip install git+https://github.com/IlanOu/Debug.git
```

## Examples

Import the library

```py
from debug import Debug, Style
```

### Debug

```py
Debug.Log("Hello World !")

Debug.LogError("Hello World !")
Debug.LogWarning("Hello World !")
Debug.LogSuccess("Hello World !")
Debug.LogWhisper("Hello World !")

Debug.LogColor("Hello World !", Style.RED)
```

You have parameters for the debugger :

```py
Debug.blocking = False
Debug.emojisActive = False
Debug.prefixActive = False
Debug.verbose = False
```

### Style

```py

print(Style.WARNING + "WARNING !!!" + Style.ENDC)

print(Style.BLUE + "Blue text" + Style.ENDC)

print(Style.UNDERLINE + "Underline text" + Style.ENDC)

print(Style.UNDERLINE + Style.BLUE + "Blue and underline text" + Style.ENDC)

```
