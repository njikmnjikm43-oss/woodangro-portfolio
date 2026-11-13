# 포트폴리오 v2 (遇當路 한 줄의 길) 생성기 — python3 _build_v2.py
import html, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
E = html.escape
HEAD = open('_head.html', encoding='utf-8').read()
TAIL = open('_tail.html', encoding='utf-8').read()

EXTRA_CSS = '''
.g{display:grid;gap:12px;margin-top:18px}
.g2{grid-template-columns:1fr 1fr}.g3{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}.g5{grid-template-columns:repeat(5,1fr)}
.g figure{margin:0}.g figcaption{margin-top:6px}
.g img{width:100%;height:auto;border:1px solid var(--rule);background:#fff}
.quote{margin:18px 0 0;background:var(--card);border-left:3px solid var(--road);padding:20px 24px;font-family:var(--serif);font-size:16px;line-height:1.95;color:#2c2925;max-width:40em}
.quote mark{background:rgba(217,56,30,.14);color:inherit;padding:0 .1em}
.quote s{color:var(--mute)}
.quote .src{display:block;margin-top:10px;font-family:var(--mono);font-size:11.5px;color:var(--mute)}
.count{border-collapse:collapse;margin-top:14px;font-size:14px;min-width:min(420px,100%)}
.count td{border-bottom:1px solid var(--rule);padding:8px 10px 8px 0}
.count td.n{font-family:var(--mono);color:var(--road);text-align:right;padding-right:0}
.persona{display:grid;grid-template-columns:auto 1fr;gap:6px 16px;margin-top:16px;background:var(--card);border:1px solid var(--rule);padding:16px 18px;font-size:14.5px;max-width:36em}
.persona dt{font-family:var(--mono);font-size:11.5px;color:var(--mute);padding-top:2px}
.persona dd{margin:0}
.roles3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:18px}
.roles3.r4{grid-template-columns:repeat(4,1fr)}
.hero.fit{background:#e9e4d8}.hero.fit img{object-fit:contain;padding:3%}
.roles3 div{background:var(--card);border:1px solid var(--rule);padding:16px}
.roles3 b{display:block;font-family:var(--serif);font-size:20px;margin-bottom:4px}
.roles3 span{font-size:13.5px;color:#4a4540;line-height:1.6}
@media (max-width:820px){.g3,.g4,.g5{grid-template-columns:1fr 1fr}.g2{grid-template-columns:1fr}.roles3,.roles3.r4{grid-template-columns:1fr}}
'''


def chk():
    return '<span class="chk">확인</span>'


def fill(label, text, style=''):
    return f'<div class="fill"{style}><p class="mono">{label}</p><p>{text}</p></div>'


def Q(t, src):
    return f'<p class="quote">{t}<span class="src">{src}</span></p>'


def figs(items, cols='g3'):
    out = ''.join(f'<figure><img src="{src}" alt="{E(alt)}" loading="lazy"><figcaption class="mono mute">{E(cap)}</figcaption></figure>' for src, alt, cap in items)
    return f'<div class="g {cols}">{out}</div>'


def step(no, label, h3, sub, body):
    return f'''
    <div class="step">
      <header data-stop="" data-x="-1"><p class="no">{no} — {label}</p><h3>{h3}</h3><p>{sub}</p></header>
      <div class="body">{body}</div>
    </div>'''


def project(n, pid, title, en, hero, hero_alt, ov_q, ov_m, meta, steps, fit=False):
    dl = ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in meta)
    return f'''
<section class="proj" id="{pid}" aria-labelledby="{pid}t">
  <div class="wrap">
    <div class="p-title" data-stop="{n}" data-x="-1"><span class="no">{n}</span><h2 id="{pid}t">{title}</h2><span class="en">{en}</span></div>
    <div class="hero{" fit" if fit else ""}"><img src="{hero}" alt="{E(hero_alt)}" loading="lazy"></div>
    <div class="band">
      <div><h3>OVERVIEW — 질문</h3><p>{ov_q}</p></div>
      <div><h3>OVERVIEW — 만든 것</h3><p>{ov_m}</p></div>
      <dl>{dl}</dl>
    </div>{''.join(steps)}
  </div>
</section>'''


