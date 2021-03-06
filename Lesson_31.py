"""Текст задания.

Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе 
Чикаго с 2001 года по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Пример данных:
ID,Case Number,Date,Block,IUCR,Primary Type,Description,Location Description,Arrest,Domestic,Beat,District,Ward,Community Area,FBI Code
2383135,HH684629,10/01/2002 12:47:08 PM,032XX W ROOSEVELT RD,0860,THEFT,RETAIL THEFT,GROCERY FOOD STORE,true,false,1134,011,24,29,06
2383437,HH693227,09/04/2002 09:30:00 PM,048XX W ARMITAGE AVE,0486,BATTERY,DOMESTIC BATTERY SIMPLE,TAVERN/LIQUOR STORE,false,true,2522,025,31,19,08B
2383482,HH692935,10/04/2002 10:09:09 PM,116XX S MICHIGAN AVE,1330,CRIMINAL TRESPASS,TO LAND,GAS STATION,true,false,0532,005,9,53,26
2383568,HH690681,10/03/2002 05:00:00 AM,017XX W TOUHY AVE,0610,BURGLARY,FORCIBLE ENTRY,APARTMENT,false,false,2423,024,49,1,05
2457967,HH706178,10/11/2002 12:28:49 AM,023XX E 79TH ST,0486,BATTERY,DOMESTIC BATTERY SIMPLE,STREET,false,false,0414,004,7,43,08B
2383599,HH692261,10/04/2002 10:00:00 AM,019XX W CULLOM AVE,0610,BURGLARY,FORCIBLE ENTRY,RESIDENCE,false,false,1922,019,47,5,05
2458153,HH780784,11/13/2002 07:15:00 AM,042XX S PRAIRIE AVE,0910,MOTOR VEHICLE THEFT,AUTOMOBILE,STREET,false,false,0214,002,3,38,07
2383787,HH690948,10/04/2002 06:05:50 AM,031XX W DOUGLAS BLVD,1310,CRIMINAL DAMAGE,TO PROPERTY,RESIDENCE,false,false,1022,010,24,29,14
2459070,HH787097,11/18/2002 11:30:00 AM,031XX W 38TH ST,0910,MOTOR VEHICLE THEFT,AUTOMOBILE,STREET,false,false,0913,009,12,58,07
2384629,HH686645,10/02/2002 09:10:00 AM,015XX E 71ST PL,0486,BATTERY,DOMESTIC BATTERY SIMPLE,STREET,false,true,0324,003,5,43,08B
2384758,HH694553,10/05/2002 11:30:00 AM,027XX N GREENVIEW AVE,0610,BURGLARY,FORCIBLE ENTRY,RESIDENCE,false,false,1931,019,32,7,05
10018869,HY208015,04/02/2015 05:30:00 PM,070XX S EGGLESTON AVE,0486,BATTERY,DOMESTIC BATTERY SIMPLE,SIDEWALK,false,true,0732,007,6,68,08B
10018946,HY208089,04/02/2015 05:50:00 PM,073XX N ROGERS AVE,0460,BATTERY,SIMPLE,PARK PROPERTY,false,false,2424,024,49,1,08B
10019044,HY208316,04/02/2015 08:25:00 PM,039XX W GRENSHAW ST,1811,NARCOTICS,POSS: CANNABIS 30GMS OR LESS,SIDEWALK,true,false,1132,011,24,29,18
10019056,HY208307,04/02/2015 09:00:00 AM,114XX S WATKINS AVE,0620,BURGLARY,UNLAWFUL ENTRY,RESIDENCE,false,false,2234,022,34,75,05
10019071,HY207977,04/02/2015 05:15:00 PM,045XX N MARMORA AVE,0560,ASSAULT,SIMPLE,ALLEY,false,false,1622,016,38,15,08A
10019194,HY208464,04/03/2015 12:33:00 AM,030XX W POPE JOHN PAUL II DR,0486,BATTERY,DOMESTIC BATTERY SIMPLE,RESIDENCE,true,true,0921,009,14,58,08B
10019307,HY207737,03/24/2015 03:46:00 AM,030XX W 36TH PL,0935,MOTOR VEHICLE THEFT,"THEFT/RECOVERY: TRUCK,BUS,MHOME",STREET,false,false,0911,009,12,58,07
10019656,HY208666,04/02/2015 09:00:00 PM,013XX W 68TH ST,1320,CRIMINAL DAMAGE,TO VEHICLE,STREET,false,false,0724,007,17,67,14
10019780,HY208917,12/13/2010 10:00:00 AM,078XX S INGLESIDE AVE,1153,DECEPTIVE PRACTICE,FINANCIAL IDENTITY THEFT OVER $ 300,RESIDENCE,false,false,0624,006,8,69,11
10019858,HY208976,04/03/2015 11:00:00 AM,011XX W MADISON ST,1210,DECEPTIVE PRACTICE,THEFT OF LABOR/SERVICES,MEDICAL/DENTAL OFFICE,true,false,1232,012,2,28,11
10020263,HY209577,04/03/2015 09:27:00 PM,061XX S WESTERN AVE,4625,OTHER OFFENSE,PAROLE VIOLATION,ALLEY,true,false,0825,008,15,66,26
10020740,HY210022,04/04/2015 11:10:00 AM,002XX N KOLMAR AVE,0486,BATTERY,DOMESTIC BATTERY SIMPLE,RESIDENCE,true,true,1113,011,28,26,08B

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import csv
import os

FILE_IN = os.path.join("C:\\", "Documents", "Crimes.csv")
dict_primary_types = {}
list_count = []

with open(FILE_IN, 'r') as f_in:
    reader = csv.reader(f_in)
    for line in reader:
        if '2015' in line[2]:
            if line[5] in dict_primary_types:
                dict_primary_types[line[5]] += 1
            else:
                dict_primary_types[line[5]] = 1

for key in dict_primary_types:
    list_count += [dict_primary_types[key]]

for key in dict_primary_types:
    if dict_primary_types[key] == max(list_count):
        print(key)
