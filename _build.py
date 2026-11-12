# 안원빈 · 우당로 포트폴리오 — 페이지 생성기
# python3 build.py  →  site/ 아래 html 파일을 만든다
import html, json, os

SITE = 'https://portfolio.woodangro.kr/'
OUT = '.'
E = html.escape

LINKS = {
    'insta': 'https://www.instagram.com/woodang_ro/',
    'bean': 'https://www.youtube.com/@BEAN-zq9ng',
    'podbbang': 'https://www.podbbang.com/channels/1793756',
    'book': 'https://woodangro.kr/',
    'indiepub': 'https://indiepub.kr/product/%EC%A3%BC%EB%A8%B9-%EC%A5%94-%EC%86%90%EC%9C%BC%EB%A1%9C-%EC%93%B0%EB%8B%A4%EB%93%AC%EC%A7%80-%EB%AA%BB%ED%95%B4%EC%84%9C/10160/category/88/display/1/',
    'haebang': 'https://www.youtube.com/@%ED%95%B4%EB%B0%A9%EC%9D%BC%EA%B8%B0-g6w',
    'photo': 'https://www.instagram.com/du_wooooooooo',
}
WORKS = [
    dict(slug='book', no='01', kind='책 발간', title='주먹 쥔 손으로 쓰다듬지 못해서',
         desc='첫 소설. 글부터 표지·내지 디자인, 굿즈, 홍보 사이트와 영상까지 혼자 만든 책.',
         roles='집필 + 출판 디자인 + 홍보', pic='img/work/book.jpg'),
    dict(slug='web', no='02', kind='웹 디자인', title='woodangro.kr',
         desc='책을 위한 사이트. 포스터 한 장이 입구가 되고, 카드 · 영화관 · 카세트 · 게임 네 개의 방으로 이어진다.',
         roles='기획 + 디자인 + 개발', pic='img/work/web.jpg'),
    dict(slug='haebang', no='03', kind='인터뷰 · 영상', title='해방일기',
         desc='알코올 중독을 겪은 사람들의 이야기를 인터뷰로 담은 기록. 춘천시중독관리통합지원센터 협업, 8회.',
         roles='기획 + 인터뷰 + 촬영 + 편집', pic='img/work/haebang.jpg'),
    dict(slug='instagram', no='04', kind='연재', title='인스타그램 연재',
         desc='짧은 조각글을 직접 조판해 이미지로 올린 연재. 다섯 편, 41장.',
         roles='글 + 조판', pic='img/work/ig.jpg'),
    dict(slug='etc', no='05', kind='그 밖의 작업', title='기타',
         desc='금천 청년 아트크루 팝업작업실, 팟캐스트 ‘우당로의 기록’, 영상, 매거진, 앨범커버.',
         roles='기획 + 운영 + 제작', pic='img/work/etc.jpg'),
]
FONTS = ('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700'
         '&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans+KR:wght@300;400;500'
         '&family=Noto+Serif+KR:wght@300;600&display=swap')


def head(title, desc, R, path, og='img/og.jpg'):
    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0d0d0c">
<link rel="icon" href="{R}img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{R}assets/site.css">
</head>
<body>
'''


def bar(R, cur):
    work_href = '#work' if cur == 'home' else f'{R}#work'
    wc = ' aria-current="page"' if cur in ('book', 'web', 'haebang', 'instagram', 'etc') else ''
    ac = ' aria-current="page"' if cur == 'about' else ''
    return f'''
<div class="bar" role="navigation" aria-label="사이트 메뉴">
  <a class="seal" href="{R or './'}" aria-label="처음으로"><span class="br">「</span><img src="{R}img/logo-w.png" alt="遇當路" width="66" height="20"><span class="br">」</span></a>
  <nav><a href="{work_href}"{wc}>작업</a><a href="{R}about/"{ac}>소개</a></nav>
  <p class="clock" id="clock" aria-hidden="true"></p>
  <a class="contact" href="{R}about/#contact">연락 →</a>
</div>
'''


def foot(R):
    works = ''.join(f'<li><a href="{R}{w["slug"]}/">{E({"book": "책 발간", "web": "woodangro.kr"}.get(w["slug"], w["title"]))}</a></li>' for w in WORKS)
    return f'''
<footer class="foot rv">
  <div class="ticks" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
  <p class="big" aria-label="우당로"><span class="br">「</span>遇當路<span class="br">」</span></p>
  <div class="cols mono">
    <div><p>[ 작업 ]</p><ul>{works}<li><a href="{R}about/">소개</a></li></ul></div>
    <div><p>[ 링크 ]</p><ul>
      <li><a href="{LINKS["insta"]}" target="_blank" rel="noopener">인스타그램</a></li>
      <li><a href="{LINKS["bean"]}" target="_blank" rel="noopener">유튜브 BEAN</a></li>
      <li><a href="{LINKS["podbbang"]}" target="_blank" rel="noopener">팟빵 우당로</a></li>
      <li><a href="{LINKS["book"]}" target="_blank" rel="noopener">woodangro.kr</a></li>
    </ul></div>
  </div>
  <p class="copy mono"><span>© 2026 안원빈 · 우당로</span><span>감정이 머무는 길, 우연이 당도하는 곳</span></p>