# ───────── 01 해방일기 ─────────
EPS = [
    ('01', 'qJzbJj1FUGI', '21:15', '알라틴, 성인아이, 그리고 알아넌으로 살아가는 ‘마련이’의 이야기'),
    ('02', '7trahGauHIw', '20:14', '고마운 나에게, 나를 찾아가는 ‘마련이’의 여정'),
    ('03', 'Dc5gdMI8tTI', '18:17', '죽고 싶었던 밤들을 지나, 비로소 죽음을 잘 준비하기까지 (팟캐스트)'),
    ('04', 'KfY3VjXa20M', '21:28', '죽고 싶었던 밤들을 지나, 비로소 죽음을 잘 준비하기까지'),
    ('05', 'OWx5TZaEwDQ', '20:29', '알코올 중독자의 자식들이 어떤 고통 속에서 자라는지, 낱낱이 말하고 싶었어요 · 1편'),
    ('06', '5vOzqdFsczY', '23:48', '알코올 중독자의 자식들이 어떤 고통 속에서 자라는지, 낱낱이 말하고 싶었어요 · 2편'),
    ('07', 'vMSKuKwVqK4', '20:36', '“막상 성인이 되니까, 그 술병이랑 너무 친해져 있더라고요” · 1편'),
    ('08', 'r9468XcXdr8', '23:50', '“내 인생에서 해방은 죽음이라고 생각했어요” · 2편'),
]
eps_rows = ''.join(f'<tr><td>EP {n}</td><td><a href="https://www.youtube.com/watch?v={v}" target="_blank" rel="noopener">{E(t)}</a></td><td class="w">{d}</td></tr>' for n, v, d, t in EPS)

P1 = project('01', 'p1', '해방일기', 'HAEBANG DIARY · 2026', 'img/haebang-hero.jpg', '해방일기 유튜브 섬네일 — 고양이와 책, 해가 뜬 바닷가 마을 그림',
    '알코올 중독 가정에서 자란 ‘성인아이’들은 자기 이야기를 어디서, 어떤 속도로 꺼낼 수 있을까. 춘천시중독관리통합지원센터의 ‘해방일기’는 치료적 글쓰기와 말하기로 그 이야기를 마주하는 프로젝트입니다.',
    '중독예방 서포터즈로 참여해 네 사람을 인터뷰하고, 그 이야기를 영상과 팟캐스트 여덟 편으로 편집했습니다. 촬영은 플레인어스와 함께했고, 센터와 강원시청자미디어센터가 제작을 지원했습니다.',
    [('작업기간', '2026. 03 – 11'), ('기여도', '인터뷰 · 편집 단독<br>촬영 공동 (플레인어스)'), ('역할', '인터뷰어 · 편집 연출 · 촬영'), ('프로그램', 'Premiere Pro · Audition<br>Photoshop'), ('결과', '4명 · 8편<br>유튜브 · 팟캐스트 공개')],
    [
        step('01', '질문', '말하기 어려운 이야기', '왜 이 사람들의 이야기였나',
             '<p>알코올 중독 가정에서 자란 네 사람이 카메라 앞에서 자기 이야기를 했습니다. 저는 질문을 하고, 그 이야기가 듣는 사람에게 닿는 형태로 정리하는 역할을 맡았습니다.</p>'
             + '<p>가장 조심한 건 대상자분들의 트라우마를 건드리지 않는 것이었습니다. 제일 어려웠던 건 쓸 단어를 고르는 일이었습니다. 이 사람이 어떤 단어에 민감하게 반응할지 가늠하려고, 인터뷰가 이어지는 한 시간 내내 집중했습니다. 쉬운 보통의 언어에서 시작해 조금 민감한 단어까지, 천천히 선을 알아 갔습니다.</p>'),
        step('02', '기획', '한 편의 구성', '각 편이 같은 순서로 흐르게',
             '<p>구성을 짤 때는 대상자의 편안함만 생각했습니다. 조금이라도 불편할 여지가 보이면 그 상황을 편하게 벗어날 수 있도록, 본 이야기에 들어가기 전에 ‘세이프 워드’를 함께 정했습니다. 한 사람당 두 편씩, 네 사람의 이야기를 담았습니다.</p>'
             '<ol class="flow" aria-label="한 편의 흐름"><li>오프닝</li><li class="arr">→</li><li>자기소개</li><li class="arr">→</li><li class="hi">세이프 워드</li><li class="arr">→</li><li>성인아이로서의 이야기</li><li class="arr">→</li><li>가정 안의 알코올</li></ol>'
             '<div class="people"><div><b>마련이</b><span>EP 01 – 02</span></div><div><b>백합임</b><span>EP 03 – 04</span></div><div><b>물티슈</b><span>EP 05 – 06</span></div><div><b>이누</b><span>EP 07 – 08</span></div></div>'
),
        step('03', '원고', '첫 질문과 가장 어려운 질문', '질문이 분위기를 만든다',
             '<div class="pair"><div><p class="mono" style="color:var(--road);margin:0">첫 질문 — 매번 같은</p>' + Q('요즘의 자신을 사물에 비유하자면, 무엇인가요?', '세이프 워드를 만들고, 근황을 듣기 위한 질문')
             + '<p style="margin-top:12px;font-size:14.5px">사람이 자기 근황을 말할 때 쓰는 문장을 들여다보면 그 사람의 습관이 보입니다. 이 답에서 세이프 워드가 나왔습니다.</p></div>'
             + '<div><p class="mono" style="color:var(--road);margin:0">가장 어려운 질문</p>' + Q('알코올 중독 그 자체, 그리고 과거에 대해 묻는 질문', '본 이야기')
             + '<p style="margin-top:12px;font-size:14.5px">과거를 묻는 일이 가장 어려웠습니다. 그런 대화를 나눌 수 있는 분위기가 만들어질 때까지, 앞의 질문들에 공을 들였습니다.</p></div></div>'),
        step('04', '발행', '여덟 편', '유튜브 ‘해방일기’ 채널 · 팟캐스트',
             f'<table class="eps">{eps_rows}</table>'
             + figs([('img/haebang-hero.jpg', '해방일기 영상 섬네일', '유튜브 섬네일'), ('img/haebang-key.jpg', '해방일기 대표 이미지', '프로젝트 대표 이미지')], 'g2')
             + '<p style="margin-top:18px">대상자분들 모두 고맙다는 말을 전해 주셨습니다. 센터장님과 성인아이 작가님들을 모시고 연 상영회에서는 모두가 울었다고 들었습니다. 인터뷰어이자 편집 연출자로서, 대상자의 진심을 보는 사람에게 전할 수 있어 다행이었습니다. 저를 믿고 이야기해 주신 분들께 감사합니다.</p>'),
    ])

