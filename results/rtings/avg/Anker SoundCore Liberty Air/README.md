# Anker SoundCore Liberty Air
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -2.8; 25 -2.8; 28 -2.9; 31 -2.9; 34 -3.0; 37 -3.1; 41 -3.2; 45 -3.3; 49 -3.4; 54 -3.5; 60 -3.8; 66 -4.1; 72 -4.2; 79 -4.3; 87 -4.5; 96 -4.6; 106 -4.7; 116 -4.8; 128 -4.6; 141 -4.0; 155 -3.6; 170 -3.3; 187 -3.4; 206 -3.9; 227 -4.5; 249 -4.8; 274 -5.0; 302 -4.9; 332 -4.8; 365 -4.5; 402 -4.1; 442 -3.6; 486 -3.1; 535 -2.5; 588 -1.8; 647 -1.1; 712 -0.7; 783 -0.5; 861 -0.6; 947 -1.0; 1042 -1.7; 1146 -2.6; 1261 -3.7; 1387 -4.7; 1526 -4.9; 1678 -4.5; 1846 -3.8; 2031 -3.2; 2234 -2.2; 2457 -1.5; 2703 -2.0; 2973 -3.7; 3270 -5.5; 3597 -6.1; 3957 -5.4; 4353 -4.2; 4788 -2.8; 5267 -2.1; 5793 -1.8; 6373 -3.4; 7010 -4.8; 7711 -5.0; 8482 -3.7; 9330 -3.3; 10263 -5.5; 11289 -8.0; 12418 -5.5; 13660 -1.4; 15026 -1.4; 16529 -1.4; 18182 -5.8; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundCore Liberty Air GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundCore Liberty Air ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 125 Hz   | 0.31 | -3.1 dB |
| Peaking | 1538 Hz  | 3.43 | -3.6 dB |
| Peaking | 3656 Hz  | 2.78 | -4.8 dB |
| Peaking | 11130 Hz | 2.38 | -6.2 dB |
| Peaking | 19305 Hz | 1.51 | -6.8 dB |
| Peaking | 175 Hz   | 2.31 | 2.2 dB  |
| Peaking | 551 Hz   | 0.4  | -2.5 dB |
| Peaking | 731 Hz   | 1.22 | 4.2 dB  |
| Peaking | 7319 Hz  | 3.63 | -3.8 dB |
| Peaking | 8925 Hz  | 0.24 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundCore%20Liberty%20Air/Anker%20SoundCore%20Liberty%20Air.png)