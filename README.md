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
# Basic
Debug.Log("Hello World !")

# Debugging
Debug.LogError("Hello World !")
Debug.LogWarning("Hello World !")
Debug.LogSuccess("Hello World !")
Debug.LogWhisper("Hello World !")

# Custom
Debug.LogColor("Hello World !", Style.RED)


# Separators
Debug.LogSeparator() 
Debug.LogSeparator("Separator") 
Debug.LogSeparator("Separator", Style.BOLD)

Debug.LogFatSeparator("Separator")  
Debug.LogFatSeparator("Separator", Style.BOLD)
```

#### You have parameters for the debugger

To enable/disable if the `Debug.LogError` is blocking

```py
Debug.blocking = False
```

To enable/disable emojis

```py
Debug.emojisActive = False
```

To enable/disable the prefix

```py
Debug.prefixActive = False
```

To enable/disable all `Debug.LogWhisper`

```py
Debug.verbose = False
```

### Style

The Style can be used in some Debug methods (ex: `Debug.LogColor("Hello", Style.RED)`).

```py

print(Style.WARNING + "WARNING !!!" + Style.ENDC)

print(Style.BLUE + "Blue text" + Style.ENDC)

print(Style.UNDERLINE + "Underline text" + Style.ENDC)

print(Style.UNDERLINE + Style.BLUE + "Blue and underline text" + Style.ENDC)

```
