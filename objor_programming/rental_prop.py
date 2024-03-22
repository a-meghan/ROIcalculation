class ROI():
    def __init__(self, firstname):
        """
        Greets user once a name is provided, this will initialize the class.
        """
        self.firstname = firstname
        print(f'\nHello {self.firstname}!')
        print("\nIn order for me to accurately estimate your monthly return rate, I must first ask a series of questions regarding the finances of your property.")
        print("If a question does not apply to you, please enter 0. All questions must be answered as a monthly value.")

    def income(self):
        """
        Asks user a series of questions to gather information regarding the amount
        of income generated from a given rental property.
        User input is stored in a list, and use sum() to find the total property
        income which is stored in a variable
        """
        self.propIncome = []
        print("\nLet's get started with income earned by your property:")

        rental_inc = int(input("How much do you earn from collecting rent? $"))
        self.propIncome.append(rental_inc)
        rental_util = int(input("How much do you earn from collecting on utilities from tenants? $"))
        self.propIncome.append(rental_util)
        laundryFee = int(input("How much do you earn from any laundry services provided to tenants? $"))
        self.propIncome.append(laundryFee)
        storage = int(input("How much do you earn from any garage/storage space provided to tenants? $"))
        self.propIncome.append(storage)
        parking = int(input("How much does your property earn for any parking services provided to tenants? $"))
        self.propIncome.append(parking)

        while True:
            misc = int(input("\nPlease enter any other income values that may not have been asked about, and enter 0 when finished: $"))
            self.propIncome.append(misc)
            if misc == 0:
                break

        # Adding together the input data provided by user
        self.total_income = sum(self.propIncome)
        print(f"Your property brings in ${self.total_income}")

    def expenses(self):
        """
        Asks user a series of questions regarding the expenses of owning their rental property each month.
        User input is stored in a list, and use sum() to find the total property
        expenses which is then stored in a variable.
        """
        self.propExpenses = []
        print("\nNow that I know how much your property brings in, I need to know how much goes out. ")

        prop_mortgage = int(input("How much is your property mortgage? $"))
        self.propExpenses.append(prop_mortgage)
        prop_tax = int(input("How much do you pay in property tax? $"))
        self.propExpenses.append(prop_tax)
        prop_insurance = int(input("How much do you pay for property insurance? $"))
        self.propExpenses.append(prop_insurance)
        prop_HOA = int(input("What do you pay for HOA fees and services? $"))
        self.propExpenses.append(prop_HOA)
        prop_lawn = int(input("How much do you pay for lawn services each month? $"))
        self.propExpenses.append(prop_lawn)
        # Utilities
        util_gas = int(input("How much do you pay for gas services each month? $"))
        self.propExpenses.append(util_gas)
        util_power = int(input("How much do you pay for electric/power services each month? $"))
        self.propExpenses.append(util_power)
        util_water = int(input("How much do you pay for water each month? $"))
        self.propExpenses.append(util_water)
        util_sewage = int(input("How much do you pay for sewage services each month? $"))
        self.propExpenses.append(util_sewage)
        util_trash = int(input("How much do you pay for garbage services each month? $"))
        self.propExpenses.append(util_trash)
        # Fall-back money
        fund_vacancy = int(input("How much do you put back for unexpected vacancies each month? $"))
        self.propExpenses.append(fund_vacancy)
        fund_repairs = int(input("How much do you put back for repairs each month? $"))
        self.propExpenses.append(fund_repairs)
        fund_CapEx = int(input("How much do you put back for Capital Expenditures (CapEx) each month? $"))
        self.propExpenses.append(fund_CapEx)
        fund_management = int(input("How much do you put back for propery management each month? $"))
        self.propExpenses.append(fund_management)

        while True:
            other_exp = int(input("\nPlease enter any other property expenses that may not have been asked about, and enter 0 when finished: $"))
            self.propExpenses.append(other_exp)
            if other_exp == 0:
                break

        # Adding together the input data provided by user
        self.total_expenses = sum(self.propExpenses)
        print(f"Your property expenses come out to be ${self.total_expenses} each month.")

    def cashFlow(self):
        """
        This function finds the difference between the summed variables from income() and expenses(), and tells user
        if their property is making money or losing it- and by how much.
        """

        self.diff = self.total_income - self.total_expenses
        if self.diff < 0:
            print(f"Your property loses ${self.diff} monthly.")
        else:
            print(f"Your monthly cashflow is ${self.diff}")

    def cash_on_cash(self):
        """
        This function asks about how much user spent going into the purchasing/investment costs and
        returns the sum total investment cost.
        """

        self.investment_costs = []
        print("Now I just need to know about how much you invested into your property:")
        downpayment = int(input("How much did you put down on your property? $"))
        self.investment_costs.append(downpayment)
        closing_costs = int(input("How much did you pay in closing costs? $"))
        self.investment_costs.append(closing_costs)
        repair_budget = int(input("How much did you set back, or pay, for repair costs? $"))
        self.investment_costs.append(repair_budget)

        while True:
            other_misc = int(input("\nPlease enter any other up front costs/investments that may not have been asked about, and enter 0 when finished: $"))
            self.investment_costs.append(other_misc)
            if other_misc == 0:
                break

        # Adding values provided by user...
        self.total_investment = sum(self.investment_costs)
        print(f"You invested ${self.total_investment} into your property.")
        print("\nTime to calculate...")

    def calcROI(self):
        """
        This function tells user the final calculation on their return of investment.
        Function returns a %
        """
        annual_cf = self.diff * 12
        finalROI = (annual_cf / self.total_investment)
        print(f"Your ROI rate comes out to... {finalROI}")