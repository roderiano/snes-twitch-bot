# snes-twitch-bot 
snes-twitch-bot is a project that controls **SNES9X 1.53** emulator inputs via twitch chat. **This project uses WinAPI**. 

<p align="center">
  <img src="https://i.giphy.com/media/5hnV7LmdgW2RqhA3i3/giphy.webp" />
</p>

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```

## Configuration
It's necessary configure your access token and channel name.
You can generate a Bot Chat Token by accessing [Twitch Token Generator](https://twitchtokengenerator.com/). You need the Access Token. 

```yaml
bot:
  token: 'your_access_token_here'
  prefix: '!'
  channels:
    - 'your_channel_name_here' 
input_handler:
  input_duration: 1.5
  compatible_emulator:
    - 'Snes9X'
```

## Initialization
You need to open **SNES9X 1.53** [(Download Link)](https://emulator.games/emulators/super-nintendo/snes9x-1-53/) before starting the project. Disable `Emulation > Pause When Inactive` option for better performace.

When the emulator is open run:
```bash
python3 bot.py
```

## Default Commands

| Chat  | SNES        | SNES9X          | Description                    |
|-------|-------------|-----------------|--------------------------------|
| !a    | A Button    | V Key           | Send A command to emulator     |
| !b    | B Button    | Z Key           | Send B command to emulator     |
| !x    | X Button    | C Key           | Send X command to emulator     |
| !y    | Y Button    | X Key           | Send Y command to emulator     |
| !r    | Right Arrow | Right Arrow Key | Send Right command to emulator |
| !l    | Left Arrow  | Left Arrow Key  | Send Left command to emulator  |
| !u    | Up Arrow    | Up Arrow Key    | Send Up command to emulator    |
| !d    | Down Arrow  | Down Arrow Key  | Send Down command to emulator  |
| !help | chat only   | chat only       | Command list                   |


## License
[MIT](https://choosealicense.com/licenses/mit/)