</footer>
'''


def end(R):
    return f'<script src="{R}assets/site.js" defer></script>\n</body>\n</html>\n'


def write(path, s):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or OUT, exist_ok=True)
    open(full, 'w', encoding='utf-8').write(s)


def ext(href, label):
    return f'<a href="{href}" target="_blank" rel="noopener">{label} ↗</a>'


def meta(rows):
    out = ''.join(f'<dt class="mono">{E(k)}</dt><dd>{v}</dd>' for k, v in rows)
    return f'<aside class="p-meta rv"><dl>{out}</dl></aside>'


def phead(R, w, lede):
    return f'''
<header class="p-head">
  <a class="back mono" href="{R}">← 작업 목록</a>
  <p class="kicker mono mute">{w["no"]} — {E(w["kind"])}</p>
  <h1>{E(w["title"])}</h1>
  <p class="lede mono">{E(lede)}</p>
</header>'''


def nextwork(R, slug):
    i = [w['slug'] for w in WORKS].index(slug)
    n = WORKS[(i + 1) % len(WORKS)]
    return f'''
<nav class="next" aria-label="다음 작업">
  <p class="mono mute">다음 작업</p>
  <a href="{R}{n["slug"]}/"><span class="mono mute">{n["no"]} — {E(n["kind"])}</span><span>{E(n["title"])} →</span></a>
</nav>'''


def img(src, alt, R='../', cls='', gallery=None, title='', w=None, h=None, lazy=True):
    size = f' width="{w}" height="{h}"' if w else ''
    tag = f'<img src="{R}{src}" alt="{E(alt)}"{size}{" loading=\"lazy\"" if lazy else ""}{f" class=\"{cls}\"" if cls else ""}>'
    if gallery:
        return f'<button type="button" class="zoomable" data-gallery="{gallery}" data-title="{E(title)}" data-full="{R}{src}" aria-label="{E(alt)} 크게 보기">{tag}</button>'
    return tag


def yt(vid, label, R='../'):
    return (f'<a class="yt" href="https://www.youtube.com/watch?v={vid}" data-id="{vid}" aria-label="{E(label)} 재생">'
            f'<img alt="" loading="lazy"><span class="play mono">재생</span></a>')


# ───────────────────────── 첫 화면 ─────────────────────────
def index():
    R = ''
    cards = ''
    for w in WORKS:
        cards += f'''
    <a class="work rv" href="{w["slug"]}/">
      <span class="no mono">{w["no"]} — {E(w["kind"])}</span>
      <h3>{E(w["title"])}</h3>
      <p class="desc mono">{E(w["desc"])}</p>
      <p class="roles mono">{E(w["roles"])}</p>
      <div class="pic"><img src="{w["pic"]}" alt="" width="1600" height="1200" loading="lazy"><span class="go mono">보기 [+]</span></div>
    </a>'''
    s = head('안원빈 · 우당로 — 포트폴리오',
             '기록자 · 콘텐츠 에디터 안원빈(우당로)의 작업. 첫 소설 『주먹 쥔 손으로 쓰다듬지 못해서』, 인터뷰 프로젝트 ‘해방일기’, 인스타그램 연재.',
             R, '')
    s += bar(R, 'home')
    s += f'''<main>
<header class="hero">
  <p class="ver mono">PORTFOLIO — 2026</p>
  <h1 class="mark" aria-label="우당로"><span class="br">「</span><span class="ch">遇</span><span class="ch">當</span><span class="ch">路</span><span class="br">」</span></h1>
  <div class="frame">
    <div class="ticks" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
    <p class="who mono">기록자 · 콘텐츠 에디터<br>관악, 서울</p>
    <div class="lede">
      <h1>안원빈 <span class="mute">·</span> 우당로</h1>
      <p class="mono">감각을 번역합니다.<br>기획부터 집필, 촬영, 발행까지 혼자 완주해 본 사람입니다.</p>
    </div>
  </div>
  <p class="rule" aria-hidden="true"><i></i></p>
</header>

<section class="works" id="work" aria-labelledby="work-t">
  <div class="sec-label mono"><h2 id="work-t" class="mono" style="margin:0;font-weight:400">[ 작업 ]</h2><span class="mute">{len(WORKS):02d}</span></div>
  <div class="grid3">{cards}
  </div>
</section>

<section class="approach" aria-label="일하는 태도">
  <p class="mono mute">[ 태도 ]</p>
  <p class="big rv">시켜서 만든 것이 아니라 만들고 싶어서 만든 것들이 쌓였습니다. 연재와 팟캐스트, 인터뷰 영상, 그리고 첫 소설까지. 브랜드의 온도를 문장으로 옮기는 일이 제 직무라고 생각합니다.</p>
  <p class="more mono rv"><a href="about/">소개 더 보기 [+]</a></p>
