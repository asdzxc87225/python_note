import localtime

def test():
    t = datetime.datetime(2002,9,3)
    lt = Lunar(t)
    st =(lt.gz_year()+'年'+lt.ln_date_str()+lt.gz_day()+'日屬'+lt.sx_year())
    print(st)
    return(st)
    
if __name__ == '__main__':
    print('hi')
