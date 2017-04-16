import pytest

from plugins.vent.operators import EchoOperator


def test_execute_operation():
    """Test execute method of EchoOperator.
    """
    task = EchoOperator(task_id='test')
    task.execute({})
