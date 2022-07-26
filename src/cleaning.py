# Cleaning columns names
import pandas as pd

def stand_colum_name(df):
    """
    standardize column names
    """
  
    dict_rename = {column : column.lower().strip() for column in df.columns}
    df = df.rename(dict_rename, axis = 1, inplace = True)

    return df
# Changing the type to float
def historic_to_float(df):
    """
    change commas into dots and strings to float
    """
    for i in df.columns:
        try:
            df[i] = df[i].apply(lambda x: float(x.replace(",", ".")))
        except:
            pass
    return df

def temperature(df):
    """
    replace - in strings
    """

    df['average yearly temperature (1961–1990 celsius)'] = df['average yearly temperature (1961–1990 celsius)'].apply(lambda x: x.replace('−','-'))

# Changing the type
def percent_to_float(df):
    """
    change percentages into floats
    """

    for i in df.columns:
        if i != 'average yearly temperature (1961–1990 celsius)':
            try:
                df[i] = df[i].apply(lambda x: float(x.replace("%", "")))
            except:
                pass
    return df

def to_numeric(df):
    """
    change temperatures from string to float
    """
      
    try:
        df = df.apply(pd.to_numeric)
    except:
        pass
    df['average yearly temperature (1961–1990 celsius)'] = df['average yearly temperature (1961–1990 celsius)'].apply(lambda x: float(x))

    return df    

dataset = pd.read_csv('output/merged.csv')
df = stand_colum_name(dataset)
df = historic_to_float(dataset)
df = temperature(dataset)
df = percent_to_float(dataset)
df = to_numeric(dataset)

df.to_csv('output/clean.csv')
