from airflow.plugins_manager import AirflowPlugin

from vent import operators


class VentPlugin(AirflowPlugin):

    name = "vent"
    operators = [operators.EchoOperator]