# ───────── 02 책 ─────────
B = '../img/book/'
P2 = project('02', 'p2', '주먹 쥔 손으로 쓰다듬지 못해서', 'FIRST NOVEL · 2026', B + 'cover-spread.jpg', '『주먹 쥔 손으로 쓰다듬지 못해서』 표지 펼침면',
    '함께 산다는 것은 무엇일까. 사랑하는 사람들의 관계 자체보다, 관계 이후에 남겨지는 것들과 남겨진 사람들에 대해 쓰고 싶었습니다.',
    '엇갈리는 네 사람의 시점으로 쓴 첫 소설입니다. 집필부터 퇴고, 표지와 내지 디자인까지 직접 하고 독립출판으로 펴냈습니다. 인디펍 · 2026년 11월 13일 출간.',
    [('작업기간', '2026. 06 초안 · 08 집필<br>출간 2026. 11. 13'), ('기여도', '집필 · 편집 · 디자인 단독<br>유통 인디펍'), ('역할', '작가 · 편집 · 북디자인'), ('프로그램', 'InDesign · Photoshop<br>AI (Claude)'), ('결과', '128×182mm · 208쪽<br>서점 네 곳 유통')],
    [
        step('01', '질문', '한 문장에서', '모든 장면을 재는 기준',
             '<p>원고 전체를 한 문장에 맞춰 재며 썼습니다. 장면을 넣고 뺄 때마다 이 문장을 증명하는지, 흐리는지를 먼저 봤습니다.</p>'
             '<p class="quote">사랑은 증거를 남기지만, 증거는 사랑을 증명할 수 없다.<span class="src">기준 문장</span></p>'
             '<dl class="persona"><dt>기준 독자</dt><dd>27세 · 초등학교 교사. 밥을 차려 두고, 상대가 방으로 들어가는 걸 보는 사람.</dd><dt>쓰임</dt><dd>장면이 이 사람에게 설명 없이 읽히는지로 판단</dd></dl>'),
        step('02', '기획', '네 사람, 엇갈리는 시점', '같은 식탁을 다른 눈으로',
             '<p>작가 류, 카페에서 일하는 지연, 그리고 두 사람 곁의 사람들. 같은 사건을 네 사람이 서로 다른 자리에서 보도록 장을 나눴습니다. 제목도 원고와 함께 바뀌었습니다.</p>'
             '<ol class="flow" aria-label="제목의 변화"><li>흔적을 확인한답시고</li><li class="arr">→</li><li>흔적을 찾는답시고</li><li class="arr">→</li><li class="hi">주먹 쥔 손으로 쓰다듬지 못해서</li></ol>'
             + '<p style="margin-top:14px">이전 제목들은 흔했습니다. 무명 작가가 책을 팔려면 궁금증이 드는 제목이 있어야 한다고 생각했고, 그 생각 아래에서 지금의 제목이 나왔습니다. 시계절 작가님이 제목 짓는 일을 도와주셨습니다.</p>'),
        step('03', '원고', '퇴고의 기준', '초고 약 62,000자 전수 검토',
             '<p>초고를 처음부터 끝까지 검색해, 습관처럼 반복되는 동작 묘사를 세었습니다. 많이 나온 것부터 장면마다 꼭 필요한지 따져 덜어냈습니다.</p>'
             '<table class="count"><tr><td>진동 · 알림이 울린다</td><td class="n">45</td></tr><tr><td>식사 소리 (달그락)</td><td class="n">42</td></tr><tr><td>향이 풍긴다 · 냄새를 맡는다</td><td class="n">31</td></tr><tr><td>웃는다 · 미소</td><td class="n">30</td></tr><tr><td>고개를 끄덕인다</td><td class="n">29</td></tr></table>'
             '<p class="mono mute" style="margin-top:6px">초고 기준 횟수 · 2026. 09</p>'
             + '<div class="pair" style="margin-top:18px"><div><p class="mono" style="color:var(--mute);margin:0">초고 — 「흔적을 찾는답시고」 교정 전</p>' + Q('자리에서 일어나 쓰레기를 버리고 돌아오니 앞자리는 비어있었다. 대신 안방 앞쪽에 화장실 문을 닫는 소리가 들렸다. 이어서 샤워기에서 물이 나오는 소리가 들렸다. <s>갑자기 머리라도 감으려고 하나.</s> 이럴거면 청소 당번을 왜 정했는지.', '1장 · 류') + '</div>'
             + '<div><p class="mono" style="color:var(--road);margin:0">책 — 『주먹 쥔 손으로 쓰다듬지 못해서』 8쪽</p>' + Q('자리에서 일어나 쓰레기를 버리고 돌아오니, 앞자리는 비어 있었다. 대신 안방 쪽의 화장실 문이 닫히는 소리가 울렸고, 이어서 샤워기 물이 나오는 소리가 들렸다. <mark>식탁 위에는 서로 다른 파스타 두 접시만 남겨져 있었다.</mark> 이럴 거면 청소 당번을 왜 정했는지.', '1장 「배부른 줄도 모르고」 · 류') + '</div></div>'
             + '<p style="margin-top:12px;font-size:14.5px">끊어진 문장을 한 호흡으로 잇고, 류의 짐작(“머리라도 감으려고 하나”)을 지웠습니다. 그 자리에 남겨진 두 접시를 놓았습니다. 설명하지 않고, 남은 것만 보이게.</p>'),
        step('04', '발행', '책이라는 물건', '판형 · 내지 · 메신저 지면 · 표지',
             '<p>본문 글자를 조금 크게, 간격을 넉넉하게 잡아 부모님 세대와 제 또래가 같은 책을 읽을 수 있게 했습니다. 소설 속 문자메시지는 실제 메신저 화면처럼, 읽지 않은 ‘1’까지 지면에 옮겼습니다.</p>'
             + figs([(B + 'sp-ch1.jpg', '차례와 1장 표제지', '차례 · 1장 표제지'), (B + 'sp-msg.jpg', '메신저 화면을 옮긴 156–157쪽', '메신저 지면'), (B + 'sp-19.jpg', '18–19쪽', '본문')], 'g3')
             + figs([(B + 'proc-silhouette.jpg', '꽃 실루엣 작업', '표지 — 실루엣'), (B + 'proc-draft.jpg', '제목을 얹은 초안', '표지 — 초안'), (B + 'cover.jpg', '최종 앞표지', '표지 — 최종')], 'g3')
             + '<p style="margin-top:16px">인디펍 · 교보문고 · YES24 · 알라딘에서 판매합니다.</p>'
             + fill('실사 컷 자리', '11. 13–14 텍스트힙 북페어 창원 — 매대 위의 책, 책을 펼친 손님의 손.')),
    ], fit=True)

