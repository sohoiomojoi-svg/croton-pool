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
- **更新（2026-11-26 社長）：サウナは今後クロトンが自社で仕入れ・販売する** → パンフに「Sauna supply & installation」を掲載、Supplies にチェック。水中LED・掃除ロボットは引き続き載せない
- プールは施工込みが前提（機器単体販売はしない）→ 設備行は「supplied & installed as part of our work」
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
- [x] 正式ロゴ → 社長提供のカラーロゴ（CROTON／Architectural Planning Studio、高解像度2000px）に差し替え。ロゴ枠は白背景＋細い灰色の縁（2026-11-26）
- [x] MasterCard → **Yes** に変更（2026-11-26 社長：決済手段は後から用意して問題なし）。**初受注までにMastercard対応の決済（Square等）を導入すること**
- [x] Business Type に Supplies も追加（2026-11-26 社長）。Capabilities は「Pool equipment supply & installation（ろ過・ポンプ・ヒートポンプ・照明）」に。サウナ等H2O関連は引き続き載せない
- [ ] 出席者 → **社長＋2名（計3名）**で決定。残り2名の人選と、3名分の入力情報・身分証データ準備 → PREP.md の表に記入
- [~] Higa氏へ英語で問い合わせ → **Gmail下書き作成済（未送信）**。締切・ブース寸法・電源・机/クロス・同一グループ2ブース可否・選考結果通知を質問。社長確認後に送信（croton@croton.okinawa から送るなら差出人を切替）
- [~] サイブ株式会社（福岡・上田和憲社長、ACE600の取引先・嘉手納基地への納入実績あり）の水中ロボットを、クロトンのブースで「パートナー商品」として紹介する方針（2026-11-26 社長）。パンフには載せない。上田社長宛の相談メール（商品・問い合わせ窓口・紹介料・英語資料）を**Gmail下書き作成済・宛先未入力**。条件はメールで残す
- [~] Higa氏宛の下書きに「提携先商品の展示可否」の質問を追加済（未送信）
- [x] デジョユ表記 → 英語は **Desjoyaux**（partner.desjoyaux-japan.com より）。About末尾に「Authorized Desjoyaux Japan Partner (Okinawa)」を太字で追加（2026-11-26）
- [~] 許認可番号をパンフに記載（2026-11-26 社長指示）：建設業 No. 12065（般の年次表記は省略）／建築士事務所 Reg. No. 183-2732（2026-08-26 LINE小島さん「R8.3更新で183が正」より。10月の応募書類は133-2732）／宅建 (3) No. 4410。**提出前に許可票で建設業・建築士事務所の番号を確認すること**
- [x] About／Capabilities を社長文案で全面改訂（2026-11-26）：創業2004年・引渡し100件以上・施工管理技士を追加、Desjoyauxは「配管埋設・機械室不要、60年の歴史」。改修・漏水補修／調査の行は削除（塩害訴求はパンフから外れ、当日のトークで補う）。設備に掃除ロボットを追加
- [ ] フォーム提出（**外部送信は社長確認後**）
- [~] 当日準備 → PREP.md に持ち物チェックリスト作成済
- [x] 訴求軸：塩害劣化と補修 → パンフの Capabilities に "salt-damage & corrosion repair" "(salt damage) surveys" を追記、About を "coastal climate" に変更。トーク順は PREP.md

## 参考
- 前回出展企業の参加記：https://hokusei-ta.com/archives/16291（実物を手に取ってもらえたのが収穫、とのこと）
- 前回の公式記事：https://www.kadena.af.mil/News/Display/Article/4424836/
