# sqlalchemy is an abstract layer on top of SQL databases, it allows you to write Python code instead of raw SQL queries, and it will translate that into the appropriate SQL for your database
# it also provides an ORM (Object-Relational Mapping) which allows you to work with database records as if they were Python objects, which can make your code cleaner and more maintainable
# but it has a learning curve and can be overkill for simple tasks, so it's important to understand when to use it and when raw SQL might be more appropriate

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mysql+mysqlconnector://root:root123@127.0.0.1:3306/skola"
)

sql = "SELECT * FROM skoleni"
df = pd.read_sql(sql, engine)

print(df)