
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
import requests
import re;
import sqlite3 as sql
from .models import Riddle, Option
import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_graphml('IT_own_basic.graphml')
    


user = 1
con = sql.connect('test3.db', check_same_thread=False)
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `USER` (`USERID` INTEGER, `CurP` INTEGER)")
    con.commit()

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `PATH` (`POINTID` PRIMERY KEY AUTO INCREMENT,'USERID' INTEGER, `POINT` VARCHAR(5))")
    con.commit()
def insert(x):
    path = list(nx.dfs_edges(G,source =x))
    i = 0
    with con:
           cur.execute(f"INSERT INTO `PATH` VALUES ('{i}','1','{path[0][0]}')")
           con.commit()
           i = i+1
    for point in path:
        with con:
            cur.execute(f"INSERT INTO `PATH` VALUES ('{i}',1    ,'{point[1]}')")
            con.commit()
        i= i+1

def index(request):
    name = ' '
    if request.method == 'POST':
        name = request.POST['name']
        if (name == 'СУБД'):
               insert('n31')
          
   
    data = {"header": "Hello Django", "message": "Welcome to Python","name":name}
    return render(request, "index.html",context = data)
    

def second(request):
    if request.method == 'POST':
        name = request.POST['name']
    with con:    
        cur = con.cursor()    
        cur.execute("SELECT POINT FROM PATH INNER JOIN USER ON USER.USERID = PATH.USERID WHERE CurP = POINTID")
        CurPointID = cur.fetchone()[0]
        print(CurPointID)
        cur.execute("SELECT CurP FROM PATH INNER JOIN USER ON USER.USERID = PATH.USERID WHERE CurP = POINTID")
        change = cur.fetchone()[0]
        change = change + 1
        sqli = '''UPDATE USER SET CurP = {0}'''.format(change)
        cur.execute(sqli)
        
    data = {"header": CurPointID}
    return render(request, "answer.html",context = data)
