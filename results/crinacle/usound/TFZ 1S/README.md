# TFZ 1S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.4; 25 -10.6; 28 -10.8; 31 -10.9; 34 -11.0; 37 -11.0; 41 -11.1; 45 -11.1; 49 -11.2; 54 -11.2; 60 -11.2; 66 -11.3; 72 -11.4; 79 -11.5; 87 -11.5; 96 -11.6; 106 -11.6; 116 -11.6; 128 -11.5; 141 -11.4; 155 -11.2; 170 -10.9; 187 -10.6; 206 -10.2; 227 -9.8; 249 -9.4; 274 -9.0; 302 -8.5; 332 -8.2; 365 -7.8; 402 -7.5; 442 -7.2; 486 -7.0; 535 -6.7; 588 -6.4; 647 -6.1; 712 -5.9; 783 -5.9; 861 -6.0; 947 -6.3; 1042 -6.8; 1146 -7.6; 1261 -8.6; 1387 -9.5; 1526 -10.0; 1678 -10.0; 1846 -9.4; 2031 -8.0; 2234 -6.2; 2457 -4.3; 2703 -2.7; 2973 -1.8; 3270 -1.7; 3597 -2.4; 3957 -3.6; 4353 -3.6; 4788 -1.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ 1S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ 1S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.34 | -4.4 dB |
| Peaking | 151 Hz  | 0.85 | -3.1 dB |
| Peaking | 1661 Hz | 2.27 | -4.6 dB |
| Peaking | 3027 Hz | 2.06 | 5.1 dB  |
| Peaking | 5607 Hz | 2.63 | 6.3 dB  |
| Peaking | 778 Hz  | 1.9  | 1.2 dB  |
| Peaking | 1298 Hz | 5.53 | -1.0 dB |
| Peaking | 6570 Hz | 7.23 | 2.3 dB  |
| Peaking | 7691 Hz | 2.14 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/TFZ%201S/TFZ%201S.png)