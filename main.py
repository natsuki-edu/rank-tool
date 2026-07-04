import os
from nicegui import ui

A_RANK_PLUS2_GSCORE = 18200

# まずは関数を定義しておく
def calc_support_point(gift_score):
    support_point = gift_score * 3.1
    return round(support_point)

def is_plus2_rank(gift_score):
    if gift_score >= A_RANK_PLUS2_GSCORE:
        return True
    else:
        return False

# +2かどうかを判定する関数を定義しておく
def check_plus2_rank():
    gift_score = int(gift_score_input.value)  # 入力欄の値を取得
    support_point = calc_support_point(gift_score)

    if is_plus2_rank(gift_score):
        support_point_label.text = f"応援ポイント: {support_point:,} ➡ ❣+2達成❣"
    else:
        support_point_label.text = f"応援ポイント: {support_point:,} ➡ +1は確保💦"

# ページ全体の背景色を設定する
ui.query("body").style("background-color: #e6e6fa")

# カードで中央寄せのレイアウトを作る
with ui.card().style(
    "width: 400px; margin: 80px auto; padding: 32px;"
    "border-radius: 20px; background-color: #fff6f8;"
    "box-shadow: 0 4px 20px rgba(255,182,193,0.4);"
):
    # タイトル
    ui.label("REALITY｜A帯+2判定ツール❣").style(
        "font-size: 20px; font-weight: bold; color: #ffb6c1;"
        "text-align: center; width: 100%; margin-bottom: 8px;"
    )

    # 入力欄を作る
    # .props()で属性(入力欄の種類や色合い等)を追加できる
    gift_score_input = ui.input(label="ギフトスコアを入力してください").props(
        "type=number color=pink"
    ).style(
        "background-color: #ffe4ec; border-radius: 8px; width: 100%;"
    )

    # ボタンを押すと結果をラベルに表示する
    ui.button("判定する 🌸", on_click=check_plus2_rank).props(
        "unelevated rounded"
    ).style(
        "width: 100%; margin-top: 16px; font-weight: bold;"
        "background-color: #dda0dd !important; color: #6b21a8 !important;"
    )

    # 最終結果を表示するラベル
    support_point_label = ui.label("結果: ").style(
        "margin-top: 16px; font-size: 15px; color: #ffa500;"
        "text-align: center; width: 100%;"
    )

# NiceGUIの画面を起動する
port = int(os.environ.get("PORT", 8080))

ui.run(
    title="REALITY｜A帯+2判定ツール",
    host="0.0.0.0",
    port=port,
    reload=False,
)
