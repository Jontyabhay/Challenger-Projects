checking_balance = 0
savings_balance = 0

def check_balance(account_type, checking_balance, savings_balance):
    if account_type == 'savings':
        balance = savings_balance
    elif account_type == 'checking':
        balance = checking_balance
    else:
        return "Unsuccessful, please enter \"checking\" or \"savings\""
    balance_statement = "Your" + account_type + " balance is " + str(balance)
    return balance_statement

print(checking_balance("chekcing",check_balance,savings_balance))
print(checking_balance("savings",check_balance,savings_balance))

def make_deposit(account_type,amount,checking_balance,savings_balance):
    deposit_status = ""
    if amount > 0:
        if account_type == 'savings':
            savings_balance += amount
            deposit_status ='successful'
        elif account_type == 'checking':
            checking_balance += amount
            deposit_status = 'successful'
        else:
            deposit_status = "Unsuccessful, please enter \"checking\" or \"savings\""
    else:
        deposit_status = "unsuccessful, please enter an amount greater than 0"
    deposit_statement = "Deposit of " + str(amount) + " to your " + account_type + " account was " + deposit_status
    print(deposit_statement)
    return savings_balance,checking_balance

savings_balance,checking_balance = make_deposit("savings",10,checking_balance,savings_balance)
print(check_balance("savings",checking_balance,savings_balance))
savings_balance,checking_balance = make_deposit("checking",200,checking_balance,savings_balance)
print(check_balance("checking",checking_balance,savings_balance))

def make_withdrawal(account_type,amount,checking_balance,savings_balance):
    withdrawal_status = ""
    fail = "Unsuccessful, please enter amount less than balance"
    if account_type == "savings":
        if amount <= savings_balance:
            savings_balance -= amount
            withdrawal_status = "successful"
        else:
            withdrawal_status = fail
    elif account_type == "checking":
        if amount <= checking_balance:
            checking_balance -= amount
            withdrawal_status = "successful"
        else:
            withdrawal_status = fail
    else:
        withdrawal_status = "unsuccessful, please enter \"checking\" or \"savings\""
    withdrawal_statement = "Withdrawal of " + str(amount) + " dollars from your " + account_type + " was " + withdrawal_status
    print(withdrawal_statement)
    return savings_balance,checking_balance

savings_balance,checking_balance = make_withdrawal("savings",11,checking_balance,savings_balance)
print(check_balance("savings",checking_balance,savings_balance))
savings_balance,checking_balance = make_withdrawal("checking",170,checking_balance,savings_balance)
print(check_balance("savings",checking_balance,savings_balance))

def acc_transfer(acc_from,acc_to,amount,savings_balance,checking_balance):
    trans_status = ""
    trans_error = "unsuccessful, please enter amount less than"
    if acc_from == 'savings' and acc_to == 'checking':
        if amount <= savings_balance:
            savings_balance -= amount
            checking_balance += amount
            trans_status = "successful"
        else:
            trans_status = trans_error + str(savings_balance)
    elif acc_from == 'checking' and acc_to == 'savings':
        if amount <= checking_balance:
            checking_balance -= amount
            savings_balance += amount
            trans_status = "successful"
        else:
            trans_status = trans_error + str(checking_balance)
    else:
        trans_status = "unsuccessful, please enter \"checking\" or \"savings\""
    trans_statement = "Transfer of " + str(amount) + " from your " + acc_from + " to your " + acc_to + " account was " + trans_status
    print(trans_statement)
    return savings_balance,checking_balance

savings_balance,checking_balance = acc_transfer("checking","savings",40,checking_balance,savings_balance)
print(check_balance("checking",checking_balance,savings_balance))
print(check_balance("savings",checking_balance,savings_balance))
savings_balance,checking_balance = acc_transfer("savings","checking",5,checking_balance,savings_balance)
print(check_balance("checking",checking_balance,savings_balance))
print(check_balance("savings",checking_balance,savings_balance))