</section>
</main>
'''
    s += foot(R) + end(R)
    write('index.html', s)


# ───────────────────────── 책 발간 ─────────────────────────
def book():
    R = '../'
    w = WORKS[0]
    cards = ''.join(img(f'img/book/card-{k:02d}.jpg', f'연초 카드 No.{k:02d} 앞면', R, gallery='cards', title='연초 카드', w=554, h=784) for k in range(1, 13))
    cards += ''.join(img(f'img/book/cardback-{k:02d}.jpg', f'연초 카드 No.{k:02d} 뒷면', R, gallery='cards', title='연초 카드 · 뒷면', w=554, h=784) for k in (1, 10))
    s = head('주먹 쥔 손으로 쓰다듬지 못해서 — 안원빈 포트폴리오',
             '첫 소설 『주먹 쥔 손으로 쓰다듬지 못해서』(인디펍, 2026). 글부터 표지·내지 디자인, 굿즈, 홍보 사이트와 영상까지 직접 만든 과정.',
             R, 'book/', 'img/work/book.jpg')
    s += bar(R, 'book')
    s += '<main>' + phead(R, w, '첫 소설. 글부터 표지·내지 디자인, 굿즈, 홍보 사이트와 영상까지 혼자 만든 책.')
    s += f'''
<div class="p-body">
{meta([("역할", "집필<br>표지 · 내지 디자인<br>굿즈<br>홍보 사이트 · 영상"), ("출판", "인디펍"), ("출간", "2026. 11. 13"), ("사양", "128×182mm · 208쪽"), ("바로가기", ext(LINKS["book"], "woodangro.kr") + "<br>" + ext(LINKS["indiepub"], "인디펍에서 구매"))])}
<div class="p-main">
  <figure class="rv">{img("img/book/cover-spread.jpg", "『주먹 쥔 손으로 쓰다듬지 못해서』 표지 펼침면", R, "shot", gallery="cover", title="표지 펼침면", lazy=False)}<figcaption class="mono">표지 펼침면 — 날개 · 뒤표지 · 책등 · 앞표지</figcaption></figure>
  <div class="prose rv">
    <p class="first">“사랑은 증거를 남기지만, 증거는 사랑을 증명할 수 없다.” 이 한 문장에서 시작한 첫 소설입니다.</p>
    <p>글을 쓰지 못하던 작가 류가 동네 카페 ‘산호’에서 일하는 지연을 만나면서 이야기가 시작됩니다. 사랑하는 사람들의 관계 자체보다, 관계 이후에 남겨지는 것들과 남겨진 사람들에 대해 쓰고 싶었습니다.</p>
    <p>등단이라는 문을 거치지 않고 독립출판으로 묶었고, 책은 처음부터 끝까지 제 손으로 만들었습니다. 이 책을 위해 인디자인을 처음 배웠고, 표지와 내지를 직접 디자인했습니다.</p>
    <p>글을 쓸 때는 몰랐는데, 책을 만들면서 글은 작품이지만 책은 누군가의 손에 들려야 하는 물건이라는 걸 배웠습니다. 판형과 종이, 글자 크기와 가격까지 고민하면서 비로소 읽는 사람을 생각하게 됐습니다.</p>
  </div>

  <h2 class="sec-label mono" style="font-weight:400"><span>[ 과정 ]</span><span class="mute">07</span></h2>
  <ol class="steps">
    <li class="step rv">
      <header><p class="mono">01</p><h3>한 문장</h3></header>
      <div>
        <div class="txt prose" style="margin:0"><blockquote>“사랑하는 사람과 살고 있다.”</blockquote>
        <p>첫 장에서 류가 이 문장 다음을 쓰지 못합니다. 이 문장은 지워지고, 다른 문장으로 바뀌었다가, 마지막 장의 제목이 되어 돌아옵니다.</p></div>
      </div>
    </li>
    <li class="step rv">
      <header><p class="mono">02</p><h3>내지</h3></header>
      <div>
        <div class="txt"><p>인디자인을 처음 배워 내지를 짰습니다. 부모님 세대와 제 또래가 같은 책을 함께 읽을 수 있도록 본문 글자를 조금 크게, 간격을 넉넉하게 잡았습니다. 내지 파일은 v3부터 v11까지 판을 거듭했습니다.</p></div>
        <div class="row">{img("img/book/sp-ch1.jpg", "차례와 1장 표제지", R, "shot", gallery="spreads", title="내지")}</div>
        <div class="row c2 stack" style="margin-top:12px">{img("img/book/sp-p6.jpg", "1장 첫 본문", R, "shot", gallery="spreads", title="내지")}{img("img/book/sp-19.jpg", "18–19쪽", R, "shot", gallery="spreads", title="내지")}</div>
      </div>
    </li>
    <li class="step rv">
      <header><p class="mono">03</p><h3>메신저 지면</h3></header>
      <div>
        <div class="txt"><p>소설 속 문자메시지는 실제 메신저 화면처럼, 받은 메시지는 왼쪽에 보낸 메시지는 오른쪽에 두었습니다. 읽지 않은 메시지의 ‘1’까지 지면에 옮겨, 답장을 기다리는 시간도 페이지 위에서 읽히게 했습니다.</p></div>
        <div class="row">{img("img/book/sp-msg.jpg", "메신저 화면을 옮긴 156–157쪽", R, "shot", gallery="spreads", title="내지")}</div>
      </div>
    </li>
    <li class="step rv">
      <header><p class="mono">04</p><h3>표지</h3></header>
      <div>
        <div class="txt"><p>꽃다발 이미지를 하얀 실루엣으로 바꾸고, 색과 배치를 여러 번 바꿔 보며 표지를 찾았습니다. 날개와 뒤표지, 책등까지 직접 디자인했습니다.</p></div>
        <div class="row c3">{img("img/book/proc-silhouette.jpg", "꽃 실루엣 작업", R, "", gallery="coverproc", title="표지 과정")}{img("img/book/proc-draft.jpg", "제목을 얹은 초안", R, "", gallery="coverproc", title="표지 과정")}{img("img/book/cover.jpg", "최종 앞표지", R, "", gallery="coverproc", title="표지 과정")}</div>
        <figure style="margin-top:12px">{img("img/book/proc-contact.jpg", "표지와 삽화에 쓴 이미지 모음", R, "", gallery="coverproc", title="표지 과정")}<figcaption class="mono">표지와 삽화에 쓴 이미지 모음</figcaption></figure>
      </div>
    </li>
    <li class="step rv">
      <header><p class="mono">05</p><h3>굿즈</h3></header>
      <div>
        <div class="txt"><p>책 속 열두 장면을 옛 담뱃갑에 들어 있던 카드처럼 옮긴 연초 카드, 소설 속 문장을 담배 모양으로 말아 담은 틴케이스, 낭독 영상으로 이어지는 NFC 키링을 만들었습니다.</p></div>
        <div class="rail cards">{cards}</div><p class="mono mute" style="margin:6px 0 0">연초 카드 12장 · 뒷면에는 그 장면의 본문</p>
        <figure style="margin-top:12px"><div class="row c2 stack">{img("img/book/keyring-sq.jpg", "NFC 키링 속지 (정사각)", R, "", gallery="keyring", title="키링 속지")}{img("img/book/keyring-rect.jpg", "NFC 키링 속지 (직사각)", R, "", gallery="keyring", title="키링 속지")}</div><figcaption class="mono">낭독 NFC 키링 속지 — 반으로 접는 양면</figcaption></figure>
      </div>
    </li>
    <li class="step rv">
      <header><p class="mono">06</p><h3>사이트와 영상</h3></header>
      <div>
        <div class="txt"><p>책 소개 사이트 woodangro.kr를 열고, 신문 지면 같은 지면판, 1장을 스크롤로 읽는 페이지, 심리 테스트, 메신저 게임 ‘읽지 않음’을 붙였습니다. 1장은 영상으로도 옮겼습니다. 사이트는 이후 포스터형으로 새로 만들었습니다 — <a href="{R}web/">woodangro.kr 작업 보기 →</a></p></div>
        <div class="row c2">{img("img/book/site-hero.jpg", "woodangro.kr 첫 화면", R, "shot", gallery="sites", title="woodangro.kr")}{img("img/book/site-zine.jpg", "지면판 zine.woodangro.kr", R, "shot", gallery="sites", title="지면판")}{img("img/book/read-fork.jpg", "1장 미리 읽기", R, "shot", gallery="sites", title="1장 미리 읽기")}{img("img/book/site-more.jpg", "책을 펼치기 전에", R, "shot", gallery="sites", title="woodangro.kr")}{img("img/book/site-test.jpg", "심리 테스트", R, "shot", gallery="sites", title="심리 테스트")}{img("img/book/site-unread.jpg", "읽지 않음", R, "shot", gallery="sites", title="읽지 않음")}</div>
        <figure style="margin-top:12px"><video class="player" src="{R}media/trailer.mp4" poster="{R}media/trailer-poster.jpg" controls preload="none" playsinline></video><figcaption class="mono">1장 예고편 · 49초 · 무음</figcaption></figure>
      </div>
    </li>
    <li class="step rv">
      <header><p class="mono">07</p><h3>출간</h3></header>
      <div>
        <div class="txt"><p>2026년 11월 13일, 인디펍에서 출간했습니다. 같은 날 텍스트힙 북페어 창원(11.13–14)이 열립니다.</p></div>
        <p class="mono">{ext(LINKS["book"], "책 소개 woodangro.kr")} &nbsp; {ext(LINKS["indiepub"], "인디펍")}</p>
      </div>
    </li>
  </ol>
