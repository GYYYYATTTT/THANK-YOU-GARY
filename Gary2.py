#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

st.set_page_config(page_title="Manga Aesthetic Fonts", page_icon="🎌")
st.title("Manga / New‑Age Aesthetic Fonts (English Only)")

# ---------- helpers ----------
def map_text(text, src, dst):
    table = {ord(a): b for a, b in zip(src, dst)}
    return text.translate(table)

def to_fullwidth(text):
    return ''.join(chr(ord(c)+0xFEE0) if '!' <= c <= '~' else c for c in text)

def to_bubble(text):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    bubble  = "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ" \
              "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ" \
              "⓪①②③④⑤⑥⑦⑧⑨"
    table = {ord(a): b for a, b in zip(normal, bubble)}
    return ''.join(table.get(ord(ch), ch) for ch in text)

def to_fraktur(text):
    normal  = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    fraktur = "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ" \
              "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷"
    return map_text(text, normal, fraktur)

def to_bold_fraktur(text):
    normal   = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    boldfrak = "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅" \
               "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟"
    return map_text(text, normal, boldfrak)

def to_script(text):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    script = "𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵" \
             "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"
    return map_text(text, normal, script)

def to_bold_script(text):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    bold_script = "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩" \
                  "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃"
    return map_text(text, normal, bold_script)

def to_double_struck(text):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ds     = "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ" \
             "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫"
    return map_text(text, normal, ds)

def to_sans_bold(text):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    sansb  = "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭" \
             "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇"
    return map_text(text, normal, sansb)

def to_monospace(text):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    mono   = "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉" \
             "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣"
    return map_text(text, normal, mono)

def to_small_caps(text):
    lower = "abcdefghijklmnopqrstuvwxyz"
    small = "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ"
    table = {ord(a): b for a, b in zip(lower, small)}
    return ''.join(table.get(ord(ch), ch) for ch in text)

# style list + emoji frames
styles = [
    ("Bubble (Circled)",      to_bubble,      ["🌸","✨","💖"], "⭐"),
    ("Script",                to_script,      ["✨","💖","🌸"], "⭐"),
    ("Bold Script",           to_bold_script, ["💖","🌸","✨"], "🌈"),
    ("Fullwidth (Vaporwave)", to_fullwidth,   ["🌈","✨","⭐"], "🌸"),
    ("Fraktur",               to_fraktur,     ["✨","🌟","💖"], "🌸"),
    ("Bold Fraktur",          to_bold_fraktur,["🌟","✨","🌸"], "💖"),
    ("Double-Struck",         to_double_struck,["💫","✨","⭐"], "🌸"),
    ("Sans-Serif Bold",       to_sans_bold,   ["✨","⭐","🌸"], "💖"),
    ("Monospace",             to_monospace,   ["🧸","✨","🍡"], "🌟"),
    ("Small Caps",            to_small_caps,  ["🌸","⭐","✨"], "💖"),
]

# ---------- UI ----------
user_text = st.text_input("Enter text:", "thank you gary")
handle = "@higary__"  # fixed as requested

st.write("---")
for name, fn, prefix_emojis, suffix_emoji in styles:
    styled = fn(user_text)
    left = " ".join(prefix_emojis)
    output = f"{left} {styled} {handle} {suffix_emoji}"
    st.markdown(f"**{name}**")
    st.markdown(f"<div style='font-size:1.6em; padding:6px 0'>{output}</div>", unsafe_allow_html=True)

