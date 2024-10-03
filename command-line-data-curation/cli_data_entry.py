from rich.console import Console
from rich.table import Table
import pandas as pd
import os

console = Console()
console.print("24-25 Season so far for Arsenal:", style = "red")

table = Table(title="24-25 Season Arsenal")

table.add_column('Date')
table.add_column('Opponent')
table.add_column('Result')
table.add_row('24/08/17', 'Wolves', '2-0')
table.add_row('24/08/24', 'Aston Villa', '2-0')
table.add_row('24/08/31', 'Brighton', '1-1')
table.add_row('24/09/15', 'Tottenham', '1-0')
table.add_row('24/09/22', 'Man City', '2-2')
table.add_row('24/09/28', 'Leicester', '4-2')
data = [
    ['24/08/17', 'Wolves', '2-0'],
    ['24/08/24', 'Aston Villa', '2-0'],
    ['24/08/31', 'Brighton', '1-1'],
    ['24/09/15', 'Tottenham', '1-0'],
    ['24/09/22', 'Man City', '2-2'],
    ['24/09/28', 'Leicester', '4-2'],
]
console.print('\n[bold cyan]I want you to enter your score prediction for the next couple games![/bold cyan]')

while True:
    console.print(table)
    console.print('Type "N" if you are done putting the prediction!')
    date = input('Enter the match date:')
    if(date == 'N'):
        break
    opponent = input("Enter the opponent:")
    score = input('Enter the score prediction:')
    try:
        flag = True
        while flag:
            console.print('Is the entry correct?')
            table2 = Table(title="24-25 Season Arsenal")
            table2.add_column('Date')
            table2.add_column('Opponent')
            table2.add_column('Result')
            table2.add_row(date, opponent, score)
            console.print(table2)
            check = input('Type "Y" to confirm the data. If you want to fix, type R:')
            flag = (check != 'Y')
            if(flag):
                console.print('Re-enter data.')
                date = input('Enter the match date:')
                opponent = input("Enter the opponent:")
                score = input('Enter the score prediction:')
        table.add_row(date, opponent, score)
        data.append([date, opponent, score])
    except:
        console.print('Error!')
        break
    
console.print('Saving the table to a file...')
df = pd.DataFrame(data, columns=["Date", "Opponent", "Result"])
df.to_csv('arsenal_season.csv', index=False)
console.print(f'Data saved to {os.path.abspath("arsenal_season.csv")}')
