#!/usr/bin/env python

from bs4 import BeautifulSoup
import glob
import os
import sqlite3
import fnmatch

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

# tags
files = glob.glob(PATH + "doc/**/*.html")
for filename in files:
    print "Parsing: " + filename
    soup = BeautifulSoup(open(filename).read())
    sections = soup.find_all("h1")[1]
    section = sections.get_text()[:-1]

    sql = SQL_INSERT % ( section, "func", filename[len(DOCUMENTS):] + "#" + sections.a['href'].split('#')[1] )
    conn.execute(sql)
    conn.commit()

# GUIDES
files = glob.glob(PATH + "doc/*.html")
for filename in files:
    print "Parsing: " + filename
    soup = BeautifulSoup(open(filename).read())
    sections = soup.find_all("h1")[1]
    section = sections.get_text()[:-1]

    sql = SQL_INSERT % ( section, "Guide", filename[len(DOCUMENTS):] + "#" + sections.a['href'].split('#')[1] )
    conn.execute(sql)
    conn.commit()