# ───────── 03 인스타그램 연재 ─────────
SERIES = [(1, '오른눈', 10), (2, '올해는 기쁜 일이 있으려나', 6), (3, '장마의 형태', 9), (4, '흑백인간', 8), (5, '단편소설', 8), (6, '우울은 수용성이래', 1)]
I = '../img/ig/'
P3 = project('03', 'p3', '인스타그램 연재', 'INSTAGRAM SERIES · @woodang_ro', 'img/ig-hero.jpg', '인스타그램 연재 다섯 편의 첫 장',
    '피드를 넘기는 손가락이 멈추는 건 몇 초입니다. 그 안에 짧은 글 한 편을 끝까지 읽히게 하려면 무엇을 줄이고, 무엇을 보여줘야 할까.',
    '‘우당로’라는 이름으로 짧은 조각글을 직접 조판해 이미지로 올렸습니다. 여섯 편, 42장. 이 연재에서 쌓인 이야기들이 첫 소설로 이어졌습니다.',
    [('작업기간', '2025. 08. 05 – 현재'), ('기여도', '글 · 조판 · 운영 단독'), ('역할', '작가 · 에디터 · 채널 운영'), ('프로그램', 'Canva · Photoshop<br>InDesign'), ('결과', '6편 · 42장<br>최고 반응 좋아요 106')],
    [
        step('01', '질문', '몇 초 안에', '피드에서 글이 읽히는 조건',
             '<p>한 편을 여러 장으로 나눠 올렸습니다. 첫 장은 제목을 단 표지이고, 넘길수록 글이 이어집니다.</p>'
             + '<p>지킨 원칙은 하나, 눈에 잘 들어오는 것이었습니다. 책을 조판하면서도 느꼈지만 미감에 정답은 없습니다. 내 눈에 보기 편하게, 그리고 읽을 사람을 정하고 그 사람의 눈에 잘 들어오게. 그게 전부입니다.</p>'),
        step('02', '기획', '여섯 편의 표지', '편마다 다른 얼굴',
             figs([(f'{I}s{s}-01.jpg', t, t) for s, t, n in SERIES], 'g3')),
        step('03', '원고', '한 편을 처음부터 끝까지', '오른눈 · 10장',
             figs([(f'{I}s1-{k:02d}.jpg', f'오른눈 {k}', f'{k:02d}') for k in range(1, 11)], 'g5')
),
        step('04', '발행', '채널', '@woodang_ro',
             '<p>연재는 인스타그램 @woodang_ro에 올렸고, 여기서 쌓인 이야기들이 첫 소설 『주먹 쥔 손으로 쓰다듬지 못해서』로 이어졌습니다.</p>'
             + '<p>가장 반응이 좋았던 글은 2026년 3월 8일에 올린 글입니다. 조회 수 자체는 높지 않았지만 좋아요가 106개 달렸습니다. 많이 보이기보다 보는 사람에게 오래 남은 글이었습니다. — <a href="https://www.instagram.com/woodang_ro/p/DVn5eWmiWPz/" target="_blank" rel="noopener">게시물 보기 →</a></p>'),
    ])

