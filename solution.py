import pandas as pd
import numpy as np
import scipy.stats as st
from scipy.stats import mannwhitneyu

chat_id = 1307537098 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, 
             y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    res = mannwhitneyu(x, y, alternative='greater')
    p_value=res.pvalue
    if (p_value<0.06):
        return True
    else:
        return False
