
## Install

1. set your telegram api credentials in the scripts
2. run `$ python3 load_old_messages.py` It will print out your account's channel and chat ids
3. set the source and target channel ids for message mirroring in the scripts
4. run `$ python3 watch_new_messages.py`

## TODO

- allow any number of mirror bindings, not just one
- combine 2 scripts into one cli util
- it should possible to accurately quote the messages: you map every message from the original chat with the forwarding chat, with a id to id map, and when a message is a quote, then you find the right message using that map

`$ tgmirror src=-01909212 dst=-010920192` 
