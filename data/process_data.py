import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """Load & merge "Messages" & "Categories" tables
    
    inputs:
    messages_filepath: string. Filepath for the csv file containing "Messages" dataset.
    categories_filepath: string. Filepath for the csv file containing "Categories" dataset.
       
    outputs:
    df: dataframe. Dataframe containing merged view of "Messages" & "Categories" tables.
    """

    #Loading "Messages" dataset
    messages = pd.read_csv(messages_filepath)
    
    #Loading "Categories" dataset
    categories = pd.read_csv(categories_filepath)
    
    #Merge datasets
    df = messages.merge(categories, how = 'left', on = ['id'])
    
    return df



def clean_data(df):
    
    """Clean the dataframe by removing duplicates & converting categories from string data type to binary type.
    
    Args:
    df: dataframe. Dataframe contains merged content of messages & categories datasets.
       
    Returns:
    df: dataframe. Dataframe contains cleaned version of the input dataframe.
    """
    #Creating a df for individual category
    categories = df['categories'].str.split(';', expand = True)
    
    #Select the first row and get list of categories from this row
    row = categories.iloc[0]
    category_colnames = row.transform(lambda x: x[:-2]).tolist()
    #Renaming columns to categories
    categories.columns = category_colnames
    #Coverting category numbers
    for column in categories:
        #Settting each value to be the last character of the string
        categories[column] = categories[column].transform(lambda x: x[-1:])
        
        #Converting columns from string to numeric
        categories[column] = pd.to_numeric(categories[column])
    
    #Dropping the original categories column from "df" dataframe
    df.drop('categories', axis = 1, inplace = True)
    
    #Concatenating the "df" dataframe with the new "categories" dataframe
    df = pd.concat([df, categories], axis = 1)
    #Dropping duplicates
    df.drop_duplicates(inplace = True)
    #Removing records with value of 2 from "df" table
    df = df[df['related'] != 2]
    
    return df



def save_data(df, database_filename):
    """Save dataset into  SQLite database.
    
    inputs:
    df: dataframe. Dataframe containing cleaned version of merged message and categories data.
    database_filename: string. Filename for output database.
       
    outputs:
    None
    """
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('Messages', engine, index=False, if_exists='replace')
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('Messages', engine, index=False, if_exists='replace')


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages & categories '\
              'datasets as the first & second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()