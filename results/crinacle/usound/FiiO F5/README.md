# FiiO F5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.1; 25 -3.2; 28 -3.4; 31 -3.5; 34 -3.6; 37 -3.7; 41 -3.8; 45 -4.0; 49 -4.1; 54 -4.2; 60 -4.4; 66 -4.7; 72 -5.0; 79 -5.3; 87 -5.6; 96 -6.0; 106 -6.3; 116 -6.6; 128 -6.7; 141 -6.9; 155 -7.0; 170 -7.0; 187 -6.9; 206 -6.7; 227 -6.5; 249 -6.4; 274 -6.2; 302 -5.8; 332 -5.5; 365 -5.1; 402 -4.7; 442 -4.2; 486 -3.8; 535 -3.3; 588 -3.0; 647 -2.3; 712 -1.6; 783 -1.2; 861 -0.8; 947 -0.6; 1042 -0.8; 1146 -1.4; 1261 -2.1; 1387 -2.7; 1526 -2.9; 1678 -3.0; 1846 -3.2; 2031 -3.8; 2234 -4.6; 2457 -4.9; 2703 -3.9; 2973 -2.4; 3270 -1.1; 3597 -0.5; 3957 -0.6; 4353 -1.7; 4788 -4.1; 5267 -6.4; 5793 -4.6; 6373 -2.0; 7010 -2.8; 7711 -5.1; 8482 -3.7; 9330 -3.7; 10263 -3.7; 11289 -3.7; 12418 -3.7; 13660 -3.7; 15026 -3.7; 16529 -3.7; 18182 -3.7; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FiiO F5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FiiO F5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 172 Hz  | 0.63 | -3.5 dB |
| Peaking | 894 Hz  | 1.33 | 3.4 dB  |
| Peaking | 2473 Hz | 2.67 | -2.9 dB |
| Peaking | 3661 Hz | 1.53 | 3.8 dB  |
| Peaking | 5217 Hz | 5.68 | -4.6 dB |
| Peaking | 22 Hz   | 0.91 | 0.8 dB  |
| Peaking | 6611 Hz | 7.96 | 2.2 dB  |
| Peaking | 7671 Hz | 6.8  | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FiiO%20F5/FiiO%20F5.png)