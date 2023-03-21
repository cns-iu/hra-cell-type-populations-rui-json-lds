import pandas as pd
def build_local_csv_from_gsheet(doc_id, sheet_id,filename):
    url = f'https://docs.google.com/spreadsheets/d/{doc_id}/export?format=csv&gid={sheet_id}'
    df = pd.read_csv(url)
    df.to_csv(filename)
