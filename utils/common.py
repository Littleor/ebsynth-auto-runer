import logging
import os

from rich.console import Console
from rich.logging import RichHandler


def logging_config(level=logging.INFO):
    console = Console()

    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(console=console, rich_tracebacks=True)]
    )


def close_ebsynth(software_path=None) -> bool:
    """
    close ebsynth
    :param software_path:
    :return:
    """
    # TODO Need support for windows
    app_name = "EbSynth" if software_path is None else software_path
    os.system(f"killall {app_name}")
