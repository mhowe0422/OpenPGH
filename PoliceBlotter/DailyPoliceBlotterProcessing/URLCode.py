#-------------------------------------------------------------------------------
# Name:       URLCode
# Purpose:
#
# Author:      Mark
#
# Created:     14/05/2014
# Copyright:   (c) Mark 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:

    con = psycopg2.connect(database='postgres',user='postgres', password='win95sux')
    cur = con.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    print ver

    #query = 'select * from "public"."URLList";'
    query = 'SELECT "lat","lng","zone","incidentdate","incidentnumber","address" FROM "PoliceBlotter".incident where zone = \'Zone 6\' order by "incidentdate", "incidentnumber"'
    #query = 'select * from "PoliceBlotter"."Neighborhood";'
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print row


except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)


finally:

    if con:
        con.close()
def main():
    pass

if __name__ == '__main__':
    main()
