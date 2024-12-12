import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://mohammad:fallatah2003@@tasktracker.postgres.database.azure.com:5432/postgres?sslmode=require"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
