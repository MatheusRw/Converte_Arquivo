import os
import pathlib
import pandas as pd


input_folder = r'C:\Users\matheus.weinert\Nextcloud\SIMCARD_RAW'
output_folder = r'C:\Users\matheus.weinert\Nextcloud\OUTPUT_SIMCARD'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get the list of files in the input folder
file_list = os.listdir(input_folder)

# Perform data transformation and save transformed files in the output folder
for filename in file_list:
    input_file = os.path.join(input_folder, filename)
    output_file_transformed = os.path.join(output_folder, pathlib.Path(filename).stem + '_transformed.csv')

    def find_word_location(df, word):
        for idx, row in df.iterrows():
            for col in df.columns:
                if word in str(row[col]):
                    return idx + 1  # Add 1 to the index to get the line number
        return None  # Return None if the word is not found

    data = pd.read_csv(input_file, encoding='ISO-8859-1', on_bad_lines='skip', header=None)
    df = pd.DataFrame(data)

    word_location = find_word_location(df, 'Var_Out:')
    word_location

    df1 = pd.read_csv(input_file, encoding='ISO-8859-1', on_bad_lines='skip', skiprows=range(word_location+2), header=None)
    df1

    df2 = pd.DataFrame(df1[0].str.split().tolist())
    df2

    df3 = df.iloc[word_location - 1:word_location]
    df3

    df4 = df3.iloc[0].str.replace('Var_Out:', '')
    df4 = df4.replace('/', ' ', regex=True)
    df4 = df4.values[0].split()  # Split the string into a list of column names

    df2.columns = df4  # Assign df4 values as the column names of df2

    #print(df2)
    df2[['ICCID','ADM1']].to_csv(output_file_transformed, index=False)
    print(f'Transformation complete for file: {filename}')

print('All files transformed and saved successfully.')
