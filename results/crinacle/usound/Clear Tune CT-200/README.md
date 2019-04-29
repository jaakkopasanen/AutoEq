# Clear Tune CT-200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.9; 79 -1.5; 87 -2.2; 96 -3.0; 106 -3.7; 116 -4.3; 128 -4.8; 141 -5.4; 155 -5.8; 170 -6.2; 187 -6.4; 206 -6.7; 227 -6.8; 249 -6.9; 274 -7.0; 302 -7.0; 332 -7.0; 365 -7.0; 402 -7.0; 442 -6.9; 486 -6.8; 535 -6.7; 588 -6.5; 647 -6.3; 712 -6.0; 783 -5.7; 861 -5.5; 947 -5.5; 1042 -5.9; 1146 -6.6; 1261 -7.4; 1387 -7.9; 1526 -7.9; 1678 -7.7; 1846 -7.6; 2031 -7.6; 2234 -7.3; 2457 -6.4; 2703 -5.9; 2973 -5.8; 3270 -6.1; 3597 -6.1; 3957 -6.2; 4353 -6.5; 4788 -6.4; 5267 -6.1; 5793 -5.6; 6373 -6.1; 7010 -9.5; 7711 -10.9; 8482 -8.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.34 | 7.0 dB  |
| Peaking | 621 Hz  | 0.14 | -2.9 dB |
| Peaking | 756 Hz  | 0.9  | 3.3 dB  |
| Peaking | 4216 Hz | 0.59 | 2.1 dB  |
| Peaking | 7604 Hz | 4.75 | -5.6 dB |
| Peaking | 147 Hz  | 4.2  | -0.4 dB |
| Peaking | 1027 Hz | 2.96 | 1.5 dB  |
| Peaking | 1265 Hz | 1.31 | -1.1 dB |
| Peaking | 2764 Hz | 4.04 | 1.1 dB  |
| Peaking | 4449 Hz | 5.9  | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Clear%20Tune%20CT-200/Clear%20Tune%20CT-200.png)