# Landing Page

## Быстрый старт

```bash
# 1. Редактируй конфиг
nano .env

# 2. Запускай
docker compose up -d --build
```

## Все переменные .env

| Переменная      | Описание                                              | Пример                                       |
|-----------------|-------------------------------------------------------|----------------------------------------------|
| `SITE_TITLE`    | Заголовок на странице                                 | `BEST VPN`                                   |
| `SITE_TAGLINE`  | Подзаголовок под лого                                 | `VPN #1`                                     |
| `LOGO_URL=`     | Подзаголовок под лого                                 | `https://img.icons8.com/quill/100/penis.png` |
| `HOST_PORT`     | Порт на хосте для реверс-прокси                       | `8080`                                       |
| `BOT_URL`       | Ссылка на Telegram-бот                                | `https://t.me/your_best_vpn_bot`             |
| `REF_PREFIX`    | Префикс для ?start=                                   | `ref_`                                       |
| `PROXY_SERVER`  | Сервер MTProto-прокси                                 | `your.domain.com`                            |
| `PROXY_PORT`    | Порт прокси                                           | `443`                                        |
| `PROXY_SECRET`  | Секрет прокси                                         | `AAAAAAAAAAAAAAAAAAAAAA...`                  |
| `SUPPORT_URL`   | Ссылка на поддержку (кнопка снизу)                    | `https://t.me/your_best_support`             |
| `SHARE_URL`     | Ссылка для кнопки «Поделиться» (пусто = текущий URL)  | `https://your.domain.com`                    |
| `SHARE_MODE`    | Режим шера: `copy` или `webshare`                     | `copy`                                       |


### SHARE_MODE подробнее
- `copy` — всегда копирует ссылку в буфер обмена (работает везде)
- `webshare` — нативный шер на Android/iOS, автоматический fallback на `copy` если браузер не поддерживает

## Обновление конфига

```bash
# Изменил .env → пересобери и перезапусти
docker compose up -d --build
```

## Реферальные ссылки

- `site.com/` → обычная страница
- `site.com/123` → кнопка «Перейти в бот» ведёт на `BOT_URL?start=ref_123`
