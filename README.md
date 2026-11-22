# pyspark-movie-reviews
Basic pyspark processing of the Movie review dataset at https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews?resource=download
# python script
1. Loads csv into pyspark dataframe
2. prints schema and 1st 5 rows
3. removes any rows with null or empty reviews (still contains dupicates)
4. counts total and number of positive/negative reviews
5. adds a review_length column having total number of review characters
6. filters for reviews longer than 500 chars and prints 1st 10
7. saves the cleaned data as new csv under "imdb_output/" folder
# AI disclosure
I used ai as a coding assistant for the project. It helped me with understanding pyspark script and debugging errors. I revieved, ran and tested the code by myself and I understand the working of the code. 
