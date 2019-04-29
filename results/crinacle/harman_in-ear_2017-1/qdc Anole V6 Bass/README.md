# qdc Anole V6 Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.0; 25 -11.0; 28 -11.0; 31 -11.0; 34 -11.0; 37 -11.1; 41 -11.1; 45 -11.1; 49 -11.1; 54 -11.0; 60 -11.0; 66 -11.1; 72 -11.2; 79 -11.3; 87 -11.3; 96 -11.4; 106 -11.4; 116 -11.4; 128 -11.3; 141 -11.2; 155 -11.1; 170 -10.8; 187 -10.6; 206 -10.2; 227 -9.9; 249 -9.5; 274 -9.2; 302 -8.7; 332 -8.3; 365 -7.9; 402 -7.6; 442 -7.4; 486 -7.2; 535 -7.0; 588 -6.8; 647 -6.7; 712 -6.6; 783 -6.5; 861 -6.4; 947 -6.6; 1042 -7.1; 1146 -7.9; 1261 -8.5; 1387 -8.7; 1526 -8.5; 1678 -8.1; 1846 -7.6; 2031 -6.8; 2234 -5.8; 2457 -4.5; 2703 -3.2; 2973 -2.3; 3270 -2.2; 3597 -2.5; 3957 -3.3; 4353 -3.3; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.0; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -7.4; 13660 -18.4; 15026 -28.9; 16529 -31.5; 18182 -29.5; 20000 -32.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V6 Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V6 Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 68 Hz    | 0.2  | -5.1 dB  |
| Peaking | 1493 Hz  | 1.46 | -4.5 dB  |
| Peaking | 5618 Hz  | 0.28 | 26.2 dB  |
| Peaking | 12153 Hz | 1.64 | 18.2 dB  |
| Peaking | 15385 Hz | 0.18 | -40.6 dB |
| Peaking | 3007 Hz  | 6.38 | 1.1 dB   |
| Peaking | 4241 Hz  | 4.84 | -2.9 dB  |
| Peaking | 7635 Hz  | 1.15 | 3.1 dB   |
| Peaking | 8048 Hz  | 2.26 | -4.5 dB  |
| Peaking | 20061 Hz | 3.67 | -4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 16000 Hz | 1.41 | -32.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Anole%20V6%20Bass/qdc%20Anole%20V6%20Bass.png)