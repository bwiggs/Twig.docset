#!/usr/bin/env python

from bs4 import BeautifulSoup
import glob
import sqlite3

RESOURCES = "Contents/Resources/"
DOCUMENTS = RESOURCES + "Documents/"
PATH = DOCUMENTS + "twig.sensiolabs.org/"

SQL_INSERT = "INSERT INTO searchindex VALUES ( NULL, '%s', '%s', '%s')"

conn = sqlite3.connect('Contents/Resources/docSet.dsidx')

# DROP table
print "Dropping searchIndex"
conn.execute("drop table if exists searchIndex")

# CREATE table
print "Creating searchIndex"
conn.execute("create table if not exists searchIndex (id integer PRIMARY KEY AUTOINCREMENT, name string, type string, path string)")
conn.commit()

# filters
files = [f for f in glob.glob(PATH + "doc/filters/*.html") if "index.html" not in f]
for filename in files:
    print "Parsing: " + filename
    soup = BeautifulSoup(open(filename).read())
    sections = soup.find_all("h1")[1]
    section = sections.get_text()[:-1]

    sql = SQL_INSERT % ( "Filter::" + section, "Function", filename[len(DOCUMENTS):] + "#" + sections.a['href'].split('#')[1] )
    conn.execute(sql)
    conn.commit()

# functions
files = [f for f in glob.glob(PATH + "doc/functions/*.html") if "index.html" not in f]
for filename in files:
    print "Parsing: " + filename
    soup = BeautifulSoup(open(filename).read())
    sections = soup.find_all("h1")[1]
    section = sections.get_text()[:-1]

    sql = SQL_INSERT % ( "Function::" + section, "Function", filename[len(DOCUMENTS):] + "#" + sections.a['href'].split('#')[1] )
    conn.execute(sql)
    conn.commit()

# tags
files = [f for f in glob.glob(PATH + "doc/tags/*.html") if "index.html" not in f]
for filename in files:
    print "Parsing: " + filename
    soup = BeautifulSoup(open(filename).read())
    sections = soup.find_all("h1")[1]
    section = sections.get_text()[:-1]

    sql = SQL_INSERT % ( section, "Tag", filename[len(DOCUMENTS):] + "#" + sections.a['href'].split('#')[1] )
    conn.execute(sql)
    conn.commit()

# extensions
files = [f for f in glob.glob(PATH + "doc/extensions/*.html") if "index.html" not in f]
for filename in files:
    print "Parsing: " + filename
    soup = BeautifulSoup(open(filename).read())
    sections = soup.find_all("h1")[1]
    section = sections.get_text()[:-1]

    sql = SQL_INSERT % ( section, "Module", filename[len(DOCUMENTS):] + "#" + sections.a['href'].split('#')[1] )
    conn.execute(sql)
    conn.commit()

# tests
files = [f for f in glob.glob(PATH + "doc/tests/*.html") if "index.html" not in f]
for filename in files:
    print "Parsing: " + filename
    soup = BeautifulSoup(open(filename).read())
    sections = soup.find_all("h1")[1]
    section = sections.get_text()[:-1]

    sql = SQL_INSERT % ( section, "Operator", filename[len(DOCUMENTS):] + "#" + sections.a['href'].split('#')[1] )
    conn.execute(sql)
    conn.commit()

# GUIDES
files = [f for f in glob.glob(PATH + "doc/*.html") if "index.html" not in f]
for filename in files:
    print "Parsing: " + filename
    soup = BeautifulSoup(open(filename).read())
    sections = soup.find_all("h1")[1]
    section = sections.get_text()[:-1]

    sql = SQL_INSERT % ( section, "Guide", filename[len(DOCUMENTS):] + "#" + sections.a['href'].split('#')[1] )
    conn.execute(sql)
    conn.commit()

