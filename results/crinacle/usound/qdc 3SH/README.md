# qdc 3SH
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.3; 25 -7.4; 28 -7.5; 31 -7.7; 34 -7.8; 37 -7.9; 41 -8.0; 45 -8.1; 49 -8.2; 54 -8.3; 60 -8.5; 66 -8.9; 72 -9.2; 79 -9.5; 87 -9.8; 96 -10.3; 106 -10.6; 116 -10.9; 128 -11.2; 141 -11.5; 155 -11.7; 170 -11.7; 187 -11.8; 206 -11.8; 227 -11.7; 249 -11.5; 274 -11.3; 302 -11.0; 332 -10.8; 365 -10.5; 402 -10.1; 442 -9.8; 486 -9.4; 535 -8.9; 588 -8.5; 647 -8.0; 712 -7.4; 783 -6.9; 861 -6.5; 947 -6.3; 1042 -6.5; 1146 -7.2; 1261 -8.1; 1387 -8.6; 1526 -8.3; 1678 -7.6; 1846 -6.3; 2031 -4.2; 2234 -1.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -3.7; 7010 -6.0; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.8; 15026 -9.3; 16529 -6.6; 18182 -6.5; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc 3SH GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc 3SH ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 100 Hz   | 0.32 | -1.3 dB |
| Peaking | 212 Hz   | 0.53 | -4.4 dB |
| Peaking | 1597 Hz  | 2.21 | -4.5 dB |
| Peaking | 2683 Hz  | 1.09 | 6.7 dB  |
| Peaking | 5092 Hz  | 2.56 | 4.8 dB  |
| Peaking | 894 Hz   | 4.61 | 1.1 dB  |
| Peaking | 4107 Hz  | 4.83 | 1.6 dB  |
| Peaking | 5954 Hz  | 5.4  | 4.0 dB  |
| Peaking | 6117 Hz  | 1.48 | -2.4 dB |
| Peaking | 14814 Hz | 3.9  | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%203SH/qdc%203SH.png)