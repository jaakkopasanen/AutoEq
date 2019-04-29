# Dita Fealty
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.6; 25 -5.0; 28 -5.4; 31 -5.7; 34 -6.0; 37 -6.2; 41 -6.5; 45 -6.8; 49 -6.9; 54 -7.2; 60 -7.5; 66 -7.7; 72 -8.0; 79 -8.3; 87 -8.5; 96 -8.9; 106 -9.2; 116 -9.4; 128 -9.5; 141 -9.7; 155 -9.8; 170 -9.7; 187 -9.7; 206 -9.6; 227 -9.5; 249 -9.3; 274 -9.1; 302 -9.0; 332 -8.8; 365 -8.5; 402 -8.3; 442 -8.1; 486 -7.8; 535 -7.5; 588 -7.2; 647 -6.9; 712 -6.5; 783 -6.0; 861 -5.6; 947 -5.4; 1042 -5.5; 1146 -5.8; 1261 -6.2; 1387 -5.8; 1526 -4.6; 1678 -4.0; 1846 -2.8; 2031 -1.8; 2234 -1.0; 2457 -0.5; 2703 -0.5; 2973 -0.9; 3270 -1.5; 3597 -2.4; 3957 -3.4; 4353 -4.7; 4788 -6.2; 5267 -7.2; 5793 -5.6; 6373 -3.5; 7010 -3.6; 7711 -7.4; 8482 -8.7; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -7.4; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dita Fealty GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dita Fealty ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.89 | 2.9 dB  |
| Peaking | 170 Hz   | 0.45 | -3.6 dB |
| Peaking | 2737 Hz  | 1.13 | 6.5 dB  |
| Peaking | 6451 Hz  | 1.37 | -5.2 dB |
| Peaking | 6595 Hz  | 4    | 7.9 dB  |
| Peaking | 922 Hz   | 3.56 | 0.9 dB  |
| Peaking | 1309 Hz  | 4.35 | -1.3 dB |
| Peaking | 2026 Hz  | 5.82 | 0.5 dB  |
| Peaking | 17542 Hz | 0.65 | 1.4 dB  |
| Peaking | 19831 Hz | 0.92 | -5.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Dita%20Fealty/Dita%20Fealty.png)