</div>
</div>
'''
    s += nextwork(R, 'book') + '</main>' + foot(R) + end(R)
    write('book/index.html', s)


# ───────────────────────── woodangro.kr ─────────────────────────
def web():
    R = '../'
    w = [x for x in WORKS if x['slug'] == 'web'][0]
    def shot(n, alt):
        return img(f'img/web/{n}.jpg', alt, R, 'shot', gallery='web', title='woodangro.kr')
    s = head('woodangro.kr — 안원빈 포트폴리오',
             '책 『주먹 쥔 손으로 쓰다듬지 못해서』를 위한 사이트 woodangro.kr. 포스터형 메인과 카드·영화관·카세트·게임 네 개의 방을 기획·디자인·개발.',
             R, 'web/', 'img/work/web.jpg')
    s += bar(R, 'web')
    s += '<main>' + phead(R, w, '책을 위한 사이트. 포스터 한 장이 입구가 되고, 네 개의 방으로 이어집니다.')
    mobiles = ''.join(img(f'img/web/m-{n}.jpg', alt, R, 'shot', gallery='webm', title='모바일') for n, alt in
                      [('main', '모바일 메인'), ('card', '모바일 CARD'), ('cinema', '모바일 映畫館'), ('listen', '모바일 LISTEN'), ('game', '모바일 FLASH GAME')])
    s += f"""
<div class="p-body">
{meta([("역할", "기획<br>디자인<br>개발 (HTML · CSS · JS)"), ("기간", "2026. 10. 30 – 11. 12"), ("구성", "메인 + 방 4개<br>1장 미리 읽기 · 심리 테스트 · 읽지 않음"), ("바로가기", ext(LINKS["book"], "woodangro.kr") + "<br>" + ext(LINKS["book"] + "listen/", "LISTEN"))])}
<div class="p-main">
  <figure class="rv">{img("img/web/d-main.jpg", "woodangro.kr 메인 — 포스터", R, "shot", gallery="web", title="woodangro.kr", lazy=False)}<figcaption class="mono">메인 — 흑백 삽화를 빨강·노랑 두 색으로 바꾸고, 영어 · 한자 · 일본어로만 지면을 채웠습니다.</figcaption></figure>
  <div class="prose rv">
    <p class="first">책 소개 페이지로 시작한 사이트가 2주 동안 스물한 번 바뀌었습니다. 마지막에 남은 건 잡지의 한 펼침면 같은 메인입니다.</p>
    <p>메인의 큰 글자들이 곧 문입니다. CARDS를 누르면 연초 카드를 섞는 방, 映畫館을 누르면 낭독 영상을 트는 극장, LISTEN은 카세트 라디오, FLASH GAME은 옛날 컴퓨터로 이어집니다. 설명 대신 장소를 만들고 싶었습니다.</p>
  </div>

  <h2 class="sec-label mono" style="font-weight:400"><span>[ 방 ]</span><span class="mute">04</span></h2>
  <ol class="steps">
    <li class="step rv">
      <header><p class="mono">01</p><h3>CARD · カード</h3></header>
      <div>
        <div class="txt"><p>책 속 열두 장면을 옮긴 연초 카드를 트럼프 카드 위에서 섞습니다. 섞을 때마다 앞판과 겹치지 않는 다섯 장이 펼쳐지고, 한 장을 누르면 그 장면의 본문을 읽을 수 있습니다.</p></div>
        <div class="row c2 stack">{shot("d-card", "CARD — 다섯 장 펼침")}{shot("d-card-read", "CARD — 카드 읽기")}</div>
      </div>
    </li>
    <li class="step rv">
      <header><p class="mono">02</p><h3>映畫館</h3></header>
      <div>
        <div class="txt"><p>극장 사진 속 스크린 자리에 낭독 영상을 겹쳤습니다. 화면 크기가 달라져도 영상이 스크린 밖으로 나가지 않게 맞췄습니다.</p></div>
        <div class="row">{shot("d-cinema", "映畫館 — 낭독 영상 상영관")}</div>
      </div>
    </li>
    <li class="step rv">
      <header><p class="mono">03</p><h3>LISTEN</h3></header>
      <div>
        <div class="txt"><p>노란 카세트는 낭독, 하얀 카세트는 책에서 나온 노래 일곱 곡. 테이프를 라디오에 넣으면 재생됩니다. 흰 바탕에 검정과 노랑, 세 가지 색만 썼습니다.</p></div>
        <div class="row">{shot("d-listen", "LISTEN — 카세트 라디오")}</div>
      </div>
    </li>
    <li class="step rv">
      <header><p class="mono">04</p><h3>FLASH GAME</h3></header>
      <div>
        <div class="txt"><p>옛날 컴퓨터 화면에서 게임을 고르거나, 책상 위 티켓을 모니터에 밀어 넣으면 심리 테스트와 메신저 게임 ‘읽지 않음’으로 넘어갑니다.</p></div>
        <div class="row">{shot("d-game", "FLASH GAME — 게임 선택")}</div>
      </div>
    </li>
  </ol>

  <h2 class="sec-label mono" style="font-weight:400"><span>[ 모바일 ]</span><span class="mute">05</span></h2>
  <div class="rail phones rv">{mobiles}</div>

  <h2 class="sec-label mono" style="font-weight:400"><span>[ 과정 ]</span><span class="mute">21 COMMITS</span></h2>
  <figure class="rv"><video class="player" src="{R}media/web-making.mp4" poster="{R}media/web-making-poster.jpg" controls preload="none" playsinline></video><figcaption class="mono">첫 공개부터 포스터 메인까지 · 30초 · 무음 — 첫 책 소개 페이지, 카세트 라디오, 카지노, 1970년대 빠칭코를 거쳐 지금의 메인으로.</figcaption></figure>
</div>
</div>
"""
    s += nextwork(R, 'web') + '</main>' + foot(R) + end(R)
    write('web/index.html', s)


# ───────────────────────── 해방일기 ─────────────────────────
EPS = [
    ('01', 'qJzbJj1FUGI', '21:15', '마련이', '알라틴, 성인아이, 그리고 알아넌으로 살아가는 ‘마련이’의 이야기'),
    ('02', '7trahGauHIw', '20:14', '마련이', '고마운 나에게, 나를 찾아가는 ‘마련이’의 여정'),
    ('03', 'Dc5gdMI8tTI', '18:17', '백합임', '죽고 싶었던 밤들을 지나, 비로소 죽음을 잘 준비하기까지 (팟캐스트)'),
    ('04', 'KfY3VjXa20M', '21:28', '백합임', '죽고 싶었던 밤들을 지나, 비로소 죽음을 잘 준비하기까지'),
    ('05', 'OWx5TZaEwDQ', '20:29', '물티슈', '알코올 중독자의 자식들이 어떤 고통 속에서 자라는지, 낱낱이 말하고 싶었어요 · 1편'),
    ('06', '5vOzqdFsczY', '23:48', '물티슈', '알코올 중독자의 자식들이 어떤 고통 속에서 자라는지, 낱낱이 말하고 싶었어요 · 2편'),
    ('07', 'vMSKuKwVqK4', '20:36', '이누', '“막상 성인이 되니까, 그 술병이랑 너무 친해져 있더라고요” · 1편'),
    ('08', 'r9468XcXdr8', '23:50', '이누', '“내 인생에서 해방은 죽음이라고 생각했어요” · 2편'),
]


def haebang():
    R = '../'
    w = WORKS[1]
    eps = ''.join(f'''
    <article class="ep rv">{yt(vid, f"해방일기 EP {no}")}
      <p class="t">{E(t)}</p>
      <p class="mono mute">EP {no} · {who} · {dur}</p>
    </article>''' for no, vid, dur, who, t in EPS)
    s = head('해방일기 — 안원빈 포트폴리오',
             '알코올 중독을 겪은 사람들의 이야기를 인터뷰로 담은 기록 프로젝트 ‘해방일기’. 춘천시중독관리통합지원센터 협업, 8회.',
             R, 'haebang/', 'img/work/haebang.jpg')
    s += bar(R, 'haebang')
    s += '<main>' + phead(R, w, '알코올 중독을 겪은 사람들의 이야기를 인터뷰 형식으로 담아내는 기록 프로젝트.')
    s += f'''
