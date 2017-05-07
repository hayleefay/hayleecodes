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
    year_1990 = float(row[4]) if row[4] != '..' else None
    year_1991 = float(row[5]) if row[5] != '..' else None
    year_1992 = float(row[6]) if row[6] != '..' else None
    year_1993 = float(row[7]) if row[7] != '..' else None
    year_1994 = float(row[8]) if row[8] != '..' else None
    year_1995 = float(row[9]) if row[9] != '..' else None
    year_1996 = float(row[10]) if row[10] != '..' else None
    year_1997 = float(row[11]) if row[11] != '..' else None
    year_1998 = float(row[12]) if row[12] != '..' else None
    year_1999 = float(row[13]) if row[13] != '..' else None
    year_2000 = float(row[14]) if row[14] != '..' else None
    year_2001 = float(row[15]) if row[15] != '..' else None
    year_2002 = float(row[16]) if row[16] != '..' else None
    year_2003 = float(row[17]) if row[17] != '..' else None
    year_2004 = float(row[18]) if row[18] != '..' else None
    year_2005 = float(row[19]) if row[19] != '..' else None
    year_2006 = float(row[20]) if row[20] != '..' else None
    year_2007 = float(row[21]) if row[21] != '..' else None
    year_2008 = float(row[22]) if row[22] != '..' else None
    year_2009 = float(row[23]) if row[23] != '..' else None
    year_2010 = float(row[24]) if row[24] != '..' else None

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
    year_1990 = float(row[4]) if row[4] != '..' else None
    year_1991 = float(row[5]) if row[5] != '..' else None
    year_1992 = float(row[6]) if row[6] != '..' else None
    year_1993 = float(row[7]) if row[7] != '..' else None
    year_1994 = float(row[8]) if row[8] != '..' else None
    year_1995 = float(row[9]) if row[9] != '..' else None
    year_1996 = float(row[10]) if row[10] != '..' else None
    year_1997 = float(row[11]) if row[11] != '..' else None
    year_1998 = float(row[12]) if row[12] != '..' else None
    year_1999 = float(row[13]) if row[13] != '..' else None
    year_2000 = float(row[14]) if row[14] != '..' else None
    year_2001 = float(row[15]) if row[15] != '..' else None
    year_2002 = float(row[16]) if row[16] != '..' else None
    year_2003 = float(row[17]) if row[17] != '..' else None
    year_2004 = float(row[18]) if row[18] != '..' else None
    year_2005 = float(row[19]) if row[19] != '..' else None
    year_2006 = float(row[20]) if row[20] != '..' else None
    year_2007 = float(row[21]) if row[21] != '..' else None
    year_2008 = float(row[22]) if row[22] != '..' else None
    year_2009 = float(row[23]) if row[23] != '..' else None
    year_2010 = float(row[24]) if row[24] != '..' else None

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
    year_1990 = float(row[4]) if row[4] != '..' else None
    year_1991 = float(row[5]) if row[5] != '..' else None
    year_1992 = float(row[6]) if row[6] != '..' else None
    year_1993 = float(row[7]) if row[7] != '..' else None
    year_1994 = float(row[8]) if row[8] != '..' else None
    year_1995 = float(row[9]) if row[9] != '..' else None
    year_1996 = float(row[10]) if row[10] != '..' else None
    year_1997 = float(row[11]) if row[11] != '..' else None
    year_1998 = float(row[12]) if row[12] != '..' else None
    year_1999 = float(row[13]) if row[13] != '..' else None
    year_2000 = float(row[14]) if row[14] != '..' else None
    year_2001 = float(row[15]) if row[15] != '..' else None
    year_2002 = float(row[16]) if row[16] != '..' else None
    year_2003 = float(row[17]) if row[17] != '..' else None
    year_2004 = float(row[18]) if row[18] != '..' else None
    year_2005 = float(row[19]) if row[19] != '..' else None
    year_2006 = float(row[20]) if row[20] != '..' else None
    year_2007 = float(row[21]) if row[21] != '..' else None
    year_2008 = float(row[22]) if row[22] != '..' else None
    year_2009 = float(row[23]) if row[23] != '..' else None
    year_2010 = float(row[24]) if row[24] != '..' else None

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
    year_1990 = float(row[4]) if row[4] != '..' else None
    year_1991 = float(row[5]) if row[5] != '..' else None
    year_1992 = float(row[6]) if row[6] != '..' else None
    year_1993 = float(row[7]) if row[7] != '..' else None
    year_1994 = float(row[8]) if row[8] != '..' else None
    year_1995 = float(row[9]) if row[9] != '..' else None
    year_1996 = float(row[10]) if row[10] != '..' else None
    year_1997 = float(row[11]) if row[11] != '..' else None
    year_1998 = float(row[12]) if row[12] != '..' else None
    year_1999 = float(row[13]) if row[13] != '..' else None
    year_2000 = float(row[14]) if row[14] != '..' else None
    year_2001 = float(row[15]) if row[15] != '..' else None
    year_2002 = float(row[16]) if row[16] != '..' else None
    year_2003 = float(row[17]) if row[17] != '..' else None
    year_2004 = float(row[18]) if row[18] != '..' else None
    year_2005 = float(row[19]) if row[19] != '..' else None
    year_2006 = float(row[20]) if row[20] != '..' else None
    year_2007 = float(row[21]) if row[21] != '..' else None
    year_2008 = float(row[22]) if row[22] != '..' else None
    year_2009 = float(row[23]) if row[23] != '..' else None
    year_2010 = float(row[24]) if row[24] != '..' else None

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
    year_1990 = float(row[4]) if row[4] != '..' else None
    year_1991 = float(row[5]) if row[5] != '..' else None
    year_1992 = float(row[6]) if row[6] != '..' else None
    year_1993 = float(row[7]) if row[7] != '..' else None
    year_1994 = float(row[8]) if row[8] != '..' else None
    year_1995 = float(row[9]) if row[9] != '..' else None
    year_1996 = float(row[10]) if row[10] != '..' else None
    year_1997 = float(row[11]) if row[11] != '..' else None
    year_1998 = float(row[12]) if row[12] != '..' else None
    year_1999 = float(row[13]) if row[13] != '..' else None
    year_2000 = float(row[14]) if row[14] != '..' else None
    year_2001 = float(row[15]) if row[15] != '..' else None
    year_2002 = float(row[16]) if row[16] != '..' else None
    year_2003 = float(row[17]) if row[17] != '..' else None
    year_2004 = float(row[18]) if row[18] != '..' else None
    year_2005 = float(row[19]) if row[19] != '..' else None
    year_2006 = float(row[20]) if row[20] != '..' else None
    year_2007 = float(row[21]) if row[21] != '..' else None
    year_2008 = float(row[22]) if row[22] != '..' else None
    year_2009 = float(row[23]) if row[23] != '..' else None
    year_2010 = float(row[24]) if row[24] != '..' else None

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
    year_1990 = float(row[4]) if row[4] != '..' else None
    year_1991 = float(row[5]) if row[5] != '..' else None
    year_1992 = float(row[6]) if row[6] != '..' else None
    year_1993 = float(row[7]) if row[7] != '..' else None
    year_1994 = float(row[8]) if row[8] != '..' else None
    year_1995 = float(row[9]) if row[9] != '..' else None
    year_1996 = float(row[10]) if row[10] != '..' else None
    year_1997 = float(row[11]) if row[11] != '..' else None
    year_1998 = float(row[12]) if row[12] != '..' else None
    year_1999 = float(row[13]) if row[13] != '..' else None
    year_2000 = float(row[14]) if row[14] != '..' else None
    year_2001 = float(row[15]) if row[15] != '..' else None
    year_2002 = float(row[16]) if row[16] != '..' else None
    year_2003 = float(row[17]) if row[17] != '..' else None
    year_2004 = float(row[18]) if row[18] != '..' else None
    year_2005 = float(row[19]) if row[19] != '..' else None
    year_2006 = float(row[20]) if row[20] != '..' else None
    year_2007 = float(row[21]) if row[21] != '..' else None
    year_2008 = float(row[22]) if row[22] != '..' else None
    year_2009 = float(row[23]) if row[23] != '..' else None
    year_2010 = float(row[24]) if row[24] != '..' else None

    q = WorkingAgeRate(countryname = countryname, countrycode = countrycode, year_1990 = year_1990, \
    year_1991 = year_1991, year_1992 = year_1992, year_1993 = year_1993, \
    year_1994 = year_1994, year_1995 = year_1995, year_1996 = year_1996, \
    year_1997 = year_1997, year_1998 = year_1998, year_1999 = year_1999, \
    year_2000 = year_2000, year_2001 = year_2001, year_2002 = year_2002, \
    year_2003 = year_2003, year_2004 = year_2004, year_2005 = year_2005, \
    year_2006 = year_2006, year_2007 = year_2007, year_2008 = year_2008, \
    year_2009 = year_2009, year_2010 = year_2000)

    q.save()
