def compute_cpi09(cpi):
    # CPI (base 2009)
    base09 = cpi.loc['2009'].mean()
    cpi09 = cpi / base09
    return cpi09
