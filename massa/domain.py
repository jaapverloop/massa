# -*- coding: utf-8 -*-

from sqlalchemy import (
    Column,
    Date,
    Integer,
    MetaData,
    Numeric,
    String,
    Table,
    create_engine,
)


metadata = MetaData()

measurement = Table('measurement', metadata,
    Column('id', Integer, primary_key=True),
    Column('weight', Numeric(4, 1), nullable=False),
    Column('code', String(25), nullable=False),
    Column('date_measured', Date(), nullable=False),
)

def setup(app):
    engine = create_engine(
        app.config['SQLALCHEMY_DATABASE_URI'],
        echo=app.config['SQLALCHEMY_ECHO']
    )

    metadata.bind = engine

def make_tables():
    metadata.create_all()