<div class="p-body">
{meta([("역할", "기획<br>인터뷰<br>촬영<br>편집"), ("협업", "춘천시중독관리통합지원센터"), ("형식", "팟캐스트 · 유튜브 인터뷰"), ("회차", "EP 01–08"), ("바로가기", ext(LINKS["haebang"], "유튜브 채널"))])}
<div class="p-main">
  <figure class="rv" style="max-width:720px">{img("img/haebang/key.jpg", "해방일기 대표 이미지", R, lazy=False)}</figure>
  <div class="prose rv">
    <p class="first">술 때문에 무너졌던 시간과, 거기서 빠져나오는 시간. 그 이야기를 당사자의 목소리로 남기는 인터뷰 프로젝트입니다.</p>
    <p>춘천시중독관리통합지원센터와 협업해 서포터즈로 참여했고, 기획과 인터뷰, 촬영, 편집을 모두 직접 맡았습니다.</p>
    <p>마련이, 백합임, 물티슈, 이누. 네 사람을 만나 여덟 편으로 엮었습니다.</p>
  </div>
  <h2 class="sec-label mono" style="font-weight:400"><span>[ 회차 ]</span><span class="mute">08</span></h2>
  <div class="eps">{eps}
  </div>
</div>
</div>
'''
    s += nextwork(R, 'haebang') + '</main>' + foot(R) + end(R)
    write('haebang/index.html', s)


# ───────────────────────── 인스타그램 연재 ─────────────────────────
SERIES = [(1, '오른눈', 10), (2, '올해는 기쁜 일이 있으려나', 6), (3, '장마의 형태', 9), (4, '흑백인간', 8), (5, '단편소설', 8)]


def instagram():
    R = '../'
    w = WORKS[2]
    blocks = ''
    for s_, t, n in SERIES:
        imgs = ''.join(img(f'img/ig/s{s_}-{k:02d}.jpg', f'{t} {k}', R, gallery=f's{s_}', title=t, w=560, h=700) for k in range(1, n + 1))
        blocks += f'''
  <section class="series rv" aria-label="{E(t)}">
    <header><h3>{E(t)}</h3><span class="mono mute">{n} CARDS</span></header>
    <div class="rail">{imgs}</div>
  </section>'''
    s = head('인스타그램 연재 — 안원빈 포트폴리오',
             '짧은 조각글을 직접 조판해 이미지로 올린 인스타그램 연재 @woodang_ro. 오른눈, 올해는 기쁜 일이 있으려나, 장마의 형태, 흑백인간, 단편소설.',
             R, 'instagram/', 'img/work/ig.jpg')
    s += bar(R, 'instagram')
    s += '<main>' + phead(R, w, '짧은 조각글을 직접 조판해 이미지로 올린 연재.')
    s += f'''
