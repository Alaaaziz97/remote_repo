import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv('ai_job_dataset.csv') 
df['salary_usd'].hist() 
plt.show() 
