# CSV差分チェックツール（Python）

SAPのマスタ移行業務で使うことを想定した、旧データと新データのCSV比較ツールです。

## 🔧 使用技術
- Python 3.x
- pandas / openpyxl

## 📂 機能概要
- 品目IDをキーに、以下の差分を抽出
  - 追加されたデータ
  - 削除されたデータ
  - 修正されたデータ（カテゴリなどが変更されたもの）

## 🖥 実行方法

```bash
python3 diff_check.py

📁 出力
	•	差分チェック結果.xlsx（追加 / 削除 / 修正 シート付き）

📌 想定ユースケース
	•	SAPや業務システムのマスタ移行・整備
	•	Excel管理の定期比較、データ監査など

---

## ✅ 作ったら Git に追加してアップロード！

ターミナルで以下を実行👇

```bash
git add README.md
git commit -m "README.md 追加"
git push