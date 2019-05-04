# Anker SoundCore Liberty Air
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.6; 25 -7.6; 28 -7.6; 31 -7.7; 34 -7.8; 37 -7.9; 41 -8.0; 45 -8.1; 49 -8.2; 54 -8.2; 60 -8.2; 66 -8.2; 72 -8.1; 79 -8.0; 87 -7.9; 96 -7.7; 106 -7.3; 116 -6.8; 128 -6.2; 141 -5.2; 155 -4.4; 170 -3.8; 187 -3.5; 206 -3.8; 227 -4.3; 249 -4.7; 274 -4.8; 302 -4.8; 332 -4.6; 365 -4.3; 402 -4.0; 442 -3.6; 486 -3.1; 535 -2.4; 588 -1.8; 647 -1.1; 712 -0.7; 783 -0.5; 861 -0.6; 947 -1.0; 1042 -1.7; 1146 -2.7; 1261 -3.8; 1387 -4.7; 1526 -5.0; 1678 -4.7; 1846 -4.0; 2031 -3.5; 2234 -2.9; 2457 -2.3; 2703 -2.5; 2973 -3.6; 3270 -5.2; 3597 -5.7; 3957 -5.0; 4353 -4.1; 4788 -3.4; 5267 -2.4; 5793 -1.7; 6373 -2.3; 7010 -5.0; 7711 -5.7; 8482 -3.7; 9330 -3.6; 10263 -5.0; 11289 -9.0; 12418 -5.7; 13660 -3.6; 15026 -3.6; 16529 -3.6; 18182 -5.6; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundCore Liberty Air GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundCore Liberty Air ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.44 | -4.3 dB |
| Peaking | 88 Hz    | 1.52 | -2.2 dB |
| Peaking | 804 Hz   | 1.75 | 3.5 dB  |
| Peaking | 1477 Hz  | 3.72 | -2.1 dB |
| Peaking | 11429 Hz | 5.13 | -6.0 dB |
| Peaking | 176 Hz   | 5.57 | 1.3 dB  |
| Peaking | 2666 Hz  | 2.81 | 3.1 dB  |
| Peaking | 3449 Hz  | 1.53 | -3.5 dB |
| Peaking | 6180 Hz  | 1.47 | 3.5 dB  |
| Peaking | 7370 Hz  | 4.17 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundCore%20Liberty%20Air/Anker%20SoundCore%20Liberty%20Air.png)