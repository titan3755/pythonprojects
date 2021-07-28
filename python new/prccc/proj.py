def convert(cfrm, cto, val):
    if cfrm == 'lbs' and cto == 'kg':
        result = val * 0.453592
        return result
    elif cfrm == 'lbs' and cto == 'oz':
        result = val * 16
        return result
    elif cfrm == 'lbs' and cto == 'ton':
        result = val * 0.000453592
        return result
    elif cfrm == 'kg' and cto == 'lbs':
        result = val * 2.2046244202
        return result
    elif cfrm == 'kg' and cto == 'ton':
        result = val * 0.001
        return result
    elif cfrm == 'kg' and cto == 'oz':
        result = val * 35.273990723
        return result
    elif cfrm == 'ton' and cto == 'lbs':
        result = val * 2204.6244202
        return result
    elif cfrm == 'ton' and cto == 'kg':
        result = val * 1000
        return result
    elif cfrm == 'ton' and cto == 'oz':
        result = val * 35273.990723
        return result
    elif cfrm == 'oz' and cto == 'lbs':
        result = val * 0.0625
        return result
    elif cfrm == 'oz' and cto == 'kg':
        result = val * 0.0283495
        return result
    elif cfrm == 'oz' and cto == 'ton':
        result = val * 0.0000283495
        return result
    else:
        err = 'Invalid Values!'
        return err