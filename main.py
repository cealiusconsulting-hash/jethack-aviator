from fasthtml.common import *

# Vercel ke liye: serve() nahi, app export karo
app, rt = fast_app(
    static_path="static",
    hdrs=(
        Meta(name="viewport", content="width=device-width, initial-scale=1.0, maximum-scale=1.0"),
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap"),
        Link(rel="stylesheet", href="/static/style.css"),
    )
)

TELEGRAM_LINK = "https://t.me/+70SR9HYtxb1lZjE1"

def telegram_svg():
    return Svg(
        Path(d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.248l-2.016 9.504c-.148.663-.537.825-1.088.513l-3-2.21-1.447 1.393c-.16.16-.294.294-.603.294l.215-3.053 5.56-5.023c.242-.215-.052-.334-.374-.12L7.287 14.58l-2.95-.922c-.64-.2-.653-.64.135-.948l11.516-4.44c.533-.193 1 .13.574.978z",
               fill="currentColor"),
        viewBox="0 0 24 24", fill="currentColor"
    )

def ticker():
    items = ["aviator hack", "jet hack aviator", "telegram", "expert picks", "live alerts", "daily tips"]
    spans = [Span(Span("◆", cls="d"), f" {item}") for item in items * 2]
    return Div(Div(*spans, cls="ticker-track"), cls="ticker")

def hero_section():
    return Div(
        Div(cls="hero-glow1"),
        Div(cls="hero-glow2"),
        # Badge
        Div(Span(cls="bdot"), " Telegram Channel · Free", cls="badge"),
        # Title + Avatar
        Div(
            Div(
                Span("JET HACK", cls="n1"),
                Span("AVIATOR", cls="n2"),
                cls="big-name"
            ),
            Div(Img(src="/static/logo.jpg", alt="JET HACK AVIATOR Logo"), cls="avatar"),
            cls="title-row"
        ),
        cls="hero-top"
    )

def content_section():
    return Div(
        # Quote
        Div(
            P("Expert signals & daily predictions — premium analysis, insider picks & live alerts straight to your Telegram."),
            cls="quote-block"
        ),
        # Tags
        Div(
            Div(Span(cls="tdot"), " Daily Signals", cls="tag"),
            Div(Span(cls="tdot"), " Expert Picks",  cls="tag"),
            Div(Span(cls="tdot"), " Live Alerts",   cls="tag"),
            cls="tags"
        ),
        # Stat bars
        Div(
            Div(Span("Accuracy",       cls="slabel"), Div(Div(cls="sfill",       style="width:98%"), cls="strack"), Span("98%",  cls="sval"), cls="srow"),
            Div(Span("Daily Signals",  cls="slabel"), Div(Div(cls="sfill sfill2", style="width:86%"), cls="strack"), Span("10+",  cls="sval"), cls="srow"),
            Div(Span("Active Members", cls="slabel"), Div(Div(cls="sfill sfill3", style="width:72%"), cls="strack"), Span("52K+", cls="sval"), cls="srow"),
            cls="stats"
        ),
        # CTA Button
        Div(
            A(telegram_svg(), " ❤️ Join Free Telegram",
              href=TELEGRAM_LINK, target="_blank", rel="noopener", cls="cta"),
            cls="cta-wrap"
        ),
        # Footer row
        Div(
            Div(Span(cls="fmdot"), " Live Members Active", cls="fm"),
            Div("Verified Analyst ✓", cls="fv"),
            cls="foot-row"
        ),
        cls="hero-bottom"
    )

def proof_section():
    win_data = [
        ("✈️", "₹1,24,000+", "Total Winnings"),
        ("🎯", "98%",         "Accuracy"),
        ("🔥", "10x",         "Avg Multiplier"),
        ("👥", "52K+",        "Members"),
    ]
    ss_data = [
        ("₹8,500",  "14.2x", "Today · 2:45 PM"),
        ("₹12,200", "22.5x", "Yesterday · 6:10 PM"),
        ("₹5,750",  "9.8x",  "2 days ago · 11:30 AM"),
    ]
    msg_data = [
        ("RK", "Rahul K.",  "Mumbai", "Bhai aaj ₹4,200 jeeta! Baaba ne sahi signal diya 14x pe. Koi nahi hai is level ka 🔥"),
        ("AS", "Arjun S.",  "Delhi",  "Pehle bahut channels try kiye sab bakwaas the. Jet Hack Baaba real deal hai. ₹9,000 profit ✈️"),
        ("VP", "Vikram P.", "Pune",   "Aaj 22x signal diya baaba ne. ₹12,000 ek baar mein! Sab log join karo 💰"),
    ]

    return Div(
        # Win numbers
        Div("🏆 Baaba Ki Guarantee", cls="proof-label"),
        H2("Real Results", cls="proof-title"),
        Div(*[Div(Div(i,cls="win-icon"), Div(n,cls="win-num"), Div(s,cls="win-sub"), cls="win-card")
              for i,n,s in win_data], cls="win-grid"),

        # Screenshots
        Div("📸 Winning Proofs", cls="proof-label", style="margin-top:28px"),
        Div(*[Div(
                Div(Span("✈️ Aviator",cls="ss-game"), Span("VERIFIED",cls="ss-badge"), cls="ss-top"),
                Div(a, cls="ss-amount"),
                Div("Multiplier: ", B(m), cls="ss-multi"),
                Div(t, cls="ss-time"),
                cls="ss-card") for a,m,t in ss_data], cls="ss-grid"),

        # Messages
        Div("💬 Members Ka Kehna", cls="proof-label", style="margin-top:28px"),
        Div(*[Div(
                Div(av, cls="msg-avatar"),
                Div(
                    Div(nm, Span(lc, cls="msg-loc"), cls="msg-name"),
                    Div(tx, cls="msg-text"),
                    Div("★★★★★", cls="stars"),
                    cls="msg-body"),
                cls="msg-card") for av,nm,lc,tx in msg_data], cls="msg-list"),

        # Final CTA
        Div(
            Div("Aap Kab Tak Wait Karoge?", cls="final-cta-title"),
            Div("52,000+ members pehle se jeet rahe hain", cls="final-cta-sub"),
            A(telegram_svg(), " ❤️ Join Free Telegram",
              href=TELEGRAM_LINK, target="_blank", rel="noopener", cls="cta final-cta-btn"),
            Div("100% Free · No Spam · Instant Access", cls="final-note"),
            cls="final-cta-box"
        ),
        cls="proof-section"
    )

@rt("/")
def get():
    return (
        Title("JET HACK AVIATOR"),
        Div(
            ticker(),
            hero_section(),
            content_section(),
            proof_section(),
            cls="page"
        )
    )

# Local development ke liye
if __name__ == "__main__":
    serve()
