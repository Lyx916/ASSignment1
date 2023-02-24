import sys
contact_info_file= sys.argv[1]
other_info_file=sys.argv[2]
output_file=sys.argv[3]

import numpy
import pandas
import pandas as pd

df_contact=pd.read_csv(contact_info_file)
df_other=pd.read_csv(other_info_file)

df=pd.merge(df_contact,df_other, left_on="respondent_id", right_on="id").drop('id',axis=1)

df1=df.dropna(axis=0,how='any')

mask=df1['job'].str.contains('insurance',case=False,regex=False)
df2=df1[~mask]

print(df2.shape)

df2.to_csv(output_file,index=False)