# ───────── 04 우당로의 기록 ─────────
PODEPS = [
    ('첫번째 기록', '처음의 엉망', '2025. 12. 05', '류근 『사랑이 다시 내게 말을 거네』', '첫사랑의 흔적과 처음의 마음'),
    ('두번째 기록', '녹음으로 푸르러진 두번째 기회', '2025. 12. 12', '드라마 『폭싹 속았수다』', '부모님의 겨울 아래에서 자란 푸름'),
    ('세번째 기록', '아직, 잘 모르겠습니다', '2025. 12. 19', '김화진 『우연한 작별, 우연한 작별』', '끝난 뒤에야 시작되는 감정'),
    ('네번째 기록', '오늘이라고 부르기로 했다', '2026. 01. 23', '영화 『에브리씽 에브리웨어 올 앳 원스』', '각본 없는 삶에서 선택을 껴안는 법'),
]
pod_rows = ''.join(f'<tr><td>{a}</td><td>{E(b)}<br><span class="mono mute">{E(src)} · {E(th)}</span></td><td class="w">{d}</td></tr>' for a, b, d, src, th in PODEPS)
P4 = project('04', 'p4', '우당로의 기록', 'PODCAST · 2025 – 2026', 'img/pod-hero.jpg', '팟캐스트 우당로의 기록 1–4화 커버',
    '글 밖에서 하고 싶은 말이 생겼습니다. 혼자 쓰는 글이 아니라, 듣는 사람과 같이 걷는 형식으로 말할 수 있을까.',
    '한 회에 한 문장 — 책이나 드라마, 영화 속 한 문장에 기대어 하나의 감정을 함께 걸어가는 팟캐스트입니다. 기획, 대본, 진행, 녹음, 편집까지 혼자 했습니다.',
    [('작업기간', '2025. 12 – 현재'), ('기여도', '단독'), ('역할', '기획 · 대본 · 진행 · 편집'), ('프로그램', 'Audition · Premiere Pro'), ('결과', '팟빵 · 유튜브 공개')],
    [
        step('01', '질문', '같이 걷는 말', '왜 글이 아니라 목소리였나',
             '<p>글 말고도 저를 보여 주고 싶었습니다. 소설로는 할 수 없는 말들을 하고 싶었습니다.</p>'),
        step('02', '기획', '한 회의 형식', '매회 같은 틀, 다른 문장',
             '<p>모든 회는 같은 틀을 지킵니다. 한 문장을 고르고, 그 문장이 건드리는 감정 하나를 정하고, 같은 인사로 닫습니다.</p>'
             '<ol class="flow" aria-label="한 회의 흐름"><li>한 감정</li><li class="arr">→</li><li class="hi">한 문장</li><li class="arr">→</li><li>함께 걷기</li><li class="arr">→</li><li>듣는 사람에게 묻기</li><li class="arr">→</li><li class="hi">닫는 인사</li></ol>'
             '<p class="quote">감정이 머무는 길, 우연이 당도하는 곳. 오늘도 편안한 산책이 되기를 바랍니다.<span class="src">매회 닫는 인사</span></p>'),
        step('03', '원고', '회차 소개글', '대본의 첫 문장들',
             '<p class="quote">처음은 늘 조금 엉망입니다. 어디서부터 잘못 엉킨 건지도 모르고, 어쩌다 마음이 그렇게 기울어버렸는지 설명하기도 어렵습니다.<span class="src">첫번째 기록 「처음의 엉망」 소개글</span></p>'
             + Q('최근에 이런 말을 봤어요. “고슴도치는 누가 달래 주나?” 생각해 보면 고슴도치는, 그것도 세상을 향해 가시를 잔뜩 세우고 있는 고슴도치를 달래 줄 수 있는 사람은 없습니다.', '「고슴도치는 누가 달래 주나」 대본 도입 · 유튜브 @woodang_ro')),
        step('04', '발행', '기록들', '팟빵 · 유튜브 @woodang_ro',
             f'<table class="eps">{pod_rows}</table>'
             + figs([(f'img/pod-ep{i}.jpg', f'{i}화 커버', f'{i}화 커버') for i in range(1, 5)], 'g4')),
    ])

