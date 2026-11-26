# the-best-meal-you-ever-had

[![make.fun · u-pangg7-the-best-meal-you-ever-had-a3ac0f85](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)
[![rank](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/museweilejing923/the-best-meal-you-ever-had/rank.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)
[![reward](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/museweilejing923/the-best-meal-you-ever-had/reward.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)

The entry:

> The best meal I ever had was a 2 a.m. bowl of instant noodles on a train platform, eaten with plastic chopsticks while my train pulled away without me.

151 characters, limit 200.

Not a banquet and not a restaurant review: a bowl of noodles on a platform at 2 a.m., eaten with plastic chopsticks while the train left without its passenger. Named dish, place, texture and one specific moment, all inside a single clean sentence that reads aloud well. The train leaving is the detail that makes the noodles taste better in memory than any restaurant meal could. In a head-to-head vote the sentence that makes the meal feel most real moves on. The plastic chopsticks are the part nobody forgets: the meal was improvised, and improvisation is what makes it the best one.

## Run

```sh
python3 main.py
```

## How it works

`main.py` runs one fixed sentence through a table of named checks and writes it to `/output/entry.txt`. The output is fully deterministic: no network, no randomness, no clock. The checks, in table order, are: about a meal, ends with a full stop, non-empty, one plain sentence with no exclamation or question mark, within the 200-character limit, no filler word "very", contains letters, every character printable, no leading or trailing space, and no double spaces or newlines. Each check is a small named function, and the table pairs it with the complaint printed when it fails — the first failure stops the run before anything is written.
