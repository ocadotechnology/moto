from typing import Final, Optional

from moto.stepfunctions.parser.asl.component.common.flow.next import Next
from moto.stepfunctions.parser.asl.component.eval_component import EvalComponent
from moto.stepfunctions.parser.asl.component.state.choice.comparison.comparison import (
    Comparison,
)
from moto.stepfunctions.parser.asl.eval.environment import Environment


class ChoiceRule(EvalComponent):
    comparison: Final[Optional[Comparison]]
    next_stmt: Final[Optional[Next]]

    def __init__(self, comparison: Optional[Comparison], next_stmt: Optional[Next]):
        self.comparison = comparison
        self.next_stmt = next_stmt

    def _eval_body(self, env: Environment) -> None:
        self.comparison.eval(env)
