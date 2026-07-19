import logging


logging.basicConfig(filename=r'./sprint-05/loggers/app.log',
                    filemode='w',
                    level=logging.NOTSET,
                    format='%(name)s - %(levelname)s - %(funcName)s - %(message)s')


class AccountError(Exception):
    def __init__(self, message):
        super().__init__(message)
        logging.error(f'AccountError: {message}')


class IncorrectNameType(AccountError):
    def __init__(self, message='Name must be a string.'):
        super().__init__(message)


class NegativeBalance(AccountError):
    def __init__(self, message='Initial balance cannot be negative.'):
        super().__init__(message)


class InvalidDeposit(AccountError):
    def __init__(self, message='Invalid deposit to balance: Amount must be positive.'):
        super().__init__(message)


class WithdrawalAmount(AccountError):
    def __init__(self, message='Invalid amount to withdraw: Exceeds balance or is negative.'):
        super().__init__(message)




class Account:
    __pk = 0


    def __init__(self, name, balance):
        if not isinstance(name, str):
            raise IncorrectNameType()
        if not isinstance(balance, (int, float)):
            message = 'Balance must be a number.'
            raise AccountError(message)
        if balance < 0:
            raise NegativeBalance()

        Account.__pk += 1
        self.pk = Account.__pk
        self.name = name
        self.__balance = balance

        self.logger = logging.getLogger(f'account_{self.pk}')
        self.logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler(filename=fr'./sprint-05/loggers/account_{self.pk}.log', mode='w')
        formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
        message = f'Account {self.pk} created for {self.name} with initial balance {self.__balance}'
        logging.info(message)


    def get_balance(self):
        message = f'Checked balance for Account {self.pk}: {self.__balance}'
        self.logger.info(message)
        return self.__balance


    def deposit(self, amount):
        if amount < 0:
            raise InvalidDeposit()
        self.__balance += amount
        message = f'Deposited {amount}. New balance: {self.__balance}'
        self.logger.info(message)


    def withdraw(self, amount):
        if amount < 0 or self.__balance < amount:
            raise WithdrawalAmount()
        self.__balance -= amount
        message = f'Withdrew {amount}. New balance: {self.__balance}'
        self.logger.info(message)


    def __del__(self):
        if hasattr(self, 'logger'):
            for handler in self.logger.handlers[:]:
                handler.close()
                self.logger.removeHandler(handler)

        if hasattr(self, 'pk'):
            logging.info(f'Account {self.pk} deleted.')


    def __str__(self):
        return f'Account pk: {self.pk}, Name: {self.name}, Balance: {self.__balance}'




def create_account(name, initial_balance):
    try:
        new_account = Account(name, initial_balance)
    except AccountError as error:
        logging.error(f'Failed to create account: {error}')
        return None
    else:
        logging.info(f'Account created successfully: {new_account}')
        return new_account



account = create_account("John Doe", 1000)
print(account)


account = create_account("John Doe", 1000)
account.deposit(200) 
account.deposit(300)


account1 = create_account("John Doe", 1000)
account2 = create_account("Jane Smith", 500)
account1.deposit(200)
account2.withdraw(300)
account2.deposit(100)
account1.withdraw(300)


account = create_account(None, 1000)
print(account)
account = create_account("Emilio Frazier", None)
print(account)
account = create_account("Elisa Saunders", -200)
print(account)


account1 = create_account("John Doe", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.get_balance()
print(account1.get_balance())
account2 = create_account("Jane Smith", 2000)
account2.deposit(1000)
account2.withdraw(500)
print(account2.get_balance())
