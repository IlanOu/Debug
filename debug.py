from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.text import Text
from rich import box
import datetime
import inspect
import sys
import time
from enum import Enum, auto

console = Console()

class LogLevel(Enum):
    INFO = auto()
    SUCCESS = auto()
    WARNING = auto()
    ERROR = auto()
    WHISPER = auto()

class Debug:
    verbose = True
    prefixActive = True
    blocking = True
    emojisActive = True
    separatorChar = "-"

    @staticmethod
    def _get_log_prefix(class_name, func_name, line_number):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        class_name_str = f"{class_name}: " if class_name != "__main__" else ""
        func_name_str = f"{func_name}() " if func_name != "<module>" else ""
        return f"[{current_time}] {class_name_str}{func_name_str} Line {line_number}:"

    @staticmethod
    def _get_level_style(level: LogLevel):
        if level == LogLevel.SUCCESS:
            return "green"
        elif level == LogLevel.WARNING:
            return "yellow"
        elif level == LogLevel.ERROR:
            return "bold red"
        elif level == LogLevel.WHISPER:
            return "dim italic"
        else:
            return ""  # Default color

    @staticmethod
    def _get_level_emoji(level: LogLevel):
        if level == LogLevel.SUCCESS:
            return "✅"
        elif level == LogLevel.WARNING:
            return "🚧"
        elif level == LogLevel.ERROR:
            return "❌"
        else:
            return ""

    @staticmethod
    def _log(message, level: LogLevel = LogLevel.INFO, color=None):
        frame = inspect.currentframe().f_back.f_back.f_back
        line_number = frame.f_lineno
        class_name = frame.f_locals.get('self', '__main__').__class__.__name__
        func_name = frame.f_code.co_name
        prefix = ""

        if Debug.prefixActive:
            prefix = Debug._get_log_prefix(class_name, func_name, line_number)

        if color is None:
            color = Debug._get_level_style(level)
        
        message = f"[{color}]{message}[/{color}]"

        console.print(f"{prefix} {message}")

    @staticmethod
    def _logger(message, level: LogLevel = LogLevel.INFO, emoji=None, color=None):
        if emoji is None:
            emoji = Debug._get_level_emoji(level)
        if emoji:
            message = f"{emoji} {message}"
        
        def __log(message, level, color):
            Debug._log(message, level, color)

        try:
            inspect.currentframe().f_back
            Debug._log(message, level, color)
        except:
            __log(message, level, color)
    
    @staticmethod
    def BOG(message):
        Debug._logger(message, level=LogLevel.INFO)
        
    @staticmethod
    def LogSuccess(message):
        Debug._logger(message, level=LogLevel.SUCCESS)

    @staticmethod
    def LogWarning(message):
        Debug._logger(message, level=LogLevel.WARNING)

    @staticmethod
    def LogError(message):
        Debug._logger(message, level=LogLevel.ERROR)
        if Debug.blocking:
            sys.exit()

    @staticmethod
    def LogWhisper(message):
        if Debug.verbose:
            Debug._logger(message, level=LogLevel.WHISPER)

    @staticmethod
    def LogSeparator(msg=None, border_style="white", text_style="white"):
        if msg:
            console.rule(Text(msg, style=text_style), style=border_style)
        else:
            console.rule(style=border_style)

    @staticmethod
    def LogPanel(message, title="Info", border_style=None, level: LogLevel = LogLevel.INFO):
        style = Debug._get_level_style(level)
        if border_style == None:
            border_style = style
        console.print(Panel(Text(message, style=style), title=title, border_style=border_style, box=box.ROUNDED))

    @staticmethod
    def LogCard(message, separator="|", style=None, title="Info", level: LogLevel = LogLevel.INFO):
        """
        Affiche un message formaté en colonnes sous forme de carte encadrée.
        Le nombre de colonnes est déterminé par le nombre de séparateurs sur chaque ligne.

        Args:
            message (str): Le message à afficher.
            separator (str): Le caractère séparateur des colonnes (par défaut "|").
            style (str): Le style de couleur Rich pour l'affichage (par défaut "cyan").
            title (str): Le titre de la carte (par défaut "Info").
            level (LogLevel): Le niveau de log pour le style du message (par défaut INFO).
        """
        lines = message.split("\n")
        column_lengths = []

        # Calculer la largeur maximale de chaque colonne
        for line in lines:
            columns = line.split(separator)
            for i, col in enumerate(columns):
                if i >= len(column_lengths):
                    column_lengths.append(0)
                column_lengths[i] = max(column_lengths[i], len(col.strip()))

        # Formater les lignes avec un alignement centré pour chaque colonne
        output_lines = []
        for line in lines:
            columns = line.split(separator)
            formatted_columns = [col.strip().center(column_lengths[i]) for i, col in enumerate(columns)]
            formatted_line = f" {separator} ".join(formatted_columns)
            output_lines.append(formatted_line)

        # Créer une carte avec Rich Panel
        level_style = Debug._get_level_style(level)
        if style == None:
            style = level_style
        card_content = Text("\n".join(output_lines), style=level_style)
        console.print(Panel(card_content, title=title, border_style=style, expand=False))


    @staticmethod
    def LogColumns(message, separator="|", style="cyan", level: LogLevel = LogLevel.INFO):
        """
        Affiche un message avec plusieurs colonnes. Le nombre de colonnes est déterminé par le nombre de séparateurs sur chaque ligne.

        Args:
            message (str): Le message à afficher.
            separator (str): Le caractère séparateur des colonnes (par défaut "|").
            style (str): Le style de couleur Rich pour l'affichage (par défaut "cyan").
            level (LogLevel): Le niveau de log pour le style du message (par défaut INFO).
        """
        lines = message.split("\n")
        column_lengths = []

        # Calculer la largeur maximale de chaque colonne
        for line in lines:
            columns = line.split(separator)
            for i, col in enumerate(columns):
                if i >= len(column_lengths):
                    column_lengths.append(0)
                column_lengths[i] = max(column_lengths[i], len(col.strip()))

        # Formater les lignes avec un alignement centré pour chaque colonne
        output_lines = []
        for line in lines:
            columns = line.split(separator)
            formatted_columns = [col.strip().center(column_lengths[i]) for i, col in enumerate(columns)]
            formatted_line = f" {separator} ".join(formatted_columns)
            output_lines.append(formatted_line)

        # Afficher le résultat avec Rich
        level_style = Debug._get_level_style(level)
        console.print("\n".join(output_lines), style=level_style)

    @staticmethod
    def show_progress(task_name, total):
        with Progress() as progress:
            task = progress.add_task(f"[green]{task_name}[/green]", total=total)
            for _ in range(total):
                progress.update(task, advance=1)
                time.sleep(0.1)

__all__ = ["LogLevel", "Debug"]
