#!/usr/bin/env bash

set -x


# environment
export AIRFLOW_HOME=${PWD}
export AIRFLOW__CORE__SQL_ALCHEMY_CONN=sqlite:///${PWD}/tests.db
export AIRFLOW__CORE__LOAD_EXAMPLES=False
export AIRFLOW__CORE__EXECUTOR=SequentialExecutor

# setup airflow db
airflow initdb

# run pytest
py.test --basetemp=${VIRTUAL_ENV} --cov=${PWD} --verbose

# clean up testing db
rm ${PWD}/tests.db
