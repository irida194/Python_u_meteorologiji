years=[1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005]
leap_y=filter(lambda x: (x%4==0 and x%100 !=0) or (x%400==0),years)
print(list(leap_y))