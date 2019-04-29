# qdc 5SH
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.9; 25 -7.1; 28 -7.3; 31 -7.5; 34 -7.7; 37 -7.8; 41 -8.0; 45 -8.1; 49 -8.2; 54 -8.4; 60 -8.6; 66 -8.8; 72 -9.1; 79 -9.4; 87 -9.6; 96 -10.0; 106 -10.3; 116 -10.5; 128 -10.6; 141 -10.7; 155 -10.7; 170 -10.7; 187 -10.6; 206 -10.4; 227 -10.1; 249 -9.8; 274 -9.4; 302 -9.0; 332 -8.7; 365 -8.3; 402 -7.9; 442 -7.5; 486 -7.2; 535 -6.9; 588 -6.7; 647 -6.6; 712 -6.6; 783 -6.6; 861 -6.8; 947 -7.1; 1042 -7.5; 1146 -8.0; 1261 -8.3; 1387 -8.1; 1526 -7.5; 1678 -6.7; 1846 -6.1; 2031 -6.0; 2234 -6.2; 2457 -5.5; 2703 -3.0; 2973 -0.5; 3270 -0.5; 3597 -1.0; 3957 -1.4; 4353 -2.9; 4788 -4.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.4; 7711 -7.7; 8482 -9.4; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.0; 15026 -12.3; 16529 -9.9; 18182 -11.3; 20000 -21.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc 5SH GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc 5SH ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 140 Hz   | 0.58 | -4.3 dB  |
| Peaking | 3311 Hz  | 1.94 | 7.8 dB   |
| Peaking | 5842 Hz  | 2.8  | 7.6 dB   |
| Peaking | 14760 Hz | 0.05 | -2.0 dB  |
| Peaking | 20021 Hz | 1.19 | -12.6 dB |
| Peaking | 679 Hz   | 1.89 | 1.0 dB   |
| Peaking | 1262 Hz  | 3.76 | -1.4 dB  |
| Peaking | 8366 Hz  | 4.31 | -3.8 dB  |
| Peaking | 13137 Hz | 0.84 | 4.2 dB   |
| Peaking | 14636 Hz | 2.41 | -7.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -6.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%205SH/qdc%205SH.png)