# ───────── 05 woodangro.kr ─────────
W = '../img/web/'
P5 = project('05', 'p5', 'woodangro.kr', 'BOOK SITE · 2026', W + 'd-main.jpg', 'woodangro.kr 메인 — 포스터',
    '책 소개 페이지는 대부분 한 번 보고 닫힙니다. 책을 읽기 전에, 책 속 장면에 먼저 들어가 머물게 할 수는 없을까.',
    '포스터 한 장을 입구로, 연초 카드를 섞는 방 · 낭독 영화관 · 카세트 라디오 · 게임 네 개의 방을 만들었습니다. 1장 미리 읽기, 심리 테스트, 메신저 게임 ‘읽지 않음’도 책의 문장으로 썼습니다.',
    [('작업기간', '2026. 10. 30 – 11. 12'), ('기여도', '기획 · 글 · 디자인 단독'), ('역할', '콘텐츠 기획 · 웹 디자인'), ('프로그램', 'HTML · CSS · JS<br>AI (Claude)'), ('결과', '방 4개 + 콘텐츠 3종')],
    [
        step('01', '질문', '설명 대신 장소', '책 소개가 아니라 책 속으로',
             '<p>줄거리를 설명하는 대신, 책에 나오는 물건과 장면을 방으로 만들었습니다. 들어온 사람이 무엇을 누를지 스스로 고르게 했습니다.</p>'),
        step('02', '기획', '네 개의 방', '책의 물건 → 사이트의 방',
             '<div class="roles3 r4"><div><b>CARD</b><span>연초 카드 열두 장을 섞어 다섯 장씩. 누르면 그 장면의 본문.</span></div><div><b>映畫館</b><span>극장 스크린에서 낭독 영상 상영.</span></div><div><b>LISTEN</b><span>카세트를 넣으면 낭독과 노래 일곱 곡.</span></div><div><b>GAME</b><span>티켓을 모니터에 넣으면 심리 테스트 · 읽지 않음.</span></div></div>'
             + figs([(W + 'd-card.jpg', 'CARD', 'CARD'), (W + 'd-cinema.jpg', '映畫館', '映畫館'), (W + 'd-listen.jpg', 'LISTEN', 'LISTEN'), (W + 'd-game.jpg', 'FLASH GAME', 'FLASH GAME')], 'g2')),
        step('03', '지면', '흑백의 책, 원색의 사이트', '왜 이 색이었나',
             '<p>책의 삽화와 굿즈는 전부 흑백입니다. 그래서 그 책을 알리는 홈페이지만큼은 더 많은 색과 강한 인상을 주고 싶었습니다. 빨강 · 노랑 · 파랑 · 검정 네 가지 면으로 지면을 나누고, 흑백 삽화 한 장을 두 가지 색으로 바꿔 메인에 놓았습니다.</p>'),
        step('04', '발행', '공개', '첫 공개부터 지금까지',
             '<p>10월 30일 첫 공개 이후 카세트 라디오, 카지노, 1970년대 빠칭코를 거쳐 지금의 포스터 메인이 됐습니다.</p>'
             '<figure style="margin:16px 0 0"><video src="../media/web-making.mp4" poster="../media/web-making-poster.jpg" controls preload="none" playsinline style="width:100%;background:#000"></video><figcaption class="mono mute" style="margin-top:6px">과정 영상 · 30초 · 무음</figcaption></figure>'
),
    ])