<div class="p-body">
{meta([("역할", "글<br>조판"), ("채널", "@woodang_ro"), ("연재", "다섯 편 · 41장"), ("바로가기", ext(LINKS["insta"], "인스타그램"))])}
<div class="p-main">
  <div class="prose rv">
    <p class="first">글을 쓰기 시작하면서 ‘우당로’라는 이름으로 인스타그램을 열고, 짧은 조각글을 직접 조판해 이미지로 올렸습니다.</p>
    <p>이 연재에서 쌓인 이야기들이 첫 소설로 이어졌습니다. 카드를 누르면 크게 넘겨 볼 수 있어요.</p>
  </div>
  {blocks}
</div>
</div>
'''
    s += nextwork(R, 'instagram') + '</main>' + foot(R) + end(R)
    write('instagram/index.html', s)


# ───────────────────────── 기타 ─────────────────────────
def etc():
    R = '../'
    w = WORKS[3]
    mag = ''.join(img(f'img/etc/mag-{k:02d}.jpg', f'매거진 작업 {k}', R, gallery='mag', title='매거진 작업', w=560, h=700) for k in range(1, 6))
    s = head('기타 작업 — 안원빈 포트폴리오',
             '금천 청년 아트크루 팝업작업실 기획·운영, 팟캐스트 ‘우당로의 기록’, 유튜브 BEAN 영상, 매거진 작업, 앨범커버 공모전 출품작.',
             R, 'etc/', 'img/work/etc.jpg')
    s += bar(R, 'etc')
    s += '<main>' + phead(R, w, '기획하고 운영하고 만든 것들.')
    s += f'''
