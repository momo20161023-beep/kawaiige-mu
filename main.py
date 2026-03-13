import os

from dotenv import load_dotenv
from supabase import create_client


def main() -> None:
    # .env を読み込む
    load_dotenv()

    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_PUBLISHABLE_KEY") or os.getenv("SUPABASE_KEY")
    supabase_table_name = os.getenv("SUPABASE_TABLE_NAME")

    if not supabase_url or "your-project-ref" in supabase_url:
        print("SUPABASE_URL が未設定です。.env に本物のURLを入れてください。")
        raise SystemExit(1)

    if not supabase_key or "your_key_here" in supabase_key:
        print(
            "Supabaseキーが未設定です。"
            ".env の SUPABASE_PUBLISHABLE_KEY を本物の値にしてください。"
        )
        raise SystemExit(1)

    if not supabase_table_name:
        print("SUPABASE_TABLE_NAME が未設定です。.env にテーブル名を入れてください。")
        raise SystemExit(1)

    supabase_client = create_client(supabase_url, supabase_key)

    # 指定テーブルの先頭1行を取得
    try:
        res = supabase_client.table(supabase_table_name).select("*").limit(1).execute()
        if res.data:
            print(res.data[0])  # 最初の1行
        else:
            print("データがありません")
    except Exception as error:
        print(f"Supabase接続でエラーが発生しました: {error}")


if __name__ == "__main__":
    main()
