# Rose Mini2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.7; 28 -2.5; 31 -3.1; 34 -3.7; 37 -4.2; 41 -4.7; 45 -5.1; 49 -5.4; 54 -5.8; 60 -6.2; 66 -6.7; 72 -7.3; 79 -7.7; 87 -8.2; 96 -8.8; 106 -9.3; 116 -9.7; 128 -10.1; 141 -10.5; 155 -10.8; 170 -10.9; 187 -11.1; 206 -11.1; 227 -11.2; 249 -11.2; 274 -11.2; 302 -11.1; 332 -11.0; 365 -10.8; 402 -10.6; 442 -10.4; 486 -10.0; 535 -9.7; 588 -9.1; 647 -8.6; 712 -8.1; 783 -7.5; 861 -6.9; 947 -6.6; 1042 -6.7; 1146 -7.1; 1261 -7.6; 1387 -7.7; 1526 -7.3; 1678 -6.6; 1846 -5.9; 2031 -5.3; 2234 -5.1; 2457 -5.2; 2703 -5.5; 2973 -4.9; 3270 -2.6; 3597 -0.6; 3957 -0.6; 4353 -0.6; 4788 -0.6; 5267 -0.9; 5793 -0.7; 6373 -1.2; 7010 -4.1; 7711 -6.3; 8482 -8.2; 9330 -6.7; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.6; 16529 -6.7; 18182 -11.7; 20000 -23.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rose Mini2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rose Mini2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.47 | 7.8 dB  |
| Peaking | 224 Hz  | 0.47 | -4.9 dB |
| Peaking | 2108 Hz | 5.05 | 1.1 dB  |
| Peaking | 3992 Hz | 2.13 | 6.2 dB  |
| Peaking | 5844 Hz | 3.48 | 5.1 dB  |
| Peaking | 14 Hz   | 0.18 | 0.2 dB  |
| Peaking | 509 Hz  | 1.98 | -0.7 dB |
| Peaking | 1007 Hz | 1.39 | 1.5 dB  |
| Peaking | 1340 Hz | 2.81 | -1.7 dB |
| Peaking | 8488 Hz | 6.22 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Rose%20Mini2/Rose%20Mini2.png)