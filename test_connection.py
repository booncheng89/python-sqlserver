from connection import connection

if __name__ == "__main__":
    conn_string = r'SERVER=localhost\SQLEXPRESS;DATABASE=demo;Trusted_Connection=yes;'

    # create a table
    query1 = """
        create table city (
            [id] int,
            [name] nvarchar(50),
            [status] bit
        )
    """
    conn1 = connection(conn_string=conn_string, query=query1, params=[])
    conn1.exec_query()


    # insert some data
    query2 = """
        insert into city(id, name, status) values (1, ?, 1)
        insert into city(id, name, status) values (2, ?, 1)
        insert into city(id, name, status) values (3, ?, 1)
        insert into city(id, name, status) values (4, ?, 1)
    """
    params2 = ['Kuching', 'Sibu', 'Miri', 'Kuala Lumpur']
    conn2 = connection(conn_string=conn_string, query= query2, params=params2)
    conn2.exec_query()


    # update some data
    query3 = """
        update city set status = 0  where id = ?
    """
    params3 = [4] # set Kuala Lumpur as inactive
    conn3 = connection(conn_string=conn_string, query=query3, params=params3)
    conn3.exec_query()

    # retrieve data from city table
    query4 = """
        select * from city where status = ?
    """
    params4 = [1]
    conn4 = connection(conn_string=conn_string, query=query4, params=params4)
    cities = conn4.fetch_query()
    # loop through every row and print data
    for city in cities:
        print(city)

    # drop table
    query5 = """
        drop table city
    """
    conn5 = connection(conn_string=conn_string, query=query5, params=[])
    conn5.exec_query()
