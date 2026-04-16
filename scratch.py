import re

with open('/Users/hiroki/Library/Mobile Documents/com~apple~CloudDocs/プログラミング/プレゼン資料/理事会向け/管理室用タブレット比較/presentation.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 絞り込み理由
content = content.replace('最終的に「REDMI Pad 2 Pro」「Lenovo Idea Tab Plus」「11インチ iPad (A16)」の3機種を',
                          '最終的に「REDMI Pad 2 Pro」「Lenovo Idea Tab Plus」「NEC LAVIE Tab T12N」の3機種を')

# 2. 表のヘッダー
content = content.replace("""                                    <th class="p-4 font-bold border-b border-stone-300 border-l border-white w-1/4 text-teal-800">
                                        <span class="text-teal-800 block text-[10px] uppercase tracking-wider font-bold mb-0.5">Lenovo</span>
                                        Idea Tab Plus
                                    </th>
                                    <th class="p-4 font-bold border-b border-stone-300 border-l border-white w-1/4">
                                        <span class="text-slate-500 block text-[10px] uppercase tracking-wider font-bold mb-0.5">Apple</span>
                                        11インチ iPad <span class="text-xs font-normal">(A16)</span>
                                    </th>""",
                          """                                    <th class="p-4 font-bold border-b border-stone-300 border-l border-white w-1/4">
                                        <span class="text-slate-500 block text-[10px] uppercase tracking-wider font-bold mb-0.5">Lenovo</span>
                                        Idea Tab Plus
                                    </th>
                                    <th class="p-4 font-bold border-b border-stone-300 border-l border-white w-1/4 text-teal-800">
                                        <span class="text-teal-800 block text-[10px] uppercase tracking-wider font-bold mb-0.5">NEC</span>
                                        LAVIE Tab T12N
                                    </th>""")

# 3. 本体価格
content = content.replace("""                                    <td class="p-4 border-l border-stone-100 font-bold text-teal-800 bg-teal-50/30">42,900円～</td>
                                    <td class="p-4 border-l border-stone-100">58,800円～</td>""",
                          """                                    <td class="p-4 border-l border-stone-100">42,900円～</td>
                                    <td class="p-4 border-l border-stone-100 font-bold text-teal-800 bg-teal-50/30">65,780円</td>""")

# 4. 画面 / 解像度
content = content.replace("""                                    <td class="p-4 border-l border-stone-100">12.1インチ<br><span class="text-xs text-slate-400">2560×1600 (90Hz)</span></td>
                                    <td class="p-4 border-l border-stone-100">11インチ<br><span class="text-xs text-slate-400">2360×1640 Liquid Retina</span></td>""",
                          """                                    <td class="p-4 border-l border-stone-100">12.1インチ<br><span class="text-xs text-slate-400">2560×1600 (90Hz)</span></td>
                                    <td class="p-4 border-l border-stone-100">12.1インチ<br><span class="text-xs text-slate-400">2560×1600 (最大800nits高輝度)</span></td>""")

# 5. OS / 処理性能
content = content.replace("""                                    <td class="p-4 border-l border-stone-100">Android 15<br><span class="text-xs text-slate-400">MediaTek Dimensity 6400</span></td>
                                    <td class="p-4 border-l border-stone-100">iPadOS<br><span class="text-xs text-slate-400">Apple A16 Bionic</span></td>""",
                          """                                    <td class="p-4 border-l border-stone-100">Android 15<br><span class="text-xs text-slate-400">MediaTek Dimensity 6400</span></td>
                                    <td class="p-4 border-l border-stone-100">Android 15<br><span class="text-xs text-slate-400">MediaTek Dimensity 6400</span></td>""")

# 6. RAM / ストレージ
content = content.replace("""                                    <td class="p-4 border-l border-stone-100 bg-teal-50/30">
                                        <span class="text-teal-900 font-bold">8GB / 128GB</span><br>
                                        <span class="text-[10px] text-teal-700 font-medium tracking-tight">★マルチタスク性能に余裕</span>
                                    </td>
                                    <td class="p-4 border-l border-stone-100">非公表 / 128GB<br><span class="text-xs text-slate-400">(または 256GB/512GB)</span></td>""",
                          """                                    <td class="p-4 border-l border-stone-100">
                                        <span class="text-slate-700 font-bold">8GB / 128GB</span><br>
                                        <span class="text-[10px] text-slate-500 font-medium tracking-tight">マルチタスクに余裕</span>
                                    </td>
                                    <td class="p-4 border-l border-stone-100 bg-teal-50/30">
                                        <span class="text-teal-900 font-bold">12GB / 256GB</span><br>
                                        <span class="text-[10px] text-teal-700 font-medium tracking-tight">★圧倒的なメモリ容量</span>
                                    </td>""")

# 7. 拡張性 / 重量
content = content.replace("""                                    <td class="p-4 border-l border-stone-100">microSD(最大2TB)<br><span class="text-xs text-slate-400">約530g</span></td>
                                    <td class="p-4 border-l border-stone-100">非対応<br><span class="text-xs text-slate-400">約477g (Wi-Fi)</span></td>""",
                          """                                    <td class="p-4 border-l border-stone-100">microSD(最大2TB)<br><span class="text-xs text-slate-400">約530g</span></td>
                                    <td class="p-4 border-l border-stone-100">microSD(最大2TB)<br><span class="text-xs text-slate-400">約530g</span></td>""")

# 8. バッテリー
content = content.replace("""                                    <td class="p-4 border-l border-stone-100">約11時間(動画再生)</td>
                                    <td class="p-4 border-l border-stone-100">最大10時間(動画/Web)</td>""",
                          """                                    <td class="p-4 border-l border-stone-100">約11時間(動画再生)</td>
                                    <td class="p-4 border-l border-stone-100">約13時間 (10200mAh)</td>""")

# 9. kintoneとの相性
content = content.replace("""                                    <td class="p-4 border-l border-stone-100 text-center bg-teal-50/30">
                                        <span class="text-teal-600 font-bold text-xl">◎</span><br>
                                        <span class="text-[10px] text-teal-800 font-bold mt-1 inline-block">一覧性が高く<br>ショートカット配置も容易</span>
                                    </td>
                                    <td class="p-4 border-l border-stone-100 text-center">
                                        <span class="text-slate-400 font-bold text-xl">○</span><br>
                                        <span class="text-[10px] text-slate-500 mt-1 inline-block">反応速度は良好だが<br>他2機種より画面が狭い</span>
                                    </td>""",
                          """                                    <td class="p-4 border-l border-stone-100 text-center">
                                        <span class="text-teal-600 font-bold text-xl">◎</span><br>
                                        <span class="text-[10px] text-slate-800 font-medium mt-1 inline-block">一覧性が高く<br>ショートカット配置も容易</span>
                                    </td>
                                    <td class="p-4 border-l border-stone-100 text-center bg-teal-50/30">
                                        <span class="text-teal-600 font-bold text-xl">◎</span><br>
                                        <span class="text-[10px] text-teal-800 font-bold mt-1 inline-block">一覧性が高く<br>ペンも活用可能</span>
                                    </td>""")

# 10. キーボード価格
content = content.replace("""                                    <td class="p-4 border-l border-stone-100 bg-teal-50/30">
                                        <span class="text-teal-900 font-bold">8,800円</span><br>
                                        <span class="text-[10px] text-teal-800 font-bold mt-1 inline-block">Idea Tab Plus<br>Folio keyboard (純正)</span>
                                        <div class="mt-1 flex items-center text-[9px] text-teal-700 font-bold">
                                            <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                                            JIS配列・19mm業務仕様
                                        </div>
                                    </td>
                                    <td class="p-4 border-l border-stone-100">
                                        <span class="text-slate-700 font-bold">6,680円</span><br>
                                        <span class="text-[10px] text-slate-500 mt-1 inline-block">Inateck 軽量JIS配列<br>(サードパーティー)</span>
                                    </td>""",
                          """                                    <td class="p-4 border-l border-stone-100">
                                        <span class="text-slate-700 font-bold">8,800円</span><br>
                                        <span class="text-[10px] text-slate-500 mt-1 inline-block">Idea Tab Plus<br>Folio keyboard (純正)</span>
                                        <div class="mt-1 flex items-center text-[9px] text-slate-500">
                                            <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                                            JIS配列・19mm業務仕様
                                        </div>
                                    </td>
                                    <td class="p-4 border-l border-stone-100 bg-teal-50/30">
                                        <span class="text-teal-900 font-bold">0円 (同梱)</span><br>
                                        <span class="text-[10px] text-teal-800 font-bold mt-1 inline-block">スタンド付きキーボード<br>デジタルペン標準付属</span>
                                    </td>""")

# 11. 補足カード
content = content.replace("""                            <p class="text-[11px] text-slate-500 leading-relaxed bg-white p-2 rounded border border-stone-100">
                                <strong class="text-stone-500 font-medium">評価：</strong> 今回比較の要件において、性能・入力性・信頼性のバランスが最も優れており、**「第1推奨」**となります。
                            </p>""",
                          """                            <p class="text-[11px] text-slate-500 leading-relaxed bg-white p-2 rounded border border-stone-100">
                                <strong class="text-stone-500 font-medium">評価：</strong> 性能や入力性のバランスは非常に高いですが、キーボードを別途購入する必要があります。今回は**「第2推奨」**としています。
                            </p>""")

content = content.replace("""                        <article class="bg-stone-50/50 border border-stone-200 rounded-xl p-5 shadow-sm">
                            <div class="text-slate-600 text-sm font-bold flex items-center mb-2">
                                <span class="w-1.5 h-4 bg-stone-300 rounded-full mr-2"></span>
                                iPadの特徴
                            </div>
                            <p class="text-xs text-slate-600 leading-relaxed mb-3">
                                <strong class="text-slate-800">圧倒的な完成度と軽さ：</strong> 重量が約477gと最軽量で、A16 BionicによるOS最適化・動作速度の安定感は3機種中で最高レベルです。
                            </p>
                            <p class="text-[11px] text-slate-500 leading-relaxed bg-white p-2 rounded border border-stone-100">
                                <strong class="text-stone-500 font-medium">評価：</strong> 運用コストとkintone画面の情報量の面で一歩譲りますが、端末の資産価値や安定性を最優先する場合の選択肢です。
                            </p>
                        </article>""",
                          """                        <article class="bg-stone-50/50 border border-stone-200 rounded-xl p-5 shadow-sm border-2 border-teal-600 relative">
                            <div class="absolute -top-3 left-3 bg-teal-700 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-sm">最有力候補</div>
                            <div class="text-teal-800 text-sm font-bold flex items-center mb-2 mt-1">
                                <span class="w-1.5 h-4 bg-teal-600 rounded-full mr-2"></span>
                                NEC LAVIEの特徴
                            </div>
                            <p class="text-xs text-slate-600 leading-relaxed mb-3">
                                <strong class="text-slate-800">業務仕様のフルパッケージ：</strong> スタンド付きキーボードとデジタルペンが標準付属しており、12GBの大容量RAMを搭載。
                            </p>
                            <p class="text-[11px] text-slate-500 leading-relaxed bg-white p-2 rounded border border-stone-100">
                                <strong class="text-teal-700 font-bold">評価：</strong> 本体価格はやや高めですが各種アクセサリが標準付属しており、実質的なコストパフォーマンスが高く**「第1推奨」**となります。
                            </p>
                        </article>""")

# 12. Tab 4
content = content.replace("""                    <p class="text-sm text-teal-900 font-medium">
                        スペック詳細と業務適性を踏まえた結果、<strong class="text-teal-800 font-bold border-b border-teal-700 pb-0.5">Lenovo Idea Tab Plus</strong> が最も業務効率を高める選択肢であると結論づけました。
                    </p>""",
                          """                    <p class="text-sm text-teal-900 font-medium">
                        スペック詳細と業務適性を踏まえた結果、キーボードとペンが標準仕様で同梱される<strong class="text-teal-800 font-bold border-b border-teal-700 pb-0.5">NEC LAVIE Tab T12N</strong> が最も業務効率を高める選択肢であると結論づけました。
                    </p>""")

# 13. Ranking replacement
content = content.replace("""                    <!-- ランキング 1位 (Lenovo: 中央配置・スマホ時一番上) -->
                    <article class="order-first md:order-none bg-white border rounded-2xl smooth-hover flex flex-col relative" style="border: 1px solid #c5a059; box-shadow: 0 10px 30px -10px rgba(197, 160, 89, 0.25);">
                        <div class="absolute -top-3 left-1/2 transform -translate-x-1/2 bg-gradient-to-r from-mutedgold-600 to-amber-500 text-white text-xs font-bold px-4 py-1.5 rounded-full shadow-md tracking-wider">
                            業務用最有力
                        </div>
                        <div class="text-center p-8 flex-grow mt-2">
                            <h4 class="text-slate-500 text-xs tracking-widest mb-2 font-semibold">LENOVO</h4>
                            <h3 class="text-xl font-bold text-slate-800 mb-4">Idea Tab Plus</h3>
                            <div class="mb-2 text-emerald-800 text-[10px] font-bold">業務完結・入力性重視</div>
                            <a href="https://www.lenovo.com/jp/ja/p/tablets/idea-tab-series/lenovo-idea-tab-plus/len103l0033" target="_blank" rel="noopener noreferrer" class="inline-flex items-center px-4 py-1.5 bg-emerald-50 text-emerald-800 border border-emerald-100 text-[10px] font-bold rounded-full mb-5 hover:bg-emerald-100 transition-all active:scale-95 shadow-sm group">
                                公式サイトへ
                                <svg class="w-2.5 h-2.5 ml-1.5 opacity-0 group-hover:opacity-100 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                            </a>
                            <p class="text-sm text-slate-600 leading-relaxed">
                                質の高い専用キーボードによるノートPC同等の運用が可能。現場でのテキスト入力や報告業務において最大の強みを発揮。
                            </p>
                        </div>
                        <div class="bg-stone-50/50 border-t border-stone-100 p-4 rounded-b-2xl">
                            <div class="text-[11px] text-slate-400 mb-1 text-center font-bold tracking-widest">PRACTICAL SCORE</div>
                            <div class="flex justify-center space-x-1 text-teal-700 font-bold tracking-widest text-lg">
                                ★★★★★
                            </div>
                        </div>
                    </article>""",
                          """                    <!-- ランキング 1位 (NEC: 中央配置・スマホ時一番上) -->
                    <article class="order-first md:order-none bg-white border rounded-2xl smooth-hover flex flex-col relative" style="border: 1px solid #c5a059; box-shadow: 0 10px 30px -10px rgba(197, 160, 89, 0.25);">
                        <div class="absolute -top-3 left-1/2 transform -translate-x-1/2 bg-gradient-to-r from-mutedgold-600 to-amber-500 text-white text-xs font-bold px-4 py-1.5 rounded-full shadow-md tracking-wider">
                            業務用最有力
                        </div>
                        <div class="text-center p-8 flex-grow mt-2">
                            <h4 class="text-slate-500 text-xs tracking-widest mb-2 font-semibold">NEC</h4>
                            <h3 class="text-xl font-bold text-slate-800 mb-4">LAVIE Tab T12N</h3>
                            <div class="mb-2 text-emerald-800 text-[10px] font-bold">フルパッケージ・長期運用</div>
                            <a href="https://www.nec-lavie.jp/products/tablet/t12n/?ipromoID=tabletop_newdai_t12n_2602" target="_blank" rel="noopener noreferrer" class="inline-flex items-center px-4 py-1.5 bg-emerald-50 text-emerald-800 border border-emerald-100 text-[10px] font-bold rounded-full mb-5 hover:bg-emerald-100 transition-all active:scale-95 shadow-sm group">
                                公式サイトへ
                                <svg class="w-2.5 h-2.5 ml-1.5 opacity-0 group-hover:opacity-100 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                            </a>
                            <p class="text-sm text-slate-600 leading-relaxed">
                                キーボードとペンが標準同梱され直ちに業務運用が可能。12GBの大容量メモリを備え、長期間快適に稼働できる最適な選択肢です。
                            </p>
                        </div>
                        <div class="bg-stone-50/50 border-t border-stone-100 p-4 rounded-b-2xl">
                            <div class="text-[11px] text-slate-400 mb-1 text-center font-bold tracking-widest">PRACTICAL SCORE</div>
                            <div class="flex justify-center space-x-1 text-teal-700 font-bold tracking-widest text-lg">
                                ★★★★★
                            </div>
                        </div>
                    </article>""")

content = content.replace("""                    <!-- ランキング 3位 (Apple) -->
                    <article class="bg-white text-center border border-stone-200 rounded-2xl smooth-hover flex flex-col relative shadow-delicate">
                        <div class="absolute -top-3 left-1/2 transform -translate-x-1/2 bg-stone-400 text-white text-xs font-medium px-4 py-1.5 rounded-full shadow-md tracking-wider">
                            安定性重視
                        </div>
                        <div class="p-8 flex-grow mt-2">
                            <h4 class="text-slate-500 text-xs tracking-widest mb-2 font-semibold">APPLE</h4>
                            <h3 class="text-xl font-bold text-slate-800 mb-4">11インチ iPad <span class="text-sm font-medium text-slate-500">(A16)</span></h3>
                            <div class="mb-2 text-emerald-800 text-[10px] font-bold">完成度・安定感重視</div>
                            <a href="https://www.apple.com/jp/ipad-11/" target="_blank" rel="noopener noreferrer" class="inline-flex items-center px-4 py-1.5 bg-emerald-50 text-emerald-800 border border-emerald-100 text-[10px] font-bold rounded-full mb-5 hover:bg-emerald-100 transition-all active:scale-95 shadow-sm group">
                                公式サイトへ
                                <svg class="w-2.5 h-2.5 ml-1.5 opacity-0 group-hover:opacity-100 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                            </a>
                            <p class="text-sm text-slate-600 leading-relaxed">
                                業界トップクラスの安定性と完成度。長く使える安心感はあるが、今回の要件に対するコスト面ではやや不利。
                            </p>
                        </div>
                        <div class="bg-stone-50/50 border-t border-stone-100 p-4 rounded-b-2xl">
                            <div class="text-[11px] text-slate-400 mb-1 text-center font-bold tracking-widest">PRACTICAL SCORE</div>
                            <div class="flex justify-center space-x-1 text-slate-500 font-bold tracking-widest text-lg">
                                ★★★☆☆
                            </div>
                        </div>
                    </article>""",
                          """                    <!-- ランキング 3位 (Lenovo) -->
                    <article class="bg-white text-center border border-stone-200 rounded-2xl smooth-hover flex flex-col relative shadow-delicate">
                        <div class="absolute -top-3 left-1/2 transform -translate-x-1/2 bg-stone-400 text-white text-xs font-medium px-4 py-1.5 rounded-full shadow-md tracking-wider">
                            入力性重視
                        </div>
                        <div class="p-8 flex-grow mt-2 text-center">
                            <h4 class="text-slate-500 text-xs tracking-widest mb-2 font-semibold">LENOVO</h4>
                            <h3 class="text-xl font-bold text-slate-800 mb-4">Idea Tab Plus</h3>
                            <div class="mb-2 text-emerald-800 text-[10px] font-bold">業務完結・入力性重視</div>
                            <a href="https://www.lenovo.com/jp/ja/p/tablets/idea-tab-series/lenovo-idea-tab-plus/len103l0033" target="_blank" rel="noopener noreferrer" class="inline-flex items-center px-4 py-1.5 bg-emerald-50 text-emerald-800 border border-emerald-100 text-[10px] font-bold rounded-full mb-5 hover:bg-emerald-100 transition-all active:scale-95 shadow-sm group">
                                公式サイトへ
                                <svg class="w-2.5 h-2.5 ml-1.5 opacity-0 group-hover:opacity-100 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                            </a>
                            <p class="text-sm text-slate-600 leading-relaxed">
                                質の高い専用キーボードによるノートPC同等の運用が可能。キーボード別途購入が必要だが強力な対抗馬。
                            </p>
                        </div>
                        <div class="bg-stone-50/50 border-t border-stone-100 p-4 rounded-b-2xl">
                            <div class="text-[11px] text-slate-400 mb-1 text-center font-bold tracking-widest">PRACTICAL SCORE</div>
                            <div class="flex justify-center space-x-1 text-slate-500 font-bold tracking-widest text-lg">
                                ★★★★☆
                            </div>
                        </div>
                    </article>""")

with open('/Users/hiroki/Library/Mobile Documents/com~apple~CloudDocs/プログラミング/プレゼン資料/理事会向け/管理室用タブレット比較/presentation.html', 'w', encoding='utf-8') as f:
    f.write(content)
