import os

from dotenv import load_dotenv
from supabase import create_client

# .env を読み込む
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_PUBLISHABLE_KEY") or os.getenv("SUPABASE_KEY")
SUPABASE_TABLE_NAME = os.getenv("SUPABASE_TABLE_NAME")

if not SUPABASE_URL or "your-project-ref" in SUPABASE_URL:
    print("SUPABASE_URL が未設定です。.env に本物のURLを入れてください。")
    raise SystemExit(1)

if not SUPABASE_KEY or "your_key_here" in SUPABASE_KEY:
    print(
        "Supabaseキーが未設定です。"
        ".env の SUPABASE_PUBLISHABLE_KEY を本物の値にしてください。"
    )
    raise SystemExit(1)

if not SUPABASE_TABLE_NAME:
    print("SUPABASE_TABLE_NAME が未設定です。.env にテーブル名を入れてください。")
    raise SystemExit(1)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# 指定テーブルの先頭1行を取得
try:
    res = supabase.table(SUPABASE_TABLE_NAME).select("*").limit(1).execute()
    if res.data:
        print(res.data[0])  # 最初の1行
    else:
        print("データがありません")
except Exception as error:
    print(f"Supabase接続でエラーが発生しました: {error}")
