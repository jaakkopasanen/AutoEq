# Anker SoundCore Liberty Lite
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.8; 25 -10.8; 28 -10.8; 31 -10.7; 34 -10.5; 37 -10.3; 41 -9.8; 45 -9.4; 49 -9.0; 54 -8.7; 60 -8.3; 66 -8.2; 72 -8.1; 79 -8.0; 87 -8.0; 96 -8.0; 106 -8.0; 116 -8.1; 128 -8.3; 141 -8.3; 155 -8.1; 170 -7.3; 187 -5.9; 206 -4.7; 227 -4.0; 249 -3.5; 274 -2.9; 302 -2.4; 332 -2.1; 365 -1.9; 402 -1.9; 442 -1.9; 486 -1.8; 535 -1.6; 588 -1.3; 647 -1.0; 712 -0.7; 783 -0.5; 861 -0.6; 947 -1.0; 1042 -1.9; 1146 -3.0; 1261 -3.9; 1387 -4.5; 1526 -4.8; 1678 -4.9; 1846 -5.0; 2031 -4.8; 2234 -4.4; 2457 -3.7; 2703 -3.7; 2973 -4.7; 3270 -6.4; 3597 -7.3; 3957 -6.6; 4353 -5.2; 4788 -4.0; 5267 -2.7; 5793 -1.6; 6373 -1.2; 7010 -2.4; 7711 -4.9; 8482 -7.7; 9330 -7.7; 10263 -4.9; 11289 -4.1; 12418 -5.3; 13660 -5.8; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundCore Liberty Lite GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundCore Liberty Lite ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.31 | -6.8 dB |
| Peaking | 140 Hz  | 1.7  | -3.6 dB |
| Peaking | 955 Hz  | 0.46 | 6.7 dB  |
| Peaking | 1537 Hz | 0.66 | -6.0 dB |
| Peaking | 8969 Hz | 5.87 | -4.7 dB |
| Peaking | 522 Hz  | 4.81 | -0.8 dB |
| Peaking | 2633 Hz | 2.97 | 2.2 dB  |
| Peaking | 3599 Hz | 3.07 | -3.3 dB |
| Peaking | 6105 Hz | 2.52 | 4.3 dB  |
| Peaking | 8196 Hz | 0.37 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundCore%20Liberty%20Lite/Anker%20SoundCore%20Liberty%20Lite.png)