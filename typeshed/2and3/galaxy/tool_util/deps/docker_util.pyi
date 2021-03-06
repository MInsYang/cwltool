# Stubs for galaxy.tools.deps.docker_util (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .commands import argv_to_str as argv_to_str

DEFAULT_DOCKER_COMMAND = ...  # type: str
DEFAULT_SUDO = ...  # type: bool
DEFAULT_SUDO_COMMAND = ...  # type: str
DEFAULT_HOST = ...  # type: Any
DEFAULT_VOLUME_MOUNT_TYPE = ...  # type: str
DEFAULT_WORKING_DIRECTORY = ...  # type: Any
DEFAULT_NET = ...  # type: Any
DEFAULT_MEMORY = ...  # type: Any
DEFAULT_VOLUMES_FROM = ...  # type: Any
DEFAULT_AUTO_REMOVE = ...  # type: bool
DEFAULT_SET_USER = ...  # type: str
DEFAULT_RUN_EXTRA_ARGUMENTS = ...  # type: Any

class DockerVolume:
    from_path = ...  # type: Any
    to_path = ...  # type: Any
    how = ...  # type: Any
    def __init__(self, path, to_path: Optional[Any] = ..., how: Any = ...) -> None: ...
    @staticmethod
    def volumes_from_str(volumes_as_str): ...
    @staticmethod
    def volume_from_str(as_str): ...

def kill_command(container, signal: Optional[Any] = ..., **kwds): ...
def logs_command(container, **kwds): ...
def build_command(image, docker_build_path, **kwds): ...
def build_save_image_command(image, destination, **kwds): ...
def build_pull_command(tag, **kwds): ...
def build_docker_cache_command(image, **kwds): ...
def build_docker_images_command(truncate: bool = ..., **kwds): ...
def build_docker_load_command(**kwds): ...
def build_docker_run_command(container_command, image, interactive: bool = ..., terminal: bool = ..., tag: Optional[Any] = ..., volumes: Any = ..., volumes_from: Any = ..., memory: Any = ..., env_directives: Any = ..., working_directory: Any = ..., name: Optional[Any] = ..., net: Any = ..., run_extra_arguments: Any = ..., docker_cmd: Any = ..., sudo: Any = ..., sudo_cmd: Any = ..., auto_rm: Any = ..., set_user: Any = ..., host: Any = ...): ...
def command_list(command, command_args: Any = ..., **kwds): ...
def command_shell(command, command_args: Any = ..., **kwds): ...
