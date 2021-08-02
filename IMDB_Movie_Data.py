# Exercise 6: Python Programming
def top5_by_genre(genre_name, file_name):

    f = None
    target = None
    try:
        d_revenue = {}
        d_rank = {}
        lines = []
        f = open(file_name, 'r')
        target = open('top5.csv', 'w')
        target.write(f.readline())
        genre_name = genre_name.title()
        for line in f:
            if genre_name not in line:
                continue
            movie_name = line.strip().split(',')[1]
            revenue = line.strip().split(',')[-2]
            rank = line.strip().split(',')[0]
            d_revenue[movie_name] = float(revenue)
            d_rank[movie_name] = int(rank)
            lines.append(line)
        sorted_revenue = sorted(d_revenue, key=d_revenue.get, reverse=True)[:5]
        sorted_rank = sorted(sorted_revenue, key=d_rank.get)
        for movie_name in sorted_rank:
            for line in lines:
                if movie_name == line.strip().split(',')[1]:
                    target.write(line)
        if d_revenue == {}:
            print('No data is available for date', date)
    except IOError:
        print('IO Error encountered')
        return (0)
    finally:
        if f != None:
            f.close()
            target.close()
            return (1)
        else:
            return (0)
