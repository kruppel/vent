import logging

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class EchoOperator(BaseOperator):

    ui_color = '#1EB9E4'
    ui_fgcolor = '#FFFFFF'

    @apply_defaults
    def __init__(self, message='whoosh', *args, **kwargs):
        super(EchoOperator, self).__init__(*args, **kwargs)
        self.message = message

    def execute(self, context):
        logging.info('[ECHOES] {0}'.format(self.message))
