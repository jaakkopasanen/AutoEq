# qdc Gemini Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.1; 25 -10.2; 28 -10.4; 31 -10.4; 34 -10.5; 37 -10.6; 41 -10.6; 45 -10.7; 49 -10.7; 54 -10.8; 60 -10.8; 66 -11.0; 72 -11.1; 79 -11.3; 87 -11.3; 96 -11.6; 106 -11.6; 116 -11.7; 128 -11.6; 141 -11.6; 155 -11.4; 170 -11.2; 187 -10.9; 206 -10.6; 227 -10.2; 249 -9.9; 274 -9.4; 302 -8.9; 332 -8.4; 365 -7.9; 402 -7.5; 442 -7.2; 486 -6.9; 535 -6.6; 588 -6.5; 647 -6.5; 712 -6.4; 783 -6.4; 861 -6.6; 947 -6.9; 1042 -7.4; 1146 -8.1; 1261 -8.5; 1387 -8.4; 1526 -7.8; 1678 -7.0; 1846 -6.2; 2031 -5.3; 2234 -4.3; 2457 -3.3; 2703 -2.1; 2973 -0.9; 3270 -1.2; 3597 -1.9; 3957 -2.5; 4353 -4.1; 4788 -2.7; 5267 -0.5; 5793 -0.5; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -16.1; 15026 -24.8; 16529 -26.6; 18182 -26.2; 20000 -26.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Gemini Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Gemini Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.33 | -3.9 dB  |
| Peaking | 153 Hz   | 0.88 | -3.4 dB  |
| Peaking | 4633 Hz  | 0.37 | 18.0 dB  |
| Peaking | 12424 Hz | 0.71 | 25.8 dB  |
| Peaking | 14992 Hz | 0.21 | -40.2 dB |
| Peaking | 704 Hz   | 1.39 | 1.4 dB   |
| Peaking | 1344 Hz  | 2.03 | -2.3 dB  |
| Peaking | 2923 Hz  | 2.94 | 2.5 dB   |
| Peaking | 4415 Hz  | 4.16 | -3.9 dB  |
| Peaking | 5503 Hz  | 3.73 | 2.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 16000 Hz | 1.41 | -25.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Gemini%20Bass/qdc%20Gemini%20Bass.png)