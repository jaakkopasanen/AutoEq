# qdc 4SS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.8; 25 -3.9; 28 -4.1; 31 -4.3; 34 -4.4; 37 -4.6; 41 -4.7; 45 -4.9; 49 -5.0; 54 -5.2; 60 -5.5; 66 -5.8; 72 -6.2; 79 -6.5; 87 -6.9; 96 -7.4; 106 -7.9; 116 -8.2; 128 -8.5; 141 -8.9; 155 -9.2; 170 -9.4; 187 -9.6; 206 -9.6; 227 -9.5; 249 -9.4; 274 -9.3; 302 -9.1; 332 -8.9; 365 -8.6; 402 -8.4; 442 -8.0; 486 -7.6; 535 -7.3; 588 -6.8; 647 -6.3; 712 -5.8; 783 -5.2; 861 -4.7; 947 -4.5; 1042 -4.7; 1146 -5.2; 1261 -5.8; 1387 -6.1; 1526 -5.9; 1678 -5.3; 1846 -4.5; 2031 -3.6; 2234 -2.8; 2457 -2.2; 2703 -1.2; 2973 -0.5; 3270 -1.3; 3597 -3.5; 3957 -3.4; 4353 -2.0; 4788 -2.1; 5267 -1.6; 5793 -0.9; 6373 -3.5; 7010 -5.1; 7711 -6.7; 8482 -6.2; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -7.6; 15026 -9.1; 16529 -8.0; 18182 -10.3; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc 4SS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc 4SS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 19 Hz    |  0.15 | 2.2 dB  |
| Peaking | 191 Hz   |  0.46 | -4.4 dB |
| Peaking | 876 Hz   |  2.42 | 2.0 dB  |
| Peaking | 2861 Hz  |  1.98 | 5.1 dB  |
| Peaking | 5430 Hz  |  3.28 | 4.5 dB  |
| Peaking | 1457 Hz  |  4.91 | -0.8 dB |
| Peaking | 2070 Hz  |  5.86 | 0.6 dB  |
| Peaking | 4422 Hz  | 10.08 | 1.5 dB  |
| Peaking | 20185 Hz |  0.45 | -7.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%204SS/qdc%204SS.png)