# qdc Anole VX Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.7; 25 -9.9; 28 -10.2; 31 -10.4; 34 -10.6; 37 -10.7; 41 -10.8; 45 -11.0; 49 -11.1; 54 -11.3; 60 -11.3; 66 -11.5; 72 -11.6; 79 -11.8; 87 -12.0; 96 -12.1; 106 -12.1; 116 -12.2; 128 -12.2; 141 -12.0; 155 -11.8; 170 -11.6; 187 -11.2; 206 -10.9; 227 -10.5; 249 -10.0; 274 -9.5; 302 -9.0; 332 -8.5; 365 -8.0; 402 -7.5; 442 -7.2; 486 -6.8; 535 -6.5; 588 -6.3; 647 -6.2; 712 -6.2; 783 -6.1; 861 -6.2; 947 -6.5; 1042 -6.9; 1146 -7.5; 1261 -7.9; 1387 -7.8; 1526 -7.2; 1678 -6.3; 1846 -5.4; 2031 -4.7; 2234 -4.0; 2457 -3.1; 2703 -2.5; 2973 -2.6; 3270 -2.2; 3597 -2.2; 3957 -3.2; 4353 -4.1; 4788 -1.3; 5267 -0.5; 5793 -0.6; 6373 -5.5; 7010 -8.6; 7711 -7.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.8; 18182 -8.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole VX Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole VX Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.41 | -4.0 dB |
| Peaking | 124 Hz   | 0.92 | -3.3 dB |
| Peaking | 221 Hz   | 1.46 | -1.9 dB |
| Peaking | 3059 Hz  | 1.84 | 4.5 dB  |
| Peaking | 5311 Hz  | 4.66 | 6.2 dB  |
| Peaking | 688 Hz   | 1.59 | 0.7 dB  |
| Peaking | 1304 Hz  | 3.49 | -2.0 dB |
| Peaking | 5934 Hz  | 9.75 | 2.6 dB  |
| Peaking | 7136 Hz  | 5.24 | -3.6 dB |
| Peaking | 17916 Hz | 1.93 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Anole%20VX%20Bass/qdc%20Anole%20VX%20Bass.png)