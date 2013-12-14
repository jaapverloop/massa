# -*- coding: utf-8 -*-

from sqlalchemy import (
    Column,
    Date,
    Integer,
    MetaData,
    Numeric,
    String,
    Table,
)


metadata = MetaData()

measurement = Table('measurement', metadata,
    Column('id', Integer, primary_key=True),
    Column('weight', Numeric(4, 1), nullable=False),
    Column('code', String(25), nullable=False),
    Column('date_measured', Date(), nullable=False),
)