# ───────── 06 굿즈 세트 ─────────
P6 = project('06', 'p6', '굿즈 세트', 'OBJECTS · 2026', 'img/goods-set.jpg', '틴케이스와 연초 카드, 낭독 NFC 키링 목업',
    '책을 덮은 뒤에도 문장이 손에 남을 수 있을까. 읽는 사람이 책 밖으로 가져갈 수 있는 물건을 만들고 싶었습니다.',
    '책 속 열두 장면을 옮긴 연초 카드와 그 카드를 담는 틴케이스, 휴대폰을 대면 낭독이 재생되는 NFC 키링, 그리고 스티커. 물건마다 책의 장면 · 문장 · 목소리를 하나씩 맡습니다.',
    [('작업기간', '2026. 10 – 11'), ('기여도', '기획 · 문안 · 디자인 단독'), ('역할', '기획 · 에디터 · 디자인'), ('프로그램', 'InDesign · Photoshop<br>AI (목업)'), ('결과', '카드 12종 · 틴케이스<br>키링 · 스티커')],
    [
        step('01', '질문', '책 밖의 문장', '물건이 맡는 역할',
             '<div class="roles3"><div><b>장면</b><span>연초 카드 — 옛 담뱃갑 속 카드처럼, 앞면엔 그림과 한 줄, 뒷면엔 그 장면의 본문.</span></div><div><b>문장</b><span>틴케이스 — 소설 속 문장을 담배 모양으로 말아 담았습니다.</span></div><div><b>목소리</b><span>NFC 키링 — 휴대폰을 대면 낭독이 바로 재생됩니다.</span></div></div>'),
        step('02', '기획', '연초 카드 열두 장', '앞면 한 줄 · 뒷면 본문',
             figs([('../img/goods/tin-hand.jpg', '틴케이스에서 연초 카드를 꺼내는 손', '틴케이스 속 연초 카드'), ('../img/goods/set-flatlay.jpg', '틴케이스, 봉투, 카드, 스티커를 펼친 구성', '구성 — 틴케이스 · 봉투 · 카드 · 스티커')], 'g2')
             + figs([(B + f'card-{k:02d}.jpg', f'연초 카드 No.{k:02d}', f'No.{k:02d}') for k in (1, 4, 6, 9, 12)], 'g5')
             + figs([(B + 'cardback-01.jpg', '연초 카드 No.01 뒷면', 'No.01 뒷면 — 1장 본문'), (B + 'cardback-10.jpg', '연초 카드 No.10 뒷면', 'No.10 뒷면')], 'g4')),
        step('03', '원고', '낭독이 재생되는 키링', '들고 다니는 목소리',
             '<p>대면 소리가 나는 물건. 키링 속지는 반으로 접는 양면입니다.</p>'
             + figs([('../img/goods/keyring-bag.jpg', '에코백에 단 낭독 NFC 키링', '가방에 단 키링'), ('../img/goods/keyring-open.jpg', '양쪽으로 펼친 키링 속지', '펼친 키링 — 양면 속지')], 'g2')
             + '<p style="margin-top:14px">휴대폰을 대면 woodangro.kr/listen 으로 이어집니다. 낭독한 장면은 제가 이 책에서 가장 좋아하는 장면입니다. 지연이 자기 이야기를 드러내는 장면, 그 결핍을 드러냄으로써 류가 지연에게 끌리게 되는 장면입니다.</p>'),
        step('04', '발행', '세트로 놓이다', '스티커 · 북페어 매대',
             '<p>노트북이나 다이어리에 붙이는 스티커로, 우당로 로고와 책 속 꽃다발, 고양이를 옮겼습니다.</p>'
             + figs([('../img/goods/sticker.jpg', '노트북에 붙인 우당로 · 고양이 · 꽃다발 스티커', '스티커 — 遇當路 · 고양이 · 꽃다발')], 'g2" style="grid-template-columns:1fr')
             + '<p class="mono mute" style="margin-top:8px">위 사진은 목업입니다.</p>'
             + fill('실사 컷 자리', '11. 13–14 북페어 — 책 · 카드 · 키링이 함께 놓인 매대, 손님이 키링에 휴대폰을 대는 순간 (영상 5초면 충분).')
),
    ])

# ───────── 07 tooo00o_ ─────────
T = '../media/tooo/'
def vid(name, cap, style=''):
    return f'<figure style="margin:0{style}"><video src="{T}{name}.mp4" poster="{T}{name}.jpg" controls preload="none" playsinline muted loop style="width:100%;display:block;background:#000"></video><figcaption class="mono mute" style="margin-top:6px">{cap}</figcaption></figure>'
