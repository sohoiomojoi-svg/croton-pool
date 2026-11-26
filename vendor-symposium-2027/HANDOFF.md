# 引き継ぎ：第7回 沖縄ベンダー・シンポジウム出展（クロトン・プール事業）

作成：2026-11-26（チャットのClaudeより）／更新：2026-11-26（Claude Code）

## イベント
- 名称：7th Annual Okinawa Vendor Symposium（主催 18th Contracting Squadron ＋ SAME Japan Post）
- 日時：2027-02-03（水）9:00–14:00
- 会場：The Rocker Club, Kadena AB
- 募集ページ：https://www.samejapan.org/7thokivensym
- 48ブース・選考制。1社最大3名にベースパス。CAGE/SAM.gov/MasterCard 不要
- 申込：ページの「Register Now」→ Googleフォーム（Gmailでサインイン）
  - 入力：氏名、会社名、性別、生年月日、国籍、パスポート発行国、メール、電話
  - 添付：身分証（JPG/PNG/PDF、10MB以下）＋ベンダーパンフレット（ファイル名は英語社名）
- 締切：未公表。前回（2026-03-04開催）は 2026-01-30 締切 or 定員到達まで → 今回は12月末〜1月初旬想定。年内提出が安全
- ブースサイズ・電源：未公表（写真では長机1台＋対面形式）→ Higa氏へ問い合わせ下書き作成済
- 問い合わせ：Narimitsu Higa <narimitsu.higa.1.jp@us.af.mil>、一般 contact@samejapan.org

## 決定事項
- **クロトン単独で出展**（H2Oは出さない）
- 理由：洋平さんの件（株式買取・利益相反の指摘）を刺激しないため。H2Oは建設業許可なし
- サウナ・水中LED・掃除ロボットのH2O→クロトン事業移管は**洋平さんの件が決着するまで保留**（弁護士確認推奨）
- パンフレットはクロトン自身の業務（プール設計施工・改修防水・設備工事・調査・外構）に限定済み

## ファイル（このフォルダ）
- `Croton Co., Ltd..pdf` … 記入済みパンフレット（申込添付用の下書き）
- `2027 Vendor Pamphlet Template.pdf` … 主催者の記入用ひな形（フォームフィールド付き）
- `Symposium Flyer.pdf` … 主催者チラシ
- `fill.py` … パンフレット生成スクリプト（reportlab＋pypdf。テンプレの上に文字を重ね、フォーム部品を削除）
  - 実行：`python3 fill.py "2027 Vendor Pamphlet Template.pdf" "Croton Co., Ltd..pdf"`
  - 先頭の SETTINGS を編集：`MASTERCARD = "yes"/"no"`、`LOGO = "croton_logo.png"`（同フォルダに置けば自動で差し替わる）
  - 長い文字列は枠幅に合わせて自動縮小。一時ファイル不要（どのPCでも実行可）
- `PREP.md` … 申込フォーム入力表・当日持ち物・訴求トーク・保留事項

## 残タスク
- [x] 住所・電話の確認 → 2026-11-18発行請求書（MoneyForward）の記載と一致。〒901-2114 を追記済
- [x] Website URL を記入 → `https://croton.okinawa/poollife/ | https://croton.jp`（メール署名マニュアル記載のもの）。英語ページが無いなら片方に絞るか判断
- [ ] 正式ロゴ画像に差し替え → Drive・GitHubに正式ロゴなし。**社長が後日画像を送る**（届いたら `croton_logo.png` で置いて fill.py 再実行）。届かなければ文字ロゴのまま提出
- [x] MasterCard → **No（空欄のまま）**で決定（2026-11-26 社長）。主催者も不要と明記
- [ ] （任意）サウナ等の追記 → 保留継続（決定事項どおり。パンフには載せていない）
- [ ] 出席者 → **社長＋2名（計3名）**で決定。残り2名の人選と、3名分の入力情報・身分証データ準備 → PREP.md の表に記入
- [~] Higa氏へ英語で問い合わせ → **Gmail下書き作成済（未送信）**。締切・ブース寸法・電源・机/クロス・同一グループ2ブース可否・選考結果通知を質問。社長確認後に送信（croton@croton.okinawa から送るなら差出人を切替）
- [ ] フォーム提出（**外部送信は社長確認後**）
- [~] 当日準備 → PREP.md に持ち物チェックリスト作成済
- [x] 訴求軸：塩害劣化と補修 → パンフの Capabilities に "salt-damage & corrosion repair" "(salt damage) surveys" を追記、About を "coastal climate" に変更。トーク順は PREP.md

## 参考
- 前回出展企業の参加記：https://hokusei-ta.com/archives/16291（実物を手に取ってもらえたのが収穫、とのこと）
- 前回の公式記事：https://www.kadena.af.mil/News/Display/Article/4424836/
