# librariesfrom datetime import datetimeimport pandas as pdimport numpy as np# generate positive/negative derivative# get date# find week date is contained in# return positive or negative based on change column# import datadef load_data(data_path, data_fn):    data = pd.read_csv(data_path + data_fn)    data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%y')    return datadef find_week(data, date):    nearest_dates_idx = np.abs(data['Date'] - date)    return np.argmin(nearest_dates_idx)def pos_or_neg(data, date):    nearest_week = find_week(data, date)    if data['change'].iloc[nearest_week] >= 0:        return 1    else:        return -1def main():    data_path = '/Users/212473475/git/ri_headlines/stock_data/'    data_fn = 'vow3.de_from_010115to022117.csv'    print data_path + data_fn    data = load_data(data_path, data_fn)    print data    scandalish = datetime(2015, 9, 20)    nearest_week = find_week(data ,scandalish)    print nearest_week    print data.iloc[nearest_week]    print pos_or_neg(data, scandalish)if __name__ == '__main__': main()