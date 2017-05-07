# Creating a script that inputs the world bank indicators data csv into my django psqldb

import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hayleecodes.settings')
django.setup()

###

from mysite.models import FertilityRates

data = pd.read_csv('django_app/fertility.csv', low_memory=False)

for index, row in data.iterrows():
    countryname = row[0]
    countrycode = row[1]
    year_1990 = row[4]
    year_1991 = row[5]
    year_1992 = row[6]
    year_1993 = row[7]
    year_1994 = row[8]
    year_1995 = row[9]
    year_1996 = row[10]
    year_1997 = row[11]
    year_1998 = row[12]
    year_1999 = row[13]
    year_2000 = row[14]
    year_2001 = row[15]
    year_2002 = row[16]
    year_2003 = row[17]
    year_2004 = row[18]
    year_2005 = row[19]
    year_2006 = row[20]
    year_2007 = row[21]
    year_2008 = row[22]
    year_2009 = row[23]
    year_2010 = row[24]

    q = FertilityRates(countryname = countryname, countrycode = countrycode, year_1990 = year_1990, \
    year_1991 = year_1991, year_1992 = year_1992, year_1993 = year_1993, \
    year_1994 = year_1994, year_1995 = year_1995, year_1996 = year_1996, \
    year_1997 = year_1997, year_1998 = year_1998, year_1999 = year_1999, \
    year_2000 = year_2000, year_2001 = year_2001, year_2002 = year_2002, \
    year_2003 = year_2003, year_2004 = year_2004, year_2005 = year_2005, \
    year_2006 = year_2006, year_2007 = year_2007, year_2008 = year_2008, \
    year_2009 = year_2009, year_2010 = year_2000)

    q.save()

###

from mysite.models import PerWorkerGDP

data = pd.read_csv('django_app/perworkergdp.csv', low_memory=False)

for index, row in data.iterrows():
    countryname = row[0]
    countrycode = row[1]
    year_1990 = row[4]
    year_1991 = row[5]
    year_1992 = row[6]
    year_1993 = row[7]
    year_1994 = row[8]
    year_1995 = row[9]
    year_1996 = row[10]
    year_1997 = row[11]
    year_1998 = row[12]
    year_1999 = row[13]
    year_2000 = row[14]
    year_2001 = row[15]
    year_2002 = row[16]
    year_2003 = row[17]
    year_2004 = row[18]
    year_2005 = row[19]
    year_2006 = row[20]
    year_2007 = row[21]
    year_2008 = row[22]
    year_2009 = row[23]
    year_2010 = row[24]

    q = PerWorkerGDP(countryname = countryname, countrycode = countrycode, year_1990 = year_1990, \
    year_1991 = year_1991, year_1992 = year_1992, year_1993 = year_1993, \
    year_1994 = year_1994, year_1995 = year_1995, year_1996 = year_1996, \
    year_1997 = year_1997, year_1998 = year_1998, year_1999 = year_1999, \
    year_2000 = year_2000, year_2001 = year_2001, year_2002 = year_2002, \
    year_2003 = year_2003, year_2004 = year_2004, year_2005 = year_2005, \
    year_2006 = year_2006, year_2007 = year_2007, year_2008 = year_2008, \
    year_2009 = year_2009, year_2010 = year_2000)

    q.save()

###

from mysite.models import PrimaryEnrollmentRate

data = pd.read_csv('django_app/primaryenrollmentrate.csv', low_memory=False)

for index, row in data.iterrows():
    countryname = row[0]
    countrycode = row[1]
    year_1990 = row[4]
    year_1991 = row[5]
    year_1992 = row[6]
    year_1993 = row[7]
    year_1994 = row[8]
    year_1995 = row[9]
    year_1996 = row[10]
    year_1997 = row[11]
    year_1998 = row[12]
    year_1999 = row[13]
    year_2000 = row[14]
    year_2001 = row[15]
    year_2002 = row[16]
    year_2003 = row[17]
    year_2004 = row[18]
    year_2005 = row[19]
    year_2006 = row[20]
    year_2007 = row[21]
    year_2008 = row[22]
    year_2009 = row[23]
    year_2010 = row[24]

    q = PrimaryEnrollmentRate(countryname = countryname, countrycode = countrycode, year_1990 = year_1990, \
    year_1991 = year_1991, year_1992 = year_1992, year_1993 = year_1993, \
    year_1994 = year_1994, year_1995 = year_1995, year_1996 = year_1996, \
    year_1997 = year_1997, year_1998 = year_1998, year_1999 = year_1999, \
    year_2000 = year_2000, year_2001 = year_2001, year_2002 = year_2002, \
    year_2003 = year_2003, year_2004 = year_2004, year_2005 = year_2005, \
    year_2006 = year_2006, year_2007 = year_2007, year_2008 = year_2008, \
    year_2009 = year_2009, year_2010 = year_2000)

    q.save()

