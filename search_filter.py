import pandas as pd
import glob
path = r'*SET PATH HERE*'
all_files = glob.iglob(path + "/*.csv")
r = open('retrieved.csv', 'w+',encoding = 'utf-8', newline = '')
u = open('unretrieved.csv', 'w+', encoding = 'utf-8', newline = '')
writeheader = True
for f in all_files:
        df = pd.read_csv(f, header = 0)
        for i in range(20):
            c = int(len(df.columns))
            if c > 52:
                df = df.drop(df.columns[0], axis = 1)
                print('column dropped!')
                print(len(df.columns))
        df = df[~df['Mention URL'].str.contains('Deleted or', na=False)]
        df1 = df[df['Mention Content'].str.contains('reopen|stay-at-home|lockdown|stay-at-home|safer at home|shutdown|shelter-in-place|restriction|shutdown|#StayHome', na=False)]
        df2 = df[~df['Mention Content'].str.contains('reopen|stay-at-home|lockdown|stay-at-home|safer at home|shutdown|shelter-in-place|restriction|shutdown|#StayHome', na=False)]
        if writeheader == True:
            df1.to_csv(r, header = True, index = False)
            df2.to_csv(u, header = True, index = False)
            writeheader = False
        else:
             df1.to_csv(r, header = False, index = False)
             df2.to_csv(u, header = False, index = False)
