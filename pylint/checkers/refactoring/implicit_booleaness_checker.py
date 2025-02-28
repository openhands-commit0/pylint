from __future__ import annotations
import itertools
import astroid
from astroid import bases, nodes, util
from pylint import checkers
from pylint.checkers import utils
from pylint.interfaces import HIGH, INFERENCE

class ImplicitBooleanessChecker(checkers.BaseChecker):
    """Checks for incorrect usage of comparisons or len() inside conditions.

    Incorrect usage of len()
    Pep8 states:
    For sequences, (strings, lists, tuples), use the fact that empty sequences are false.

        Yes: if not seq:
             if seq:

        No: if len(seq):
            if not len(seq):

    Problems detected:
    * if len(sequence):
    * if not len(sequence):
    * elif len(sequence):
    * elif not len(sequence):
    * while len(sequence):
    * while not len(sequence):
    * assert len(sequence):
    * assert not len(sequence):
    * bool(len(sequence))

    Incorrect usage of empty literal sequences; (), [], {},

    For empty sequences, (dicts, lists, tuples), use the fact that empty sequences are false.

        Yes: if variable:
             if not variable

        No: if variable == empty_literal:
            if variable != empty_literal:

    Problems detected:
    * comparison such as variable == empty_literal:
    * comparison such as variable != empty_literal:
    """
    name = 'refactoring'
    msgs = {'C1802': ('Do not use `len(SEQUENCE)` without comparison to determine if a sequence is empty', 'use-implicit-booleaness-not-len', "Empty sequences are considered false in a boolean context. You can either remove the call to 'len' (``if not x``) or compare the length against a scalar (``if len(x) > 1``).", {'old_names': [('C1801', 'len-as-condition')]}), 'C1803': ('"%s" can be simplified to "%s", if it is strictly a sequence, as an empty %s is falsey', 'use-implicit-booleaness-not-comparison', 'Empty sequences are considered false in a boolean context. Following this check blindly in weakly typed code base can create hard to debug issues. If the value can be something else that is falsey but not a sequence (for example ``None``, an empty string, or ``0``) the code will not be equivalent.'), 'C1804': ('"%s" can be simplified to "%s", if it is striclty a string, as an empty string is falsey', 'use-implicit-booleaness-not-comparison-to-string', 'Empty string are considered false in a boolean context. Following this check blindly in weakly typed code base can create hard to debug issues. If the value can be something else that is falsey but not a string (for example ``None``, an empty sequence, or ``0``) the code will not be equivalent.', {'default_enabled': False, 'old_names': [('C1901', 'compare-to-empty-string')]}), 'C1805': ('"%s" can be simplified to "%s", if it is strictly an int, as 0 is falsey', 'use-implicit-booleaness-not-comparison-to-zero', '0 is considered false in a boolean context. Following this check blindly in weakly typed code base can create hard to debug issues. If the value can be something else that is falsey but not an int (for example ``None``, an empty string, or an empty sequence) the code will not be equivalent.', {'default_enabled': False, 'old_names': [('C2001', 'compare-to-zero')]})}
    options = ()
    _operators = {'!=', '==', 'is not', 'is'}

    @utils.only_required_for_messages('use-implicit-booleaness-not-len')
    def visit_unaryop(self, node: nodes.UnaryOp) -> None:
        """`not len(S)` must become `not S` regardless if the parent block is a test
        condition or something else (boolean expression) e.g. `if not len(S):`.
        """
        pass

    def _check_use_implicit_booleaness_not_comparison(self, node: nodes.Compare) -> None:
        """Check for left side and right side of the node for empty literals."""
        pass

    def _implicit_booleaness_message_args(self, literal_node: nodes.NodeNG, operator: str, target_node: nodes.NodeNG) -> tuple[str, str, str]:
        """Helper to get the right message for "use-implicit-booleaness-not-comparison"."""
        pass

    @staticmethod
    def base_names_of_instance(node: util.UninferableBase | bases.Instance) -> list[str]:
        """Return all names inherited by a class instance or those returned by a
        function.

        The inherited names include 'object'.
        """
        pass