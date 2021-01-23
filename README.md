# emojify

word2emoji: Translating text to emojis using GloVe embeddings and emoji keywords. Still needs proper stop word removal, similarity thresholding, ranking, blacklisting (ℹ, 🆕), a prioritized lookup table, and other features to be more accurate.

Example 1: 
```
on 🆕 a 🅰 dark 🌑 desert 🏜 highway 🛣 
cool 🆒 wind 🌈 in 🏙 my ℹ hair 👱 
warm 🆒 smell 🍠 of 🏙 colitas 🙅 🏿 ‍ ♀ ️ 
rising 💹 up 🆙 through 🚿 the 🆕 air 🌡 
up 🆙 ahead 🏰 in 🏙 the 🆕 distance ☎ 
i ℹ saw 🚗 a 🅰 shimmering ❇ light 🕯 
my ℹ head 👁 grew 👪 heavy 🌈 and ℹ my ℹ sight 👀 grew 👪 dim 🔅 
i ℹ had ℹ to 🆕 stop ⏹ for 🆕 the 🆕 night 🌃 
there ℹ she ♀ stood 🏳 in 🏙 the 🆕 doorway 🚪 
i ℹ heard 🔊 the 🆕 mission 🌌 bell 🔔 
and ℹ i ℹ was ♂ thinking 🤔 to 🆕 myself ℹ 
this ℹ could ℹ be ℹ heaven 💕 or ℹ this ℹ could ℹ be ℹ hell 💕 
then ⚾ she ♀ lit 🕯 up 🆙 a 🅰 candle 🌹 
and ℹ she ♀ showed 📺 me ℹ the 🆕 way ℹ 
there ℹ were 🔒 voices 🔊 down 🔒 the 🆕 corridor 🚈 
i ℹ thought ℹ i ℹ heard 🔊 them ℹ say ℹ 
welcome 🎀 to 🆕 the 🆕 hotel 🛏 california 🌮
```

Example 2: 
```
its 🆕 a 🅰 godawful 🚊 small 🔉 affair 💕 
to 🆕 the 🆕 girl 👩 ‍ 👧 ‍ 👦 with 🆕 the 🆕 mousy 👱 hair 👱 
but ℹ her ♀ mummy 🐊 is 🅰 yelling 🏳 no 🚫 
and ℹ her ♀ daddy 💕 has 🏘 told 📰 her ♀ to 🆕 go ℹ 
but ℹ her ♀ friend 💕 is 🅰 nowhere ☮ to 🆕 be ℹ seen 👨 
now 🆕 she ♀ walks 🚶 through 🚿 her ♀ sunken 🚤 dream 💕 
to 🆕 the 🆕 seat 💺 with 🆕 the 🆕 clearest ⚠ view ♿ 
and ℹ shes ♀ hooked ⚾ to 🆕 the 🆕 silver 🏅 screen 🎦 
but ℹ the 🆕 film 🎦 is 🅰 a 🅰 saddening 🎧 bore 🐨 
for 🆕 shes ♀ lived 👪 it ℹ ten 🕥 times 📰 or ℹ more 🆕 
she ♀ could ℹ spit 👄 in 🏙 the 🆕 eyes 👄 of 🏙 fools 💕 
as 🆕 they ℹ ask ℹ her ♀ to 🆕 focus ☮ on 🆕 
sailors 🚤 fighting ☮ in 🏙 the 🆕 dance 🕺 hall 🏭 
oh 🆗 man 👨 look ℹ at 🏟 those ℹ cavemen 🦏 go ℹ 
its 🆕 the 🆕 freakiest 🙅 🏿 ‍ ♀ ️ show 📺 
take ℹ a 🅰 look ℹ at 🏟 the 🆕 lawman 🐊 
beating 🏅 up 🆙 the 🆕 wrong ℹ guy 👨 
oh 🆗 man 👨 wonder 💕 if ℹ hell 💕 ever ℹ know ℹ 
hes ♂ in 🏙 the 🆕 best 🕹 selling 💲 show 📺 
is 🅰 there ℹ life 👪 on 🆕 mars 🛰 
```

Example 3:
```
there ℹ is 🅰 a 🅰 house 🏘 in 🏙 new 🆕 orleans 🏙 
they ℹ call ☎ the 🆕 rising 💹 sun 🌤 
and ℹ its 🆕 been ℹ the 🆕 ruin 💕 of 🏙 many 🌱 a 🅰 poor 🚿 boy 👦 
and ℹ god 🛐 i ℹ know ℹ im Ⓜ one 👨 
my ℹ mother ♀ was ♂ a 🅰 tailor 👗 
she ♀ sewed 👄 my ℹ new 🆕 blue 💙 jeans 👖 
my ℹ father 👪 was ♂ a 🅰 gamblin 🐓 man 👨 
down 🔒 in 🏙 new 🆕 orleans 🏙 
now 🆕 the 🆕 only 🚫 thing ℹ a 🅰 gambler 🏇 needs ♿ 
is 🅰 a 🅰 suitcase 💼 and ℹ trunk 🌲 
and ℹ the 🆕 only 🚫 time ℹ hell 💕 be ℹ satisfied 😞 
is 🅰 when ℹ hes ♂ all ℹ drunk 🚗 
```
