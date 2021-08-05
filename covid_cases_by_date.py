def get_covid_cases_by_date(filename, date):

    f=None
    try:
        d={}
        f=open(filename, 'r', encoding='UTF-8')
        for line in f:
            if date not in line:
                continue
            city_name=line.strip().split(',')[-1]
            if line.split(',')[5]=="<15":
                d[city_name] = d.get(city_name, 0)
            else:
                d[city_name]=d.get(city_name,0)+int(line.split(',')[5])
        for city_name in sorted(d,key=d.get,reverse=True)[:10]:
            print(str(d[city_name])+'\t'+city_name)
        if d=={}:
            print('No data is available for date',date)
    except IOError:
        print('IO Error encountered')
    finally:
        if f!=None:
            f.close()