P7 = project('07', 'p7', 'tooo00o_', 'AI FILM CHANNEL · 2026', 'img/tooo-hero.jpg', 'tooo00o_ 영상 C06 — 흐린 하늘 아래 들판에서 흰 옷을 입고 춤추는 사람',
    '글로 쓰던 장면을 움직이는 이미지로 옮길 수 있을까. 이야기가 있는 단편영화처럼, 몇십 초 안에 하나의 장면이 남는 영상을 만들고 싶었습니다.',
    'Higgsfield(AI)로 만드는 영상 채널 @tooo00o_ 입니다. 시네마틱 · 예술 뮤직비디오를 중심으로, 기획부터 연출과 편집까지 혼자 합니다.',
    [('작업기간', '2026. 11 – 현재'), ('기여도', '단독'), ('역할', '기획 · 연출 · 편집'), ('프로그램', 'Higgsfield (AI)'), ('결과', '영상 3편<br>인스타그램 @tooo00o_')],
    [
        step('01', '기획', '세 갈래의 영상', '무엇이 주인공인가',
             '<div class="roles3"><div><b>서사</b><span>짧아도 시작과 끝이 있는 이야기.</span></div><div><b>상징 · 이미지</b><span>한 장면, 한 문장이 남는 영상.</span></div><div><b>공간 · 분위기</b><span>장소와 공기가 주인공인 영상.</span></div></div>'),
        step('02', '작업', '세 편', '16:9 두 편 · 9:16 한 편',
             '<div class="g g2">' + vid('the_artist_is_present_homage', 'The Artist Is Present — 오마주 · 25초') + vid('tooo_c06_169_long_bw', 'C06 — 흑백 · 20초') + '</div>'
             + '<div class="g g3">' + vid('tooo_strobe_color_v3', 'N°001 — “It was clear, so no one noticed.” · 15초') + '</div>'
             + '<p style="margin-top:14px"><a href="https://www.instagram.com/tooo00o_/" target="_blank" rel="noopener">인스타그램 @tooo00o_ →</a></p>'),
    ])

TOC = [('p1', '01', '해방일기', '인터뷰 · 편집 · 촬영'), ('p2', '02', '주먹 쥔 손으로 쓰다듬지 못해서', '집필 · 편집 · 출판'),
       ('p3', '03', '인스타그램 연재', '글 · 조판 · 채널 운영'), ('p4', '04', '우당로의 기록', '팟캐스트 기획 · 진행 · 편집'),
       ('p5', '05', 'woodangro.kr', '콘텐츠 기획 · 웹'), ('p6', '06', '굿즈 세트', '텍스트를 물건으로'), ('p7', '07', 'tooo00o_', 'AI 영상 · 기획 · 연출')]
toc = ''.join(f'<li><a href="#{a}"><span class="no">{n}</span><span class="t">{E(t)}</span><span class="r">{E(r)}</span></a></li>' for a, n, t, r in TOC)

BODY = f'''<main>
<section class="cover" aria-label="표지">
  <div class="wrap" style="display:contents">
    <div class="wrap top mono"><span>PORTFOLIO — 2026</span><span>CONTENT EDITOR</span></div>
    <div class="wrap mid">
      <h1 class="kanji" aria-label="우당로"><span>遇</span><span>當</span><span class="r">路</span></h1>
      <p class="sub"><b>안원빈 · 우당로</b><span class="mono mute">우연이 당도하는 길 — A ROAD WHERE CHANCE ARRIVES</span></p>
    </div>
    <div class="wrap bottom mono"><span>기록자 · 콘텐츠 에디터<br>관악, 서울</span><span style="text-align:right">한 줄의 길을 따라<br>일곱 개의 정류장 ↓</span></div>
  </div>
  <span class="start" data-stop="出發" data-x=".5"></span>
</section>

<section class="intro" aria-label="인트로">
  <div class="wrap">
    <p class="big" data-stop="" data-x="-1">감각을 <em>번역</em>합니다.</p>
    <p class="s">기획부터 집필, 촬영, 발행까지 혼자 완주해 본 사람입니다. 사람의 이야기를 듣고, 그 이야기가 가장 잘 읽히는 형식을 찾아 끝까지 내보내는 일을 합니다.</p>
  </div>
</section>

<section class="toc" aria-label="목차">
  <div class="wrap">
    <div class="label mono"><span>[ 정류장 ]</span><span>07</span></div>
    <ol>{toc}</ol>
  </div>
</section>
{P1}{P2}{P3}{P4}{P5}{P6}{P7}

<section class="end" aria-label="끝">
  <div class="wrap">
    <div class="arrive" data-stop="到着" data-x=".5"></div>
    <h2>THANK YOU</h2>
    <p>같은 길을 여기까지 걸어 주셔서 고맙습니다.</p>
    <div class="links mono">
      <a href="https://www.instagram.com/woodang_ro/" target="_blank" rel="noopener">INSTAGRAM @woodang_ro</a>
      <a href="https://woodangro.kr/" target="_blank" rel="noopener">WOODANGRO.KR</a>
      <a href="https://www.instagram.com/tooo00o_/" target="_blank" rel="noopener">INSTAGRAM @tooo00o_</a>
      <a href="https://www.youtube.com/@BEAN-zq9ng" target="_blank" rel="noopener">YOUTUBE BEAN</a>
      <a href="https://www.podbbang.com/channels/1793756" target="_blank" rel="noopener">PODBBANG 우당로의 기록</a>
    </div>
  </div>
</section>
</main>
'''

head = HEAD.replace('</style>', EXTRA_CSS + '</style>')
tail = TAIL.replace('시안 v2 · 01 해방일기만', '시안 v2 · 빨간 점선 = 채울 자리')
open('index.html', 'w', encoding='utf-8').write(head + BODY + tail)
print('built v2')