<div class="p-body">
{meta([("포함", "금천 청년 아트크루<br>우당로의 기록<br>영상<br>매거진 작업<br>앨범커버")])}
<div class="p-main">
  <section class="block rv" aria-labelledby="b1">
    <header><h2 id="b1">금천 청년 아트크루 · 팝업작업실</h2><span class="mono mute">기획 · 운영</span></header>
    <p class="txt">금천 청년 아트크루 프로젝트에서 팝업작업실을 기획하고 운영했습니다.</p>
    <figure>{yt("g2fWQSvGGXY", "금천 청년 아트크루 프로젝트 성과공유회")}<figcaption class="mono">‘금천 청년 아트크루 프로젝트 : 네트워크 스테이지’ 성과공유회 · 영상 금천문화재단</figcaption></figure>
  </section>

  <section class="block rv" aria-labelledby="b2">
    <header><h2 id="b2">팟캐스트 ‘우당로의 기록’</h2><span class="mono mute">기획 · 대본 · 녹음 · 편집</span></header>
    <p class="txt">글 밖에서 하고 싶은 말을 남기려고 시작한 팟캐스트입니다. 기획부터 대본, 녹음, 편집, 업로드까지 혼자 합니다.</p>
    <ul class="links">
      <li><a href="https://www.podbbang.com/channels/1793756/episodes/25235084" target="_blank" rel="noopener"><span class="mono mute">04</span><span class="t">오늘이라고 부르기로 했다</span><span class="mono mute">팟빵 ↗</span></a></li>
      <li><a href="https://www.podbbang.com/channels/1793756/episodes/25221565" target="_blank" rel="noopener"><span class="mono mute">03</span><span class="t">아직, 잘 모르겠습니다</span><span class="mono mute">팟빵 ↗</span></a></li>
      <li><a href="{LINKS["podbbang"]}" target="_blank" rel="noopener"><span class="mono mute">—</span><span class="t">채널 전체 듣기</span><span class="mono mute">팟빵 ↗</span></a></li>
    </ul>
  </section>

  <section class="block rv" aria-labelledby="b3">
    <header><h2 id="b3">영상</h2><span class="mono mute">유튜브 BEAN</span></header>
    <div class="row c2 stack" style="margin-top:20px">
      <figure>{yt("O-c5wxwpWKc", "동묘")}<figcaption class="mono">동묘</figcaption></figure>
      <figure>{yt("44BUlVw96fA", "파도가 칠때는 서핑을")}<figcaption class="mono">ep.8 파도가 칠때는 서핑을</figcaption></figure>
    </div>
  </section>

  <section class="block rv" aria-labelledby="b4">
    <header><h2 id="b4">매거진 작업</h2><span class="mono mute">5 CARDS</span></header>
    <div class="rail" style="margin-top:20px">{mag}</div>
  </section>

  <section class="block rv" aria-labelledby="b5">
    <header><h2 id="b5">앨범커버</h2><span class="mono mute">공모전 출품작 · @from.1andon</span></header>
    <div style="max-width:480px;margin-top:20px">{img("img/etc/album.jpg", "앨범커버 공모전 출품작", R, gallery="album", title="앨범커버", w=700, h=700)}</div>
  </section>
