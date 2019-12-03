import pandas as pd
import os
import sys



data = pd.read_excel('12864_2016_2684_MOESM1_ESM.xlsx', sheet_name = 'Table S20', skiprows = 2, header = 0, index_col="gene_id")

gene1 = 'IWGSC_CSS_1AL_scaff_1027303.novel_model_1'
gene2 = 'IWGSC_CSS_1AL_scaff_1059868.mRNA.Traes_1AL_5B26F6A14.2'

#print(data.loc[gene1])

gene = sys.argv[1]

print('Expression at 0dpi' ,data.loc[gene]['0dpi'])
print('Expression at 1dpi' ,data.loc[gene]['1dpi'])
print('Expression at 3dpi' ,data.loc[gene]['3dpi'])
print('Expression at 5dpi' ,data.loc[gene]['5dpi'])
print('Expression at 7dpi' ,data.loc[gene]['7dpi'])
print('Expression at 9dpi' ,data.loc[gene]['9dpi'])
print('Expression at 11dpi' ,data.loc[gene]['11dpi'])
