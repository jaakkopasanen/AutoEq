# Anker SoundCore Liberty Lite
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.1; 25 -6.1; 28 -6.1; 31 -6.0; 34 -5.8; 37 -5.5; 41 -5.1; 45 -4.7; 49 -4.3; 54 -4.0; 60 -4.0; 66 -4.1; 72 -4.2; 79 -4.3; 87 -4.6; 96 -5.0; 106 -5.4; 116 -6.0; 128 -6.5; 141 -6.9; 155 -6.8; 170 -6.3; 187 -5.5; 206 -4.8; 227 -4.2; 249 -3.6; 274 -3.0; 302 -2.6; 332 -2.3; 365 -2.1; 402 -2.0; 442 -2.0; 486 -1.9; 535 -1.6; 588 -1.4; 647 -1.0; 712 -0.7; 783 -0.5; 861 -0.5; 947 -1.0; 1042 -1.9; 1146 -2.9; 1261 -3.8; 1387 -4.5; 1526 -4.8; 1678 -4.8; 1846 -4.8; 2031 -4.6; 2234 -3.9; 2457 -3.4; 2703 -3.4; 2973 -4.9; 3270 -6.8; 3597 -7.7; 3957 -7.0; 4353 -5.7; 4788 -3.7; 5267 -2.4; 5793 -1.8; 6373 -2.3; 7010 -2.4; 7711 -4.3; 8482 -8.2; 9330 -9.5; 10263 -5.6; 11289 -3.9; 12418 -5.2; 13660 -6.7; 15026 -4.3; 16529 -3.9; 18182 -3.9; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundCore Liberty Lite GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundCore Liberty Lite ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 143 Hz   | 1.83 | -3.3 dB |
| Peaking | 635 Hz   | 0.96 | 3.3 dB  |
| Peaking | 3723 Hz  | 2.8  | -4.6 dB |
| Peaking | 6124 Hz  | 1.71 | 3.2 dB  |
| Peaking | 9028 Hz  | 3.74 | -6.9 dB |
| Peaking | 27 Hz    | 1.54 | -2.4 dB |
| Peaking | 931 Hz   | 3.03 | 1.8 dB  |
| Peaking | 1547 Hz  | 1.21 | -1.7 dB |
| Peaking | 2560 Hz  | 3.98 | 1.8 dB  |
| Peaking | 13532 Hz | 5.38 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundCore%20Liberty%20Lite/Anker%20SoundCore%20Liberty%20Lite.png)