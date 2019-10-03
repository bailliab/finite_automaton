"""A class for Finite State automation"""
import attr
from automata.fa.dfa import DFA


@attr.s
class FiniteState(object):
    """Using the Automata library for Finate State"""
    state = attr.ib(default={"S0", "S1", "S2"})
    input_symbols = attr.ib(default={"0", "1"})
    transitions = attr.ib(default={
        "S0": {"0": "S0", "1": "S1"},
        "S1": {"0": "S2", "1": "S0"},
        "S2": {"0": "S1", "1": "S2"},
        })
    initial_state = attr.ib(default="S0")
    final_states = attr.ib(default={"S0", "S1", "S2"})
    dfa = attr.ib(default=None)

    def __attrs_post_init__(self):
        """Initialization by creating the default object"""
        if self.dfa is None:
            self.dfa = DFA(
                states=self.state,
                input_symbols=self.input_symbols,
                transitions=self.transitions,
                initial_state=self.initial_state,
                final_states=self.final_states,
            )

    def get_final_value(self, input_string):
        """Returns the final value, rasies RejectionException if a problem is found"""
        value = self.dfa.read_input(input_string)[1:]
        return value

    def get_final_state(self, input_string):
        """Returns the final state, rasies RejectionException if a problem is found"""
        value = self.dfa.read_input(input_string)[:1]
        return value
