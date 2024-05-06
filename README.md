# Debugger

Simple debugger Python pour afficher du texte dans la console.

## Comment l'installer ?

```bash
pip install git+https://github.com/IlanOu/Debug.git
```

## Exemples

### Debug

```py
Debug.Log("Hello World !")

Debug.LogError("Hello World !")
Debug.LogWarning("Hello World !")
Debug.LogSuccess("Hello World !")
Debug.LogWhisper("Hello World !")

Debug.LogColor("Hello World !", Style.RED)
```

### Style

```py

print(Style.WARNING + "WARNING !!!" + Style.ENDC)

print(Style.BLUE + "Blue text" + Style.ENDC)

print(Style.UNDERLINE + "Underline text" + Style.ENDC)

print(Style.UNDERLINE + Style.BLUE + "Blue and underline text" + Style.ENDC)

```
