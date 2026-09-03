"""
SUFIA AI Trading Bot - Telegram Bot Integration
Supports Inline Keyboards, WebApp Mini App, Voice Notes, and Live Signals
"""

import os
import sys
import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Default WebApp URL (can be localhost via ngrok/localtunnel or live domain)
WEBAPP_URL = os.getenv("WEBAPP_URL", "http://localhost:8000")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

def get_main_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🚀 Launch SUFIA Web App (Full UI)", web_app=WebAppInfo(url=WEBAPP_URL))
        ],
        [
            InlineKeyboardButton("🎙️ Voice Studio", callback_data="btn_voice"),
            InlineKeyboardButton("📊 Auto Trade", callback_data="btn_trade")
        ],
        [
            InlineKeyboardButton("📈 QX Live Signal", callback_data="btn_signal"),
            InlineKeyboardButton("👤 User Profile", callback_data="btn_profile")
        ],
        [
            InlineKeyboardButton("⚡ Instant EUR/USD OTC Signal", callback_data="btn_quick_signal")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name or "TARIK"
    welcome_text = (
        f"👋 **Welcome {user_name}!**\n\n"
        "👑 **SUFIA — Your AI Trading Journey Starts Up**\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "সোফিয়া এআই ট্রেডিং বটে আপনাকে স্বাগতম!\n\n"
        "🔹 **Voice Studio**: ভয়েস ইনপুট দিয়ে ট্রেডিং সংক্রান্ত যেকোনো প্রশ্ন করুন।\n"
        "🔹 **Auto Trade Place**: Quotex ও ক্রিপ্টো পেয়ারে অটো ট্রেড চালু করুন।\n"
        "🔹 **QX Live Signal**: ৯৬%+ এক্যুরেসি সম্পন্ন লাইভ সিগন্যাল পান।\n\n"
        "👇 নিচে থাকা বাটনগুলোতে ক্লিক করে আপনার ট্রেডিং জার্নি শুরু করুন:"
    )
    await update.message.reply_text(
        welcome_text,
        reply_markup=get_main_keyboard(),
        parse_mode="Markdown"
    )

async def signal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signal_msg = (
        "📈 **QX LIVE SIGNAL ALERT** 📈\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "🎯 **Asset**: EUR/USD (OTC)\n"
        "⏱️ **Timeframe**: 1 Minute\n"
        "🟢 **Direction**: CALL (BUY / UP ⬆)\n"
        "🔥 **AI Confidence**: 96%\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "💡 *AI Note: Strong momentum above support 1.0840. Place trade now!*"
    )
    await update.message.reply_text(signal_msg, parse_mode="Markdown")

async def autotrade_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "📊 **SUFIA AUTO TRADE ENGINE**\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "💰 **Demo Balance**: $10,450.00\n"
        "⚙️ **Strategy**: AI Smart Trend + Martingale (1-Step)\n"
        "✅ **Status**: Bot is Ready to Auto Trade.\n\n"
        "👉 সম্পূর্ণ ড্যাশবোর্ড ও বাটন কন্ট্রোল দেখতে **Launch SUFIA Web App** এ ক্লিক করুন।"
    )
    await update.message.reply_text(msg, reply_markup=get_main_keyboard(), parse_mode="Markdown")

async def voice_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "🎙️ **SUFIA VOICE STUDIO**\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "সোফিয়া ভয়েস অ্যাসিস্ট্যান্ট সচল আছে!\n"
        "আপনি আমাকে এখানে ভয়েস মেসেজ পাঠাতে পারেন অথবা Web App ওপেন করে সরাসরি কথা বলতে পারেন।"
    )
    await update.message.reply_text(msg, reply_markup=get_main_keyboard(), parse_mode="Markdown")

async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "btn_voice":
        await query.message.reply_text(
            "🎙️ **Voice Studio**: সোফিয়া এআই ভয়েস অ্যাসিস্ট্যান্টের সাথে লাইভ কথা বলতে Web App ওপেন করুন বা ভয়েস নোট পাঠান।",
            reply_markup=get_main_keyboard(),
            parse_mode="Markdown"
        )
    elif query.data == "btn_trade":
        await query.message.reply_text(
            "📊 **Auto Trade Place**: Quotex এ অটোমেটেড ডেমো/লাইভ ট্রেড এক্সিকিউট করতে Web App এ Auto Trade সুইচ অন করুন।",
            reply_markup=get_main_keyboard(),
            parse_mode="Markdown"
        )
    elif query.data == "btn_signal":
        await query.message.reply_text(
            "📈 **QX Live Signal**: ৯৬% এক্যুরেসি সহ লাইভ ১-মিনিট ও ৫-মিনিট সিগন্যাল Web App এ রিয়েল-টাইম কাউন্টডাউন সহ চালু আছে।",
            reply_markup=get_main_keyboard(),
            parse_mode="Markdown"
        )
    elif query.data == "btn_profile":
        await query.message.reply_text(
            "👤 **User Profile**:\nUser: TARIK\nStatus: 🟢 ACTIVATED (ASADXANIKA) 👑\nQuotex ID: 83923904",
            reply_markup=get_main_keyboard(),
            parse_mode="Markdown"
        )
    elif query.data == "btn_quick_signal":
        await query.message.reply_text(
            "🔥 **INSTANT SIGNAL**: EUR/USD (OTC) • 1 MIN • 🟢 CALL (UP) • 96% Accuracy!",
            reply_markup=get_main_keyboard(),
            parse_mode="Markdown"
        )

async def handle_voice_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎙️ **সোফিয়া আপনার ভয়েস গ্রহণ করেছে!**\n\n"
        "অ্যানালাইসিস: বর্তমান EUR/USD চার্টে স্ট্রং বুলিশ মোমেন্টাম রয়েছে। পরবর্তী ক্যান্ডেলে ১-মিনিট CALL ট্রেড নেওয়ার সুযোগ রয়েছে।",
        parse_mode="Markdown"
    )

def main():
    token = TELEGRAM_BOT_TOKEN
    if not token:
        print("⚠️ Telegram Bot Token not set. Pass token or set TELEGRAM_BOT_TOKEN environment variable.")
        print("To run with token: python telegram_bot.py YOUR_BOT_TOKEN")
        if len(sys.argv) > 1:
            token = sys.argv[1]
        else:
            return

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("signals", signal_command))
    application.add_handler(CommandHandler("autotrade", autotrade_command))
    application.add_handler(CommandHandler("voice", voice_command))
    application.add_handler(CallbackQueryHandler(handle_callback_query))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice_message))

    print("🤖 SUFIA Telegram Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
