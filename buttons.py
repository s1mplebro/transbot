from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


langs = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text = "Russian🇷🇺",callback_data="rus"),
	InlineKeyboardButton(text = "English🇬🇧",callback_data="eng"),
	InlineKeyboardButton(text = "Uzbek🇺🇿",callback_data="uzb"),
	],
	[
	InlineKeyboardButton(text = "Afrikaans🌍",callback_data="afr"),
	InlineKeyboardButton(text = "Arabic󠁧󠁢󠁥󠁮󠁧󠁿🇸🇦",callback_data="ara"),
	InlineKeyboardButton(text = "Armenian🇦🇲",callback_data="arm"),
	],
	[
	InlineKeyboardButton(text = "Azerbaijani🇦🇿",callback_data="aze"),
	InlineKeyboardButton(text = "Belarusian🇧🇾",callback_data="bel"),
	InlineKeyboardButton(text = "Bulgarian🇧🇬",callback_data="bul"),
	],
	[
	InlineKeyboardButton(text = "Chinese (traditional)🇨🇳",callback_data="chi"),
	InlineKeyboardButton(text = "Croatian🇭🇷",callback_data="cro"),
	InlineKeyboardButton(text = "Dutch🇳🇱",callback_data="deu"),
	],
	[
	InlineKeyboardButton(text = "French🇫🇷",callback_data="fre"),
	InlineKeyboardButton(text = "Georgian🇬🇪",callback_data="geo"),
	InlineKeyboardButton(text = "German🇩🇪",callback_data="det"),
	],
	[
	InlineKeyboardButton(text = "Albanian🇦🇱",callback_data="alb"),
	InlineKeyboardButton(text = "Amharic🌍",callback_data="amh"),
	InlineKeyboardButton(text = "Bengali🇧🇯",callback_data="bng"),
	],
	[
	InlineKeyboardButton(text = "Bosnian🇧🇦",callback_data="bos"),
	InlineKeyboardButton(text = "Catalan🇨🇻",callback_data="cta"),
	InlineKeyboardButton(text = "Cebuano🌍",callback_data="ceb"),
	],
	#
	[
	InlineKeyboardButton(text = "Basque🇪🇸",callback_data="basq"),
	InlineKeyboardButton(text = "Chichewa🌍",callback_data="chichi"),
	InlineKeyboardButton(text = "Corsican🌍",callback_data="cors"),
	],
	[
	InlineKeyboardButton(text = "Czech🇨🇿",callback_data="chez"),
	InlineKeyboardButton(text = "Danish🇩🇰",callback_data="dani"),
	InlineKeyboardButton(text = "Esperanto🇵🇱",callback_data="espa"),
	],
	#
	[
	InlineKeyboardButton(text = "Estonian🇪🇪",callback_data="eston"),
	InlineKeyboardButton(text = "Filipino🇵🇭",callback_data="filip"),
	InlineKeyboardButton(text = "Finnish🇫🇮",callback_data="finn"),
	],
	[
	InlineKeyboardButton(text = "Greek🇬🇷",callback_data="grek"),
	InlineKeyboardButton(text = "Haitian creole🇬🇦",callback_data="gat"),
	InlineKeyboardButton(text = "Hausa🇳🇬",callback_data="hasua"),
	],
	[
	InlineKeyboardButton(text = "Hebrew🇮🇱",callback_data="izra"),
	InlineKeyboardButton(text = "Hindi🇮🇳",callback_data="hind"),
	InlineKeyboardButton(text = "Icelandic🇮🇸",callback_data="iceland"),
	],
	[
	InlineKeyboardButton(text = "Igbo🇳🇪",callback_data="igbo"),
	InlineKeyboardButton(text = "Indonesian🇮🇩",callback_data="indo"),
	InlineKeyboardButton(text = "Irish🇮🇷",callback_data="irish"),
	],
	[
	InlineKeyboardButton(text = "Italian🇮🇹",callback_data="ital"),
	InlineKeyboardButton(text = "Japanese🇯🇵",callback_data="japan"),
	InlineKeyboardButton(text = "Kannada🇨🇦",callback_data="canada"),
	],
	[
	InlineKeyboardButton(text = "Javanese🇮🇩",callback_data="javas"),
	InlineKeyboardButton(text = "Kazakh🇰🇿",callback_data="kaza"),
	InlineKeyboardButton(text = "korean🇰🇷",callback_data="korea"),
	],
	[
	InlineKeyboardButton(text = "Kyrgyz🇰🇬",callback_data="kgz"),
	InlineKeyboardButton(text = "Latvian🇱🇻",callback_data="latva"),
	InlineKeyboardButton(text = "Luxembourgish🇱🇺",callback_data="luxem"),
	],
	[
	InlineKeyboardButton(text = "Macedonian🇲🇰",callback_data="mace"),
	InlineKeyboardButton(text = "Malay🇲🇾",callback_data="mala"),
	InlineKeyboardButton(text = "Mongolian🇲🇳",callback_data="mongo"),
	],# нужно написать функции
	[
	InlineKeyboardButton(text = "Persian🇮🇷",callback_data="pers"),
	InlineKeyboardButton(text = "Polish🇵🇱",callback_data="polsh"),
	InlineKeyboardButton(text = "Portuguese🇵🇹",callback_data="port"),
	],
	[
	InlineKeyboardButton(text = "Romanian🇷🇴",callback_data="roman"),
	InlineKeyboardButton(text = "Serbian🇷🇸",callback_data="serb"),
	InlineKeyboardButton(text = "Spanish🇪🇸",callback_data="span"),
	],
	[
	InlineKeyboardButton(text = "Tajik🇹🇯",callback_data="tj"),
	InlineKeyboardButton(text = "Swedish🇸🇪",callback_data="swed"),
	InlineKeyboardButton(text = "Turkish🇹🇷",callback_data="turk"),
	],
	[
	InlineKeyboardButton(text = "Uyghur🌎",callback_data="uy"),
	InlineKeyboardButton(text = "Vietnamese🇻🇳",callback_data="viet"),
	InlineKeyboardButton(text = "Somali🇸🇴",callback_data="som"),
	],
	[
	InlineKeyboardButton(text = "Slovenian🇸🇮",callback_data="slov"),
	InlineKeyboardButton(text = "Thai🇹🇭",callback_data="thai"),
	InlineKeyboardButton(text = "Ukrainian🇺🇦",callback_data="ukr"),
	],
	[
	InlineKeyboardButton(text = "Назад🔙",callback_data="back")
	],
	],
)

menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text = "Начать перевод▶️",callback_data="begn"),
	InlineKeyboardButton(text = "Написать Админу💻",callback_data="writ"),
	],
	],
)
