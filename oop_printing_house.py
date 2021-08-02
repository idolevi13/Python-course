class PrintOrder:

    def __init__(self, client_name, copies):
        if client_name =="":
            raise ValueError ("Invalid input")
        else:
            self.client_name= client_name

        if copies<1:
            raise ValueError ("Invalid input")
        else:
            self.copies= copies

    def __repr__(self):
        return "Client name: " + self.client_name + ", Copies: " + str(self.copies) +","

class PosterOrder (PrintOrder):

    def __init__(self, client_name, copies, size):
        PrintOrder.__init__(self, client_name, copies)
        if len(size)!=2 or size[0]<1 or size[1]<1:
            raise ValueError ("Invalid poster size")
        else:
            self.size= size

    def __repr__(self):
        return "Poster order: " + PrintOrder.__repr__(self) + " Size: "+ str(self.size)

    def calc_cost(self):
        cost = self.copies * self.size[0] * self.size[1] * 30
        return cost

class LetterOrder (PrintOrder):

    def __init__(self, client_name, copies, paper_type, paper_prices):
        PrintOrder.__init__(self, client_name, copies)
        if paper_type not in paper_prices.keys():
            raise ValueError ("Invalid paper type")
        else:
            self.paper_type= paper_type
        self.paper_prices= paper_prices

    def __repr__(self):
        return "Letter order: " + PrintOrder.__repr__(self) + " Paper type: " + self.paper_type

    def calc_cost(self):
        cost= self.copies * self.paper_prices[self.paper_type]
        return cost

class PrintShop:

    def __init__(self):
        self.orders= []
        self.revenues=0

    def add_order (self, order):
        self.orders.append(order)

    def print_next_order (self):
        if self.orders==[]:
            return
        order = self.orders.pop(0)
        self.revenues+= order.calc_cost()

    def __repr__(self):
        printshop_dic={}
        for order in self.orders:
            count= printshop_dic.get (order.client_name, 0)
            count+=1
            printshop_dic[order.client_name]=count
        to_print=""
        headline= "Print shop orders:\n"
        for key in printshop_dic.keys():
            to_print += key + " : " + str(printshop_dic[key]) + " orders\n"
        return headline + to_print + "Revenues: " + str(self.revenues)
