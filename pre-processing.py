import pandas as pd

selective_filter = ['Advanced Persistent Threat', 'Advanced persistent threat', 'advanced persistent threat', 'advanced-persistent-threat', 'Advanced-persistent-threat', 'Advanced-Persistent-Threat', 'Advanced and Persistent Threat', 'Advanced and persistent threat', 'advanced and persistent threat','Advanced & Persistent Threat', 'Advanced & persistent threat', 'advanced & persistent threat',
                    'Advanced Persistent Attack', 'Advanced persistent attack', 'advanced persistent attack', 'advanced-persistent-attack', 'Advanced-persistent-attack', 'Advanced-Persistent-Attack', 'Advanced and Persistent Attack', 'Advanced and persistent attack', 'advanced and persistent attack','Advanced & Persistent Attack', 'Advanced & persistent attack', 'advanced & persistent attack',
                    'Advanced Persistent Theory', 'Advanced persistent theory', 'advanced persistent theory', 'advanced-persistent-theory', 'Advanced-persistent-theory', 'Advanced-Persistent-Theory', 'Advanced and Persistent Theory', 'Advanced and persistent theory', 'advanced and persistent theory','Advanced & Persistent Theory', 'Advanced & persistent theory', 'advanced & persistent theory']


for number in range(1, 9):

    print('Query - {}\n'.format(number))

    x = pd.read_csv('Q{}.csv'.format(number), error_bad_lines = False)
    print('Entries after bad lines filteration = {}'.format(len(x)))

    columns = list(x)
    x = x[x['Cited by'] > 0]
    x = x.dropna(subset = ['DOI'])
    print('Entries after cited by filteration = {}'.format(len(x)))

    x = x.reset_index()
    x = x.filter(columns)
    keep_indices = []

    def check(string, sub_str):
        if (string.find(sub_str) == -1):
            return False
        else:
            return True

    for index in range(len(x)):
        abstract = x.iloc[index, 16]
        for item in selective_filter:
            if check(abstract, item) == True:
                if index in keep_indices:
                    pass
                else:
                    keep_indices.append(index)
            else:
                pass

    print('Entries after selective filteration = {}'.format(len(keep_indices)))

    x_updated = x[x.index.isin(keep_indices)]
    x_updated.to_csv('Query{}.csv'.format(number))

q1 = pd.read_csv('Query1.csv')
q2 = pd.read_csv('Query2.csv')
q3 = pd.read_csv('Query3.csv')
q4 = pd.read_csv('Query4.csv')
q5 = pd.read_csv('Query5.csv')
q6 = pd.read_csv('Query6.csv')
q7 = pd.read_csv('Query7.csv')
q8 = pd.read_csv('Query8.csv')

print(len(q1) + len(q2) + len(q3) + len(q4) + len(q5) + len(q6) + len(q7) + len(q8))

data = pd.concat([q1, q2, q3, q4, q5, q6, q7, q8])

data.drop_duplicates(subset = ['DOI'], keep = 'first', inplace = True)
print(len(data))

data = data.reset_index()
del data['Unnamed: 0']

data.to_csv('data.csv')
