import pandas as pd

# CSVを読み込み
old = pd.read_csv('old_data.csv')
new = pd.read_csv('new_data.csv')

# 品目IDをキーにして比較
old.set_index('品目ID', inplace=True)
new.set_index('品目ID', inplace=True)

# 追加（新にあって旧にない）
added = new.loc[~new.index.isin(old.index)]

# 削除（旧にあって新にない）
removed = old.loc[~old.index.isin(new.index)]

# 修正（共通IDだが内容が違う）
common_ids = old.index.intersection(new.index)
changed = new.loc[common_ids][new.loc[common_ids] != old.loc[common_ids]].dropna(how='all')

# 結果をExcelに出力
with pd.ExcelWriter('差分チェック結果.xlsx') as writer:
    added.to_excel(writer, sheet_name='追加')
    removed.to_excel(writer, sheet_name='削除')
    changed.to_excel(writer, sheet_name='修正')

print("差分チェック完了！")