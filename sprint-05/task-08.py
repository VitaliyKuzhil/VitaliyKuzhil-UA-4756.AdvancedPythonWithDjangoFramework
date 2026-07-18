import logging

logging.basicConfig(filename='app.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(name)s - %(levelname)s - %(message)s')


def average(numbers):
    
    if not numbers:
        logging.debug('The list is empty')

    try:
        result = sum(numbers) / len(numbers)

    except ZeroDivisionError:
        logging.warning('Division by zero')

    except ValueError:
        logging.error()

    except TypeError:
        logging.critical('Incorrect data entered')

    else:
        logging.info(result)


average([1, 2, 3, 4, 5])
average([10, -20, -30])
average([])
average([1, 2, 3, 0, 5])
average([1, 2, "three", 4, 5])
