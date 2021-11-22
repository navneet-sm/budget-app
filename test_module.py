class Category:
    
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance
        
    def check_funds(self, amount):
        if (self.get_balance() != None) and (amount > self.get_balance()):
            return False
        else:
            return True
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def transfer(self, amount, b_category):
        if self.check_funds(amount) is True:
            self.withdraw(-amount, f"Transfer to {b_category.name}")
            b_category.deposit(amount, f"Transfer from {self.name}")    
            return True
        else:
            return False
        
    def __str__(self):
        name = self.name.center(30,'*')
        items = ''
        for item in self.ledger:
            items += str(item['description'][:23]).ljust(23, ' ') + '{:.2f}'.format(item['amount']).rjust(7, ' ') + '\n'
        total = 'Total: ' + str('{:.2f}'.format(self.get_balance()))
        reciept = f'{name}\n{items}{total}'
        return reciept  

def create_spend_chart(categories):
    total, total_exp, total_d, c_names = 0, 0, {}, []
    for category in categories:
        for item in category.ledger:
            if item['amount'] < 0:
                total += -item['amount']
                total_exp += -item['amount']
        total_d[category.name] = [total]
        total = 0
    total_d['Total Expenses'] = total_exp
    chart_d = {k:'' for k in range(0, 110, 10)}
    for category in categories:
        p = round(((total_d[category.name][0] / total_exp) * 100)/ 10) * 10
        total_d[category.name].append(p)
        for i in range(0, 110, 10):
            if total_d[category.name][1] >= i:
                if len(chart_d[i]) <= 1:
                    chart_d[i] += ' o'
                else:
                    chart_d[i] += '  o'
            else:
                chart_d[i] += '  '
        c_names.append(category.name)
    line = len(chart_d[0]) * '-'
    chart_d['line'] = f'    {line}--\n'
    x, chart = 100, 'Percentage spent by category\n'
    while x >= 0:
        n = str(x).rjust(3, ' ')
        chart += f'{n}|{chart_d[x]}\n'
        x -= 10
    chart += chart_d['line']
    names = '   '
    for i in range(max(len(x) for x in c_names)):
        for name in c_names:
            name = name.ljust((max(len(x) for x in c_names)), ' ')
            names += f'  {name[i]}'
        names += '\n   '
    chart += names
    return chart.rstrip('\n')
class Category:
    
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance
        
    def check_funds(self, amount):
        if (self.get_balance() != None) and (amount > self.get_balance()):
            return False
        else:
            return True
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def transfer(self, amount, b_category):
        if self.check_funds(amount) is True:
            self.withdraw(-amount, f"Transfer to {b_category.name}")
            b_category.deposit(amount, f"Transfer from {self.name}")    
            return True
        else:
            return False
        
    def __str__(self):
        name = self.name.center(30,'*')
        items = ''
        for item in self.ledger:
            items += str(item['description'][:23]).ljust(23, ' ') + '{:.2f}'.format(item['amount']).rjust(7, ' ') + '\n'
        total = 'Total: ' + str('{:.2f}'.format(self.get_balance()))
        reciept = f'{name}\n{items}{total}'
        return reciept  

def create_spend_chart(categories):
    total, total_exp, total_d, c_names = 0, 0, {}, []
    for category in categories:
        for item in category.ledger:
            if item['amount'] < 0:
                total += -item['amount']
                total_exp += -item['amount']
        total_d[category.name] = [total]
        total = 0
    total_d['Total Expenses'] = total_exp
    chart_d = {k:'' for k in range(0, 110, 10)}
    for category in categories:
        p = round(((total_d[category.name][0] / total_exp) * 100)/ 10) * 10
        total_d[category.name].append(p)
        for i in range(0, 110, 10):
            if total_d[category.name][1] >= i:
                if len(chart_d[i]) <= 1:
                    chart_d[i] += ' o'
                else:
                    chart_d[i] += '  o'
            else:
                chart_d[i] += '  '
        c_names.append(category.name)
    line = len(chart_d[0]) * '-'
    chart_d['line'] = f'    {line}--\n'
    x, chart = 100, 'Percentage spent by category\n'
    while x >= 0:
        n = str(x).rjust(3, ' ')
        chart += f'{n}|{chart_d[x]}\n'
        x -= 10
    chart += chart_d['line']
    names = '   '
    for i in range(max(len(x) for x in c_names)):
        for name in c_names:
            name = name.ljust((max(len(x) for x in c_names)), ' ')
            names += f'  {name[i]}'
        names += '\n   '
    chart += names
    return chart.rstrip('\n')