</div>
</div>
'''
    s += nextwork(R, 'etc') + '</main>' + foot(R) + end(R)
    write('etc/index.html', s)


# ───────────────────────── 소개 ─────────────────────────
def about():
    R = '../'
    s = head('소개 — 안원빈 · 우당로',
             '기록자 · 콘텐츠 에디터 안원빈. 필명 우당로(遇當路). 요리사에서 카페를 거쳐 글을 쓰기까지.',
             R, 'about/', 'img/og.jpg')
    s += bar(R, 'about')
    skills = ['콘텐츠 기획', '카피라이팅', '에세이 · 스토리텔링', '인스타그램 연재 포맷 설계', '릴스 · 카드뉴스 제작', '팟캐스트 기획 · 진행 · 편집', '인터뷰 · 촬영', '촬영 대본 작성', '책 표지 · 내지 디자인 (인디자인)']
    cv = [('주방', '요리학교 졸업, 5성급 호텔 주방 요리사'), ('카페', '카페에서 2년'), ('글', '인스타그램 ‘우당로’ 연재, 글 전시 참여'),
          ('소리', '팟캐스트 ‘우당로의 기록’, 인터뷰 프로젝트 ‘해방일기’'), ('현장', '금천 청년 아트크루 팝업작업실 기획 · 운영'),
          ('책', '2026. 11 첫 소설 『주먹 쥔 손으로 쓰다듬지 못해서』 (인디펍)')]
    s += f'''<main>
<header class="p-head">
  <a class="back mono" href="{R}">← 작업 목록</a>
  <p class="kicker mono mute">소개</p>
  <h1>안원빈</h1>
  <p class="lede mono">기록자 · 콘텐츠 에디터 · 필명 우당로(遇當路)</p>
</header>
<div class="p-body">
<aside class="p-meta rv"><dl><dt class="mono">필명</dt><dd>우당로 遇當路<br><span class="mute">감정이 머무는 길,<br>우연이 당도하는 곳</span></dd><dt class="mono">기반</dt><dd>관악, 서울</dd></dl></aside>
<div class="p-main">
  <div class="about-grid">
    <figure class="rv">{img("img/me.jpg", "안원빈", R, lazy=False, w=784, h=1045)}</figure>
    <div class="prose rv" style="margin:0">
      <p class="first">기획부터 집필, 촬영, 발행까지 혼자 완주해 본 사람입니다.</p>
      <p>5성급 호텔 주방에서 접시 위 소스 한 방울의 위치를 따지던 요리사였고, 어도비 고객지원센터에서 크리에이티브 툴을 쓰는 사람들의 언어를 들으며 만드는 방법에 대해 고민해왔습니다. 그 사이에 시켜서 만든 것이 아니라 만들고 싶어서 만든 것들이 쌓였습니다. 지금은 책을 출간한 한 사람의 문학가로서 활동 중입니다.</p>
      <p>감성 콘텐츠 채널 ‘우당로’ 연재, 팟캐스트 2개 기획·진행, 협업 영상 프로젝트 ‘해방일기’, 글 전시 참여, 그리고 1,000여 편의 기록과 80여 편의 완성 산문. 브랜드의 온도를 문장으로 옮기는 일이 제 직무라고 생각합니다.</p>
      <p>2026년 11월, 첫 소설 『주먹 쥔 손으로 쓰다듬지 못해서』를 독립출판으로 펴냈습니다. 글과 표지, 내지를 모두 직접 만들었습니다.</p>
    </div>
  </div>
  <h2 class="sec-label mono" style="font-weight:400"><span>[ 할 수 있는 일 ]</span></h2>
  <ul class="skills rv">{"".join(f"<li>{E(x)}</li>" for x in skills)}</ul>
  <h2 class="sec-label mono" style="font-weight:400"><span>[ 지나온 길 ]</span></h2>
  <ul class="cv rv">{"".join(f'<li><span class="mono">{E(a)}</span><span>{E(b)}</span></li>' for a, b in cv)}</ul>
  <h2 class="sec-label mono" style="font-weight:400" id="contact"><span>[ 연락 ]</span></h2>
  <ul class="links rv" style="margin-bottom:clamp(60px,9vw,120px)">
    <li><a href="{LINKS["insta"]}" target="_blank" rel="noopener"><span class="mono mute">DM</span><span class="t">인스타그램 @woodang_ro</span><span class="mono mute">↗</span></a></li>
    <li><a href="{LINKS["bean"]}" target="_blank" rel="noopener"><span class="mono mute">YT</span><span class="t">유튜브 BEAN</span><span class="mono mute">↗</span></a></li>
    <li><a href="{LINKS["podbbang"]}" target="_blank" rel="noopener"><span class="mono mute">POD</span><span class="t">팟빵 우당로</span><span class="mono mute">↗</span></a></li>
    <li><a href="{LINKS["book"]}" target="_blank" rel="noopener"><span class="mono mute">BOOK</span><span class="t">책 소개 woodangro.kr</span><span class="mono mute">↗</span></a></li>
  </ul>
</div>
</div>
</main>
'''
    s += foot(R) + end(R)
    write('about/index.html', s)


def extras():
    write('CNAME', 'portfolio.woodangro.kr\n')
    write('.nojekyll', '')
    write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n')
    urls = [''] + [w['slug'] + '/' for w in WORKS] + ['about/']
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + ''.join(f'  <url><loc>{SITE}{u}</loc><lastmod>2026-11-09</lastmod></url>\n' for u in urls) + '</urlset>\n')


for f in (index, book, web, haebang, instagram, etc, about, extras):
    f()
print('built')
