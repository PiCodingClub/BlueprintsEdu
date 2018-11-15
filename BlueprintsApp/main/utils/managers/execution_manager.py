import subprocess
import threading

from utils import logger_utils
from utils.managers.manager import Manager
from utils.managers.project_manager import ProjectManager


class ExecutionManager(Manager):
    __LOGGER = logger_utils.get_logger(__name__)

    @classmethod
    def execute_program(cls, project, main_file):
        main_path = "{}{}\\out\\{}\\{}.py".format(ProjectManager.PATH, project, project, main_file)
        app_daemon = threading.Thread(target=ExecutionManager.call_subprocess(main_path, "python"),
                                      name="{} daemon".format(project))
        app_daemon.daemon = True
        app_daemon.start()

    @classmethod
    def call_subprocess(cls, path, language):
        subprocess.Popen([language, path])
