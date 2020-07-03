import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_val = pd.read_csv('CompetenciaECI/Validacion_ECI_2020.csv');
df = pd.read_csv('CompetenciaECI/Entrenamieto_ECI_2020.csv');
y = df['Stage']
print(df.shape)
print(set(df.columns) - set(df_val.columns))
