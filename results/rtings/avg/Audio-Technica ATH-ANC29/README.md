# Audio-Technica ATH-ANC29
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -2.4; 25 -2.1; 28 -1.9; 31 -1.8; 34 -1.7; 37 -1.7; 41 -1.7; 45 -1.8; 49 -2.0; 54 -2.1; 60 -2.3; 66 -2.6; 72 -2.8; 79 -3.0; 87 -3.4; 96 -3.7; 106 -4.1; 116 -4.4; 128 -4.7; 141 -5.1; 155 -5.3; 170 -5.5; 187 -5.5; 206 -5.5; 227 -5.5; 249 -5.4; 274 -5.5; 302 -5.6; 332 -5.8; 365 -5.9; 402 -6.1; 442 -6.5; 486 -6.8; 535 -7.1; 588 -7.3; 647 -7.3; 712 -7.4; 783 -7.4; 861 -5.6; 947 -5.0; 1042 -8.1; 1146 -11.2; 1261 -10.5; 1387 -8.0; 1526 -4.9; 1678 -2.7; 1846 -1.6; 2031 -1.1; 2234 -0.6; 2457 -0.6; 2703 -1.3; 2973 -1.4; 3270 -0.6; 3597 -0.6; 3957 -0.6; 4353 -0.6; 4788 -0.6; 5267 -0.5; 5793 -1.6; 6373 -8.4; 7010 -8.8; 7711 -6.6; 8482 -6.6; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.6; 16529 -6.6; 18182 -6.6; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC29 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC29 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.46 | 5.4 dB  |
| Peaking | 45 Hz   | 1.55 | -0.5 dB |
| Peaking | 1208 Hz | 3.93 | -7.7 dB |
| Peaking | 3246 Hz | 0.58 | 6.9 dB  |
| Peaking | 6856 Hz | 4.96 | -6.7 dB |
| Peaking | 634 Hz  | 3.17 | -1.6 dB |
| Peaking | 1978 Hz | 2.85 | 1.3 dB  |
| Peaking | 2925 Hz | 3.97 | -1.6 dB |
| Peaking | 5454 Hz | 5.33 | 2.9 dB  |
| Peaking | 9832 Hz | 1.18 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | 1.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC29/Audio-Technica%20ATH-ANC29.png)