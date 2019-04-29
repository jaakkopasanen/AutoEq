# qdc Anole V3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.0; 25 -9.1; 28 -9.3; 31 -9.5; 34 -9.6; 37 -9.8; 41 -9.9; 45 -10.0; 49 -10.1; 54 -10.3; 60 -10.5; 66 -10.7; 72 -11.0; 79 -11.2; 87 -11.4; 96 -11.8; 106 -12.0; 116 -12.2; 128 -12.3; 141 -12.5; 155 -12.5; 170 -12.5; 187 -12.4; 206 -12.2; 227 -12.0; 249 -11.7; 274 -11.4; 302 -11.0; 332 -10.7; 365 -10.3; 402 -9.9; 442 -9.3; 486 -8.8; 535 -8.1; 588 -7.5; 647 -6.7; 712 -5.8; 783 -4.9; 861 -4.1; 947 -3.5; 1042 -3.3; 1146 -3.5; 1261 -3.8; 1387 -3.7; 1526 -3.2; 1678 -2.5; 1846 -1.8; 2031 -1.4; 2234 -1.5; 2457 -2.0; 2703 -2.3; 2973 -2.1; 3270 -1.5; 3597 -0.5; 3957 -0.6; 4353 -1.2; 4788 -0.6; 5267 -0.8; 5793 -3.1; 6373 -5.6; 7010 -5.8; 7711 -7.0; 8482 -7.5; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -9.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.21 | -2.3 dB |
| Peaking | 193 Hz  | 0.42 | -5.3 dB |
| Peaking | 934 Hz  | 1.55 | 3.2 dB  |
| Peaking | 2097 Hz | 1.25 | 4.2 dB  |
| Peaking | 4322 Hz | 1.78 | 5.4 dB  |
| Peaking | 3590 Hz | 3.63 | 2.2 dB  |
| Peaking | 4423 Hz | 1.65 | -2.4 dB |
| Peaking | 5200 Hz | 4.67 | 3.5 dB  |
| Peaking | 8075 Hz | 3.22 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Anole%20V3/qdc%20Anole%20V3.png)