import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="aircraft_db",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Aircraft CASCADE;')
cur.execute('DROP TABLE IF EXISTS Casualties CASCADE;')
cur.execute('DROP TABLE IF EXISTS Incidents CASCADE;')

cur.execute('CREATE TABLE Aircraft(aircraft_reg_number varchar(255),'
            'event_ntsb_number varchar(255),'
            'aircraft_make varchar(255),'
            'aircraft_model varchar(255),'
            'PRIMARY KEY (aircraft_reg_number));'
            )

cur.execute('CREATE TABLE Casualties(casualty_id varchar(255),'
            'event_ntsb_number varchar(255),'
            'first_name varchar(255),'
            'last_name varchar(255),'
            'dob varchar(255),'
            'age int,'
            'sex varchar(20),'
            'PRIMARY KEY (casualty_id));'
            )

cur.execute('CREATE TABLE Incidents(event_ntsb_number varchar(255),'
            'aircraft_reg_number varchar(255),'
            'event_severity varchar(255),'
            'event_date varchar(255),'
            'event_location varchar(255),'
            'event_state varchar(255),'
            'PRIMARY KEY (event_ntsb_number),'
            'FOREIGN KEY (aircraft_reg_number) REFERENCES Aircraft(aircraft_reg_number));'
            )

cur.execute('ALTER TABLE Casualties ADD FOREIGN KEY (event_ntsb_number) REFERENCES Incidents(event_ntsb_number);')

cur.execute('ALTER TABLE Aircraft ADD FOREIGN KEY (event_ntsb_number) REFERENCES Incidents(event_ntsb_number);')

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('vo0647',
             'Airbus',
             'A234')
            )

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('tr4824',
             'Ferrari',
             'B52')
            )

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('fb3513',
             'Honeywell',
             'D339')
            )

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('gd4294',
             'Honeywell',
             'D019')
            )

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('oa8766',
             'Honeywell',
             'D339')
            )

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('ux8920',
             'Sus',
             'D339')
            )

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('cm4946',
             'Ford',
             'B52')
            )

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('au4275',
             'Sus',
             'ID232')
            )

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('de9625',
             'Boeing',
             'D019')
            )

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('jd1143',
             'Sus',
             'D019')
            )

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('kh6269',
             'Honeywell',
             'D019')
            )

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('sp6303',
             'Honeywell',
             'A234')
            )

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('ii5207',
             'Ferrari',
             'ID232')
            )
            
cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('uj7834',
             'Airbus',
             'A234')
            )          
                  
cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('he6251',
             'Sus',
             'D019')
            )       
                           
cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('qa7530',
             'Airbus',
             'D019')
            )  
       
cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('zr5082',
             'Airbus',
             'D019')
            )  

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('ps3752',
             'Honeywell',
             'ID232')
            )  

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('ta7671',
             'Airbus',
             'D019')
            ) 

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('ae0784',
             'Honeywell',
             'B52')
            )  

cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('vo0647',
             'zhw20jc816',
             '4 June 1996',
             'Severe',
             'Helena', 
             'North Carolina')
            ) 

cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('tr4824',
             'tyk34sx279',
             '4 June 1989',
             'Severe',
             'Denver', 
             'Alaska')
            ) 

cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('fb3513',
             'gof12ih190',
             '19 October 1960',
             'Minor',
             'Jackson', 
             'New Hampshire')
            ) 

cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('gd4294',
             'ous85wn249',
             '1 February 2003',
             'Damaging',
             'Concord', 
             'Indiana')
            ) 

cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('oa8766',
             'nek92od060',
             '5 September 1986',
             'Damaging',
             'Jefferson City', 
             'North Carolina')
            ) 

cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('ux8920',
             'guq98px044',
             '26 April 2002',
             'Damaging',
             'Atlanta', 
             'Montana')
            ) 
            
cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('cm4946',
             'ykq09is184',
             '12 December 1980',
             'Damaging',
             'Honolulu', 
             'North Dakota')
            )          
            
cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('au4275',
             'fat60sj562',
             '1 April 2016',
             'Mild',
             'Little Rock', 
             'Nevada')
            )

cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('de9625',
             'iys45xm229',
             '11 November 2009',
             'Mild',
             'Olympia', 
             'Illinois')
            )

cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('jd1143',
             'tia75mc421',
             '19 February 2013',
             'Damaging',
             'Nashville', 
             'Pennsylvania')
            )
            
cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('kh6269',
             'llb18lx345',
             '16 August 1966',
             'Minor',
             'Providence', 
             'Alaska')
            )            
            
cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('sp6303',
             'zsx48hj408',
             '5 February 1994',
             'Catastrophic',
             'Bismarck', 
             'Tennessee')
            ) 

cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('ii5207',
             'ukz02is226',
             '6 December 1960',
             'Catastrophic',
             'Richmond', 
             'Oregon')
            ) 

cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('uj7834',
             'ntj91ib412',
             '9 March 1991',
             'Minor',
             'Helena', 
             'South Carolina')
            )

cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('he6251',
             'mhn03km027',
             '16 June 1992',
             'Severe',
             'Annapolis', 
             'California')
            )

cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('qa7530',
             'wmx92ag739',
             '23 June 1999',
             'Catastrophic',
             'Dover', 
             'Ohio')
            )    
            
cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('zr5082',
             'lsb53zp487',
             '15 December 1980',
             'Damaging',
             'Baton Rouge', 
             'Michigan')
            )

cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('ps3752',
             'rkf74bg521',
             '24 April 1986',
             'Catastrophic',
             'Nashville', 
             'Colorado')
            )            
            
cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('ta7671',
             'ppn08fj507',
             '1 May 2004',
             'Minor',
             'Boise', 
             'Missouri')
            )              
            
cur.execute('INSERT INTO Incidents(aircraft_reg_number, event_ntsb_number, event_date, event_severity, event_location, event_state ) '
            'VALUES(%s,%s,%s,%s,%s,%s)',
            ('ae0784',
             'jii02dr566',
             '13 October 1987',
             'Catastrophic',
             'Denver', 
             'Louisiana')
            )              
                        
cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('xut5eesn24',
             'zhw20jc816',
             'hrpgpu',
             'mjibpv',
             '18 July 1987', 
             '39',
             'F')
            ) 

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('tqf2wgii62',
             'zhw20jc816',
             'wxprjiz',
             'i',
             '23 July 2014', 
             '72',
             'F')
            ) 

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('isx2lhiz87',
             'zhw20jc816',
             'rtzloat',
             'pndfe',
             '21 June 1972', 
             '14',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('gea3xeiu78',
             'tyk34sx279',
             'ydxjl',
             'nvemillktt',
             '19 August 1970', 
             '7',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('xlp8nnih24',
             'tyk34sx279',
             'kivf',
             'n',
             '4 October 1981', 
             '75',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('wwn2azxr40',
             'tyk34sx279',
             'cfk',
             'vrslzem',
             '11 April 2005', 
             '5',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('cay3hmpu28',
             'gof12ih190',
             'ar',
             'qaiqlqaw',
             '14 November 1982', 
             '90',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('oye7ugsv25',
             'gof12ih190',
             'bluosux',
             'blbzzoaww',
             '2 July 2009', 
             '41',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('mff5qcrm46',
             'gof12ih190',
             'joelkvwi',
             'hrqybn',
             '18 September 1961', 
             '80',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('gjy5hohq05',
             'ous85wn249',
             'xgxplwqtpp',
             'plxawdnlu',
             '9 February 1982', 
             '97',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('yjq4dxcf40',
             'ous85wn249',
             'terts',
             'fmantivz',
             '24 June 1961', 
             '26',
             'F')
            )
            
cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('yrw5jrqc24',
             'ous85wn249',
             'utmxqizi',
             'thu',
             '23 May 2021', 
             '1',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('nlw4paqj74',
             'nek92od060',
             'wlcyyll',
             'mtcx',
             '21 January 1960', 
             '14',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('dni7myqs79',
             'nek92od060',
             'hixsi',
             'xjllx',
             '24 September 2017', 
             '24',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('ycf6mevn90',
             'nek92od060',
             'ecoizmmfhm',
             'qlmhh',
             '27 June 2021', 
             '1',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('mhi7btfs21',
             'guq98px044',
             'zkyqusv',
             'wtwr',
             '17 January 2005', 
             '61',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('zqh7sfqi67',
             'guq98px044',
             'gbtejpw',
             'pdmspx',
             '1 March 1976', 
             '15',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('hpg0hkof26',
             'guq98px044',
             'nlgipholu',
             'hpdpdjgta',
             '12 October 1980', 
             '89',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('jkh5lmxh98',
             'ykq09is184',
             'kzhjhlnq',
             'ryjuisvvnr',
             '8 May 2002', 
             '27',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('skd4vqoa55',
             'ykq09is184',
             'tb',
             'evkonll',
             '28 October 19862', 
             '92',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('kvn4xyal22',
             'ykq09is184',
             'tbgjs',
             'ctqqrqy',
             '14 May 2011', 
             '50',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('zeb7pphb47',
             'fat60sj562',
             'txpp',
             'cb',
             '3 June 2017', 
             '85',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('bqo0jcmc70',
             'fat60sj562',
             'eatq',
             'ponlwqkug',
             '18 April 1966', 
             '3',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('pzg5axzf04',
             'fat60sj562',
             'exjrzqf',
             'j',
             '26 September 1977', 
             '94',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('dfu5itnn48',
             'iys45xm229',
             'zdb',
             'er',
             '14 February 1970', 
             '68',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('rvf8zpdd35',
             'iys45xm229',
             'j',
             'fbdthxccs',
             '28 April 1989', 
             '13',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('jgk9nxhs09',
             'iys45xm229',
             'fxyey',
             'fg',
             '19 November 1990', 
             '39',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('vaf5fcje40',
             'tia75mc421',
             'kpfq',
             'jdiwmh',
             '19 July 2010', 
             '36',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('leu9nzpm33',
             'tia75mc421',
             'ljouprba',
             'uwmsv',
             '27 July 2018', 
             '41',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('ggd8ijyw43',
             'tia75mc421',
             'fuqqdo',
             'svzithfvkz',
             '23 March 2002', 
             '20',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('trx4ewrw34',
             'llb18lx345',
             'ayiccijkyp',
             'qhvrviazb',
             '24 December 1981', 
             '18',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('xky1mety81',
             'llb18lx345',
             'anaukz',
             'mhwtfveze',
             '19 June 1981', 
             '51',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('fqe5sxcp52',
             'llb18lx345',
             'ayiccijkyp',
             'bulwfrish',
             '2 December 1966', 
             '79',
             'F')
            )
            
cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('rwa3fjqo63',
             'zsx48hj408',
             'tin',
             'olzrpbqm',
             '17 March 1969', 
             '69',
             'F')
            )            
 
cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('fbb0assv63',
             'zsx48hj408',
             'ha',
             'dvc',
             '15 July 1976', 
             '49',
             'F')
            )            
            
cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('lvd7oask99',
             'zsx48hj408',
             'ixafqflbjf',
             'laokt',
             '30 July 1974', 
             '69',
             'F')
            )           

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('zos0vqrf57',
             'ukz02is226',
             'ijufchna',
             'gessof',
             '4 August 1976', 
             '92',
             'F')
            ) 

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('mhy7yffr28',
             'ukz02is226',
             'xhm',
             'lksehly',
             '22 July 1987', 
             '95',
             'F')
            ) 

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('nxc8ptkn71',
             'ukz02is226',
             'ekdfv',
             'rcfcdbi',
             '17 October 1993', 
             '39',
             'F')
            ) 

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('tdi9fvuo41',
             'ntj91ib412',
             'ub',
             'brjkquxmly',
             '2 January 1980', 
             '93',
             'M')
            ) 

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('ofk7klzw39',
             'ntj91ib412',
             'eojbunr',
             'ujafnpfxew',
             '20 March 1971', 
             '10',
             'M')
            ) 

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('fps0dzsk35',
             'ntj91ib412',
             'tw',
             'aeqgusuiaa',
             '17 March 1983', 
             '25',
             'M')
            ) 

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('eyv6uqvy58',
             'mhn03km027',
             'fyymet',
             'td',
             '27 August 2004', 
             '60',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('yre4umiy58',
             'mhn03km027',
             'vkl',
             'yiuugivyoa',
             '24 November 1995', 
             '60',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('dtu4bpmf55',
             'mhn03km027',
             'q',
             'sa',
             '23 July 2005', 
             '98',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('ldg9iwwg43',
             'wmx92ag739',
             'opwoe',
             'fqjmxiinf',
             '25 December 1996', 
             '35',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('zxc2nbcz47',
             'wmx92ag739',
             'n',
             'baoniq',
             '16 January 1987', 
             '27',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('dap8rwxz47',
             'wmx92ag739',
             'fn',
             'aiei',
             '1 December 1972', 
             '38',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('ple9efmk82',
             'lsb53zp487',
             'rtkercck',
             'sillem',
             '28 September 1979', 
             '29',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('oew9qofa04',
             'lsb53zp487',
             'cwylrljm',
             'kkbwvgr',
             '15 October 2020', 
             '58',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('hgm9yvxl58',
             'lsb53zp487',
             'xrqtz',
             'hpxi',
             '28 June 1966', 
             '22',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('stm9sgnb86',
             'rkf74bg521',
             'vasdcleg',
             'rsuwgucb',
             '26 April 2016', 
             '85',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('awd2kpsa35',
             'rkf74bg521',
             'yxe',
             'cemxpq',
             '5 November 2013', 
             '85',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('fhr4hdgn53',
             'rkf74bg521',
             'jgxndvjy',
             'phuqzkspvr',
             '9 May 2008', 
             '85',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('dzc8tvnz49',
             'ppn08fj507',
             'nhtfrnci',
             'nqqgg',
             '16 June 1988', 
             '44',
             'M')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('bba8uhkp63',
             'ppn08fj507',
             'wwsb',
             'mwauoel',
             '8 September 1994', 
             '14',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('hxu3nedx90',
             'ppn08fj507',
             'uya',
             'gbhddbwlr',
             '5 March 1993', 
             '82',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('ezl2gewd67',
             'jii02dr566',
             'vz',
             'omspo',
             '15 February 2012', 
             '80',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('zec9pang88',
             'jii02dr566',
             'zm',
             'ewodgrpb',
             '10 October 1977', 
             '79',
             'F')
            )

cur.execute('INSERT INTO Casualties(casualty_id, event_ntsb_number, first_name, last_name, dob, age, sex ) '
            'VALUES(%s,%s,%s,%s,%s,%s,%s)',
            ('rgl4bwgo84',
             'jii02dr566',
             'ieitvcs',
             'vboxqzze',
             '20 September 1960', 
             '3',
             'M')
            )
            
cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'zhw20jc816' + '\' WHERE aircraft_reg_number =  \'' + 'vo0647' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'tyk34sx279' + '\' WHERE aircraft_reg_number =  \'' + 'tr4824' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'gof12ih190' + '\' WHERE aircraft_reg_number =  \'' + 'fb3513' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'ous85wn249' + '\' WHERE aircraft_reg_number =  \'' + 'gd4294' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'nek92od060' + '\' WHERE aircraft_reg_number =  \'' + 'oa8766' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'guq98px044' + '\' WHERE aircraft_reg_number =  \'' + 'ux8920' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'ykq09is184' + '\' WHERE aircraft_reg_number =  \'' + 'cm4946' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'fat60sj562' + '\' WHERE aircraft_reg_number =  \'' + 'au4275' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'iys45xm229' + '\' WHERE aircraft_reg_number =  \'' + 'de9625' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'llb18lx345' + '\' WHERE aircraft_reg_number =  \'' + 'kh6269' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'zsx48hj408' + '\' WHERE aircraft_reg_number =  \'' + 'sp6303' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'ukz02is226' + '\' WHERE aircraft_reg_number =  \'' + 'ii5207' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'ntj91ib412' + '\' WHERE aircraft_reg_number =  \'' + 'uj7834' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'mhn03km027' + '\' WHERE aircraft_reg_number =  \'' + 'he6251' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'wmx92ag739' + '\' WHERE aircraft_reg_number =  \'' + 'qa7530' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'lsb53zp487' + '\' WHERE aircraft_reg_number =  \'' + 'zr5082' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'rkf74bg521' + '\' WHERE aircraft_reg_number =  \'' + 'ps3752' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'ppn08fj507' + '\' WHERE aircraft_reg_number =  \'' + 'ta7671' + '\'')

cur.execute('UPDATE Aircraft SET event_ntsb_number = \'' + 'jii02dr566' + '\' WHERE aircraft_reg_number =  \'' + 'ae0784' + '\'')

conn.commit()

cur.close()
conn.close()