###

from mysite.models import LaborParticipationRate

data = pd.read_csv('django_app/laborparticipationrate.csv', low_memory=False)

for index, row in data.iterrows():
    countryname = row[0]
    countrycode = row[1]
    year_1990 = row[4]
    year_1991 = row[5]
    year_1992 = row[6]
    year_1993 = row[7]
    year_1994 = row[8]
    year_1995 = row[9]
    year_1996 = row[10]
    year_1997 = row[11]
    year_1998 = row[12]
    year_1999 = row[13]
    year_2000 = row[14]
    year_2001 = row[15]
    year_2002 = row[16]
    year_2003 = row[17]
    year_2004 = row[18]
    year_2005 = row[19]
    year_2006 = row[20]
    year_2007 = row[21]
    year_2008 = row[22]
    year_2009 = row[23]
    year_2010 = row[24]

    q = LaborParticipationRate(countryname = countryname, countrycode = countrycode, year_1990 = year_1990, \
    year_1991 = year_1991, year_1992 = year_1992, year_1993 = year_1993, \
    year_1994 = year_1994, year_1995 = year_1995, year_1996 = year_1996, \
    year_1997 = year_1997, year_1998 = year_1998, year_1999 = year_1999, \
    year_2000 = year_2000, year_2001 = year_2001, year_2002 = year_2002, \
    year_2003 = year_2003, year_2004 = year_2004, year_2005 = year_2005, \
    year_2006 = year_2006, year_2007 = year_2007, year_2008 = year_2008, \
    year_2009 = year_2009, year_2010 = year_2000)

    q.save()

###

from mysite.models import LiteracyRate

data = pd.read_csv('django_app/literacyrate.csv', low_memory=False)

for index, row in data.iterrows():
    countryname = row[0]
    countrycode = row[1]
    year_1990 = row[4]
    year_1991 = row[5]
    year_1992 = row[6]
    year_1993 = row[7]
    year_1994 = row[8]
    year_1995 = row[9]
    year_1996 = row[10]
    year_1997 = row[11]
    year_1998 = row[12]
    year_1999 = row[13]
    year_2000 = row[14]
    year_2001 = row[15]
    year_2002 = row[16]
    year_2003 = row[17]
    year_2004 = row[18]
    year_2005 = row[19]
    year_2006 = row[20]
    year_2007 = row[21]
    year_2008 = row[22]
    year_2009 = row[23]
    year_2010 = row[24]

    q = LiteracyRate(countryname = countryname, countrycode = countrycode, year_1990 = year_1990, \
    year_1991 = year_1991, year_1992 = year_1992, year_1993 = year_1993, \
    year_1994 = year_1994, year_1995 = year_1995, year_1996 = year_1996, \
    year_1997 = year_1997, year_1998 = year_1998, year_1999 = year_1999, \
    year_2000 = year_2000, year_2001 = year_2001, year_2002 = year_2002, \
    year_2003 = year_2003, year_2004 = year_2004, year_2005 = year_2005, \
    year_2006 = year_2006, year_2007 = year_2007, year_2008 = year_2008, \
    year_2009 = year_2009, year_2010 = year_2000)

    q.save()

###

from mysite.models import WorkingAgeRate

data = pd.read_csv('django_app/workingagepopulation.csv', low_memory=False)

for index, row in data.iterrows():
    countryname = row[0]
    countrycode = row[1]
    year_1990 = row[4]
    year_1991 = row[5]
    year_1992 = row[6]
    year_1993 = row[7]
    year_1994 = row[8]
    year_1995 = row[9]
    year_1996 = row[10]
    year_1997 = row[11]
    year_1998 = row[12]
    year_1999 = row[13]
    year_2000 = row[14]
    year_2001 = row[15]
    year_2002 = row[16]
    year_2003 = row[17]
    year_2004 = row[18]
    year_2005 = row[19]
    year_2006 = row[20]
    year_2007 = row[21]
    year_2008 = row[22]
    year_2009 = row[23]
    year_2010 = row[24]

    q = WorkingAgeRate(countryname = countryname, countrycode = countrycode, year_1990 = year_1990, \
    year_1991 = year_1991, year_1992 = year_1992, year_1993 = year_1993, \
    year_1994 = year_1994, year_1995 = year_1995, year_1996 = year_1996, \
    year_1997 = year_1997, year_1998 = year_1998, year_1999 = year_1999, \
    year_2000 = year_2000, year_2001 = year_2001, year_2002 = year_2002, \
    year_2003 = year_2003, year_2004 = year_2004, year_2005 = year_2005, \
    year_2006 = year_2006, year_2007 = year_2007, year_2008 = year_2008, \
    year_2009 = year_2009, year_2010 = year_2000)

    q.save()
