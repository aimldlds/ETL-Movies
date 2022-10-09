#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Import dependencies
import json
import pandas as pd
import numpy as np

# 1. Create a function that takes in three arguments;
# Wikipedia data, Kaggle metadata, and MovieLens rating data (from Kaggle)

def extract_transform_load():
    
    # 2. Read in the kaggle metadata and MovieLens ratings CSV files as Pandas DataFrames.
    kaggle_metadata = pd.read_csv(f'{file_dir}/movies_metadata.csv', low_memory=False)
    ratings = pd.read_csv(f'{file_dir}/ratings.csv',engine='python')
    
    # 3. Open the read the Wikipedia data JSON file.
    with open(f'{file_dir}/wikipedia-movies.json', mode='r') as file:
        wiki_movies_raw = json.load(file)
    
    # 4. Read in the raw wiki movie data as a Pandas DataFrame.
    wiki_movies_df = pd.DataFrame(wiki_movies_raw)
    
    # 5. Return the three DataFrames
    return wiki_movies_df, kaggle_metadata, ratings


# 6 Create the path to your file directory and variables for the three files. 
file_dir = S
# Wikipedia data
wiki_file = f'{file_dir}/wikipedia.movies.json'
# Kaggle metadata
kaggle_file = f'{file_dir}/movies_metadata.csv'
# MovieLens rating data.
ratings_file = f'{file_dir}/ratings.csv'

# 7. Set the three variables in Step 6 equal to the function created in Step 1.
wiki_file, kaggle_file, ratings_file = extract_transform_load()


# In[8]:


# 8. Set the DataFrames from the return statement equal to the file names in Step 6. 
wiki_movies_df = wiki_file
kaggle_metadata = kaggle_file
ratings = ratings_file


# In[9]:


# 9. Check the wiki_movies_df DataFrame.
wiki_movies_df.head()


# In[10]:


# 10. Check the kaggle_metadata DataFrame.
kaggle_metadata.head()


# In[11]:


# 11. Check the ratings DataFrame.
ratings


# In[ ]:




