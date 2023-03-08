import pandas
import pathlib
import subprocess
import tqdm

dataframe = pandas.read_csv(pathlib.Path.cwd() / 'csv' / '1.0.1.csv')
for x in tqdm.tqdm(['de', 'en', 'es', 'fr', 'hr']):
    markdown = ''
    for y in dataframe.to_dict('records'):
        if y['format'] == 'h3':
            markdown += '### '+y[x]+'   \n   \n   '
        else:
            markdown += y[x]+'   \n   \n   '
    
    markdown_path = pathlib.Path.cwd() / 'markdown' / f'manual_{x}.md'
    with open(markdown_path, 'w') as save_file:
        save_file.write(markdown)
               
    pdf_path = markdown_path.parents[1] / 'pdf' / f'{markdown_path.stem}.pdf'
    call = ['pandoc', str(markdown_path), '--pdf-engine=xelatex', '-o', str(pdf_path)]
    subprocess.call(call)
