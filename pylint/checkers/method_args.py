"""Variables checkers for Python code."""
from __future__ import annotations
from typing import TYPE_CHECKING
import astroid
from astroid import arguments, bases, nodes
from pylint.checkers import BaseChecker, utils
from pylint.interfaces import INFERENCE
if TYPE_CHECKING:
    from pylint.lint import PyLinter

class MethodArgsChecker(BaseChecker):
    """BaseChecker for method_args.

    Checks for
    * missing-timeout
    * positional-only-arguments-expected
    """
    name = 'method_args'
    msgs = {'W3101': ("Missing timeout argument for method '%s' can cause your program to hang indefinitely", 'missing-timeout', "Used when a method needs a 'timeout' parameter in order to avoid waiting for a long time. If no timeout is specified explicitly the default value is used. For example for 'requests' the program will never time out (i.e. hang indefinitely)."), 'E3102': ('`%s()` got some positional-only arguments passed as keyword arguments: %s', 'positional-only-arguments-expected', 'Emitted when positional-only arguments have been passed as keyword arguments. Remove the keywords for the affected arguments in the function call.', {'minversion': (3, 8)})}
    options = (('timeout-methods', {'default': ('requests.api.delete', 'requests.api.get', 'requests.api.head', 'requests.api.options', 'requests.api.patch', 'requests.api.post', 'requests.api.put', 'requests.api.request'), 'type': 'csv', 'metavar': '<comma separated list>', 'help': "List of qualified names (i.e., library.method) which require a timeout parameter e.g. 'requests.api.get,requests.api.post'"}),)

    def _check_missing_timeout(self, node: nodes.Call) -> None:
        """Check if the call needs a timeout parameter based on package.func_name
        configured in config.timeout_methods.

        Package uses inferred node in order to know the package imported.
        """
        pass

    def _check_positional_only_arguments_expected(self, node: nodes.Call) -> None:
        """Check if positional only arguments have been passed as keyword arguments by
        inspecting its method definition.
        """
        pass