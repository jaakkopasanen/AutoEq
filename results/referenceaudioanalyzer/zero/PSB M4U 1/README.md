# PSB M4U 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -9.8; 25 -9.4; 28 -9.0; 31 -8.7; 34 -8.4; 37 -8.2; 41 -8.0; 45 -7.9; 49 -7.8; 54 -7.9; 60 -7.9; 66 -7.9; 72 -8.4; 79 -9.1; 87 -9.7; 96 -9.8; 106 -9.9; 116 -10.1; 128 -10.1; 141 -9.8; 155 -9.6; 170 -9.2; 187 -8.6; 206 -8.0; 227 -7.2; 249 -6.5; 274 -5.9; 302 -5.2; 332 -4.3; 365 -3.8; 402 -3.3; 442 -2.5; 486 -1.7; 535 -1.1; 588 -0.8; 647 -0.7; 712 -0.7; 783 -0.7; 861 -0.7; 947 -0.7; 1042 -0.7; 1146 -0.7; 1261 -0.6; 1387 -0.5; 1526 -0.6; 1678 -1.3; 1846 -2.7; 2031 -4.6; 2234 -6.6; 2457 -8.6; 2703 -10.4; 2973 -11.7; 3270 -12.5; 3597 -12.7; 3957 -12.4; 4353 -12.1; 4788 -12.3; 5267 -12.4; 5793 -12.9; 6373 -12.8; 7010 -10.1; 7711 -6.1; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PSB M4U 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 16 Hz   | 0.65 | -4.8 dB  |
| Peaking | 94 Hz   | 1.68 | -2.0 dB  |
| Peaking | 156 Hz  | 0.95 | -4.0 dB  |
| Peaking | 1230 Hz | 0.39 | 7.9 dB   |
| Peaking | 3628 Hz | 0.8  | -11.3 dB |
| Peaking | 1741 Hz | 2.01 | 3.6 dB   |
| Peaking | 1986 Hz | 0.82 | -2.5 dB  |
| Peaking | 4006 Hz | 2.68 | 2.0 dB   |
| Peaking | 6480 Hz | 2.52 | -6.6 dB  |
| Peaking | 7510 Hz | 1.51 | 4.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -9.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/PSB%20M4U%201/PSB%20M4U%201.png)