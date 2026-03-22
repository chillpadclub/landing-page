#!/usr/bin/env python3
"""
entrypoint.py — подставляет переменные из .env в index.template.html,
затем запускает nginx.
"""
import os

TEMPLATE     = "/app/index.template.html"
DEFAULT_LOGO = "/app/logo_default.b64"
OUTPUT       = "/usr/share/nginx/html/index.html"

# ── Логотип ──────────────────────────────────────────────────────────────────
logo_url = os.environ.get("LOGO_URL", "").strip()

if logo_url:
    # Внешняя ссылка — используем как src напрямую
    logo_src = logo_url
    print(f"[entrypoint] лого: внешний URL → {logo_url}")
else:
    # Вшитый base64
    with open(DEFAULT_LOGO, "r") as f:
        logo_src = f.read().strip()
    print("[entrypoint] лого: встроенный (base64)")

# ── Остальные переменные ──────────────────────────────────────────────────────
replacements = {
    "__LOGO_SRC__":      os.environ.get("LOGO_SRC",    	 "https://img.icons8.com/neon/96/penis.png"),
    "__SITE_TITLE__":    os.environ.get("SITE_TITLE",    "BEST VPN"),
    "__SITE_TAGLINE__":  os.environ.get("SITE_TAGLINE",  "VPN №1"),
    "__BOT_URL__":       os.environ.get("BOT_URL",       "https://t.me/your_best_vpn_bot"),
    "__PROXY_SERVER__":  os.environ.get("PROXY_SERVER",  ""),
    "__PROXY_PORT__":    os.environ.get("PROXY_PORT",    ""),
    "__PROXY_SECRET__":  os.environ.get("PROXY_SECRET",  ""),
    "__SUPPORT_URL__":   os.environ.get("SUPPORT_URL",   "https://t.me/your_best_support"),
    "__SHARE_URL__":     os.environ.get("SHARE_URL",     ""),
    "__SHARE_MODE__":    os.environ.get("SHARE_MODE",    "copy"),
    "__REF_PREFIX__":    os.environ.get("REF_PREFIX",    "ref_"),
}

with open(TEMPLATE, "r") as f:
    html = f.read()

for placeholder, value in replacements.items():
    html = html.replace(placeholder, value)

with open(OUTPUT, "w") as f:
    f.write(html)

print("[entrypoint] index.html собран успешно")
print("[entrypoint] запускаю nginx...")
os.execvp("nginx", ["nginx", "-g", "daemon off;"])
