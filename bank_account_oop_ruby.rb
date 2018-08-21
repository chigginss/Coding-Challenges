""" 
Create a bank account class with checking and saving accounts. 
Add methods to deposite, withdraw, check balance, transfer and track how many accounts the bank has 

practice with Ruby OOP 

"""

class bankAccount

    private 
    
    @@number_of_accounts = 0
    @@interest_rate = 1.25

    attr_writer: :account_number, :checking, :saving
    
    def create_account_number
        rand(10**16)
    end
   
    public
    attr_reader :`
    def initialize (checking_deposit, saving_deposit)
        @account_number = create_account_number
        @checking = checking_deposit
        @savings = saving_deposit
        @@number_of_accounts += 1
    end

    def deposit (account, amount)
        if account == "checking"
            @checking += amount
        elsif account == "savings"
            @saving += amount
        else
            p "no account"
    end

    def withdraw (account, amount)
        if account == "checking"
            if amount > @checking
                p "insufficient funds"
            else
                @checking -= amount 
        elsif account == "savings"
            if amount > @savings
                p "insufficient funds"
            else
                @savings -= amount 
        else
            p "no account"
    end

    def account_info
        p @account_number
        p @checking
        p @savings
        p @@interest_rate
    end

    def total_money
        p @checking + @savings
    end

    def total_accounts
        p @@number_of_accounts
    end

    def get_checking
        @checking
    end

    def get_savings
        @savings
    end
end 

my_account = bankAccount.new(500,2000)
# p mine.deposit("checking")





