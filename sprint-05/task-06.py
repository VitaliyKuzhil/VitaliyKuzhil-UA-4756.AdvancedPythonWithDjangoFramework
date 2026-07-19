import math
import logging

logging.basicConfig(filename='./sprint-05/loggers/app_task-06.log', level=logging.NOTSET)


def findingTangent(sin_alpha, cos_alpha):

    logging.info(f'A value has been entered sin(alpha) = {sin_alpha}')
    logging.info(f'A value has been entered cos(alpha) = {cos_alpha}')

    try:
        tan_alpha = sin_alpha / cos_alpha
    except ZeroDivisionError:
        logging.warning(f'The cosine of the angle alpha = {cos_alpha}. The tangent is not defined.')
    except TypeError:
        logging.critical(f'The tangent of the angle alpha is not defined.')
    else:
        logging.debug(f'The value of the tangent of the angle alpha is found = {tan_alpha}')


findingTangent(0.5, math.sqrt(3) / 2)
findingTangent(0.5, 'w')
findingTangent(0.5, 0)