# Created by vidit.singh at 19-06-2022

def write_sql(df, conn, table):
    print("Writing data into Database")
    for item_df in df:
        min_key = item_df[item_df.columns[0]].min()
        max_key = item_df[item_df.columns[0]].max()
        item_df.to_sql(table, conn, if_exists='append', index=False)  # we don't want to write index of dataframe
        print(f'Loaded data into {table} withing the range of {min_key} and {max_key}')
    print(f'******************** Data loading completed for {table} ********************')
    # This can be used for logging purpose to check if any batch failed.
