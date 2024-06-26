import datetime
import inspect
import sys
import shutil

class Style:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'

    RED = '\033[31m'
    BLACK = '\033[30m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GREY = '\033[37m'
    DARK_GRAY = '\033[90m'

    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'

    RESET = '\033[0m'
    SEPARATOR = '.' * 50 + '\n'


class Debug:
    verbose = True
    prefixActive = True
    blocking = True
    emojisActive = True
    separatorChar = "-"

    @staticmethod
    def _get_log_prefix(level, class_name, func_name, line_number):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        class_name_str = str(class_name)
        func_name_str = str(func_name)

        if class_name_str == "__main__" or class_name_str == "str":
            class_name_str = ""
        else:
            class_name_str += " : "

        if func_name_str == "<module>":
            func_name_str = ""
        else:
            func_name_str += "() "

        prefix = f"{Style.DIM}{Style.SEPARATOR}{level}[{current_time}] - {Style.BOLD}{class_name_str}{func_name_str}{Style.RESET}{level}{Style.DIM + Style.ITALIC}Line {line_number}:{Style.RESET}\n"
        return prefix

    @staticmethod
    def _log(message, level=Style.DARK_GRAY):
        frame = inspect.currentframe().f_back.f_back
        line_number = frame.f_lineno
        class_name = frame.f_locals.get('self', '__main__').__class__.__name__
        func_name = frame.f_code.co_name
        prefix = ""

        if Debug.prefixActive:
            prefix = Debug._get_log_prefix(level, class_name, func_name,
                                        line_number)

        print(f"{level}{prefix}{level}{message}{Style.RESET}")

    @staticmethod
    def Log(message):
        Debug._log(str(message))

    @staticmethod
    def LogWhisper(message):
        if Debug.verbose:
            Debug._log(str(message), Style.DARK_GRAY + Style.DIM + Style.ITALIC)

    @staticmethod
    def LogSuccess(message):
        if Debug.emojisActive:
            message = "|✅| " + str(message)
        Debug._log(str(message), Style.OK_GREEN)

    @staticmethod
    def LogWarning(message):
        if Debug.emojisActive:
            message = "|🟨| " + message
        Debug._log(str(message), Style.WARNING)

    @staticmethod
    def LogError(message):
        Debug.prefixActive = True
        Debug._log("|❌| " + message, Style.FAIL + Style.BOLD)
        if Debug.blocking == True:
            sys.exit()
        Debug.prefixActive = False
        
    

    @staticmethod
    def LogColor(message, style=Style.RESET):
        if isinstance(style, list):
            style = "".join(style)
        Debug._log(style + message, Style.WARNING)

    
    @staticmethod
    def LogSeparator(msg=None, style=None):
        log_length = 50

        to_print = ""

        if msg is None:
            to_print = Debug.separatorChar * log_length
        else:
            string_length = len(str(msg))
            separator_length = int((log_length - string_length) / 2)

            if string_length < log_length:
                to_print = Debug.separatorChar * separator_length + " " + str(msg) + " " + Debug.separatorChar * separator_length
            else:
                to_print = str(msg)
        
        
        while len(to_print) < log_length:
            to_print += Debug.separatorChar
        
        while len(to_print) > log_length:
            to_print = to_print[1:]
        
        prefix_active = Debug.prefixActive
        Debug.prefixActive = False
        if style == None:
            Debug._log(str(to_print), Style.BOLD + Style.PURPLE)
        else:
            Debug._log(str(to_print), style)
        
        Debug.prefixActive = prefix_active

    @staticmethod
    def LogFatSeparator(msg, style=None):
        log_length = 50
        string_length = len(str(msg))

        space_length = int((log_length - string_length) / 2)
        separator_length = log_length

        
        center = " "*space_length + str(msg) + " "*space_length

        if string_length > log_length:
            separator_length = string_length
        else:
            while len(center) < log_length:
                center += " "
            
            while len(center) > log_length:
                center = center[1:]
        
        line = Debug.separatorChar*separator_length
        
        to_print = line + "\n" + center + "\n" + line
        
        prefix_active = Debug.prefixActive
        Debug.prefixActive = False
        if style == None:
            Debug._log(str(to_print), Style.PURPLE + Style.BOLD)
        else:
            Debug._log(str(to_print), style)
        
        Debug.prefixActive = prefix_active
        
    @staticmethod
    def LogPopup(message, style=Style.GREEN):
        console_width = shutil.get_terminal_size().columns

        # Diviser le message en lignes
        lines = message.split('\n')

        # Trouver la longueur de la ligne la plus longue
        max_line_length = max(len(line) for line in lines)

        # Construire le cadre supérieur
        frame_top = "".rjust(console_width - max_line_length - 4) + "╔" + "═" * (max_line_length + 2) + "╗"

        # Construire les lignes du message
        message_lines = []
        for line in lines:
            padding = console_width - len(line) - (max_line_length - len(line)) - 4
            message_line = "".rjust(padding) + "║ " + line.center(max_line_length) + " ║"
            message_lines.append(message_line)

        # Construire le cadre inférieur
        frame_bottom = "".rjust(console_width - max_line_length - 4) + "╚" + "═" * (max_line_length + 2) + "╝"

        # Afficher la popup
        Debug.LogColor(frame_top, style)
        for line in message_lines:
            Debug.LogColor(line, style)
        Debug.LogColor(frame_bottom, style)

        print()  # Ajoute une ligne vide après la popup

__all__ = ["Style", "Debug"]
