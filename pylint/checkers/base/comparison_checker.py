"""Comparison checker from the basic checker."""
import astroid
from astroid import nodes
from pylint.checkers import utils
from pylint.checkers.base.basic_checker import _BasicChecker
from pylint.interfaces import HIGH
LITERAL_NODE_TYPES = (nodes.Const, nodes.Dict, nodes.List, nodes.Set)
COMPARISON_OPERATORS = frozenset(('==', '!=', '<', '>', '<=', '>='))
TYPECHECK_COMPARISON_OPERATORS = frozenset(('is', 'is not', '==', '!='))
TYPE_QNAME = 'builtins.type'

def _is_one_arg_pos_call(call: nodes.NodeNG) -> bool:
    """Is this a call with exactly 1 positional argument ?"""
    pass

class ComparisonChecker(_BasicChecker):
    """Checks for comparisons.

    - singleton comparison: 'expr == True', 'expr == False' and 'expr == None'
    - yoda condition: 'const "comp" right' where comp can be '==', '!=', '<',
      '<=', '>' or '>=', and right can be a variable, an attribute, a method or
      a function
    """
    msgs = {'C0121': ('Comparison %s should be %s', 'singleton-comparison', 'Used when an expression is compared to singleton values like True, False or None.'), 'C0123': ('Use isinstance() rather than type() for a typecheck.', 'unidiomatic-typecheck', 'The idiomatic way to perform an explicit typecheck in Python is to use isinstance(x, Y) rather than type(x) == Y, type(x) is Y. Though there are unusual situations where these give different results.', {'old_names': [('W0154', 'old-unidiomatic-typecheck')]}), 'R0123': ("In '%s', use '%s' when comparing constant literals not '%s' ('%s')", 'literal-comparison', 'Used when comparing an object to a literal, which is usually what you do not want to do, since you can compare to a different literal than what was expected altogether.'), 'R0124': ('Redundant comparison - %s', 'comparison-with-itself', 'Used when something is compared against itself.'), 'R0133': ("Comparison between constants: '%s %s %s' has a constant value", 'comparison-of-constants', "When two literals are compared with each other the result is a constant. Using the constant directly is both easier to read and more performant. Initializing 'True' and 'False' this way is not required since Python 2.3."), 'W0143': ('Comparing against a callable, did you omit the parenthesis?', 'comparison-with-callable', 'This message is emitted when pylint detects that a comparison with a callable was made, which might suggest that some parenthesis were omitted, resulting in potential unwanted behaviour.'), 'W0177': ('Comparison %s should be %s', 'nan-comparison', "Used when an expression is compared to NaN values like numpy.NaN and float('nan').")}

    def _check_singleton_comparison(self, left_value: nodes.NodeNG, right_value: nodes.NodeNG, root_node: nodes.Compare, checking_for_absence: bool=False) -> None:
        """Check if == or != is being used to compare a singleton value."""
        pass

    def _check_literal_comparison(self, literal: nodes.NodeNG, node: nodes.Compare) -> None:
        """Check if we compare to a literal, which is usually what we do not want to do."""
        pass

    def _check_logical_tautology(self, node: nodes.Compare) -> None:
        """Check if identifier is compared against itself.

        :param node: Compare node
        :Example:
        val = 786
        if val == val:  # [comparison-with-itself]
            pass
        """
        pass

    def _check_constants_comparison(self, node: nodes.Compare) -> None:
        """When two constants are being compared it is always a logical tautology."""
        pass

    def _check_type_x_is_y(self, node: nodes.Compare, left: nodes.NodeNG, operator: str, right: nodes.NodeNG) -> None:
        """Check for expressions like type(x) == Y."""
        pass