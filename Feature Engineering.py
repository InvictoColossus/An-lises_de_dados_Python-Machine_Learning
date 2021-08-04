df['pg']=1
df.loc[df.dt_pgto.isnull(),'pg']= 0

df['tempo_pg'] = (df.dt_pgto - df.dt_venda).dt.days

import numpy as np
df['cliente_idade']=np.floor((pd.to_datetime('today')-df.cliente_dt_nasc)/np.timedelta64(1,'Y'))

df


