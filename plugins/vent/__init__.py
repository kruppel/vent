from airflow.plugins_manager import AirflowPlugin

from plugins.vent import operators


class VentPlugin(AirflowPlugin):

    name = "vent"
    operators = [operators.EchoOperator]
