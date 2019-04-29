# iBasso IT04
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -4.9; 25 -5.1; 28 -5.3; 31 -5.5; 34 -5.6; 37 -5.7; 41 -5.8; 45 -5.9; 49 -6.0; 54 -6.1; 60 -6.3; 66 -6.5; 72 -6.8; 79 -7.0; 87 -7.3; 96 -7.7; 106 -7.9; 116 -8.2; 128 -8.4; 141 -8.6; 155 -8.8; 170 -8.9; 187 -8.9; 206 -8.9; 227 -8.7; 249 -8.5; 274 -8.3; 302 -8.0; 332 -7.6; 365 -7.2; 402 -6.7; 442 -6.3; 486 -5.9; 535 -5.6; 588 -5.3; 647 -4.9; 712 -4.8; 783 -4.8; 861 -4.7; 947 -4.8; 1042 -5.1; 1146 -5.8; 1261 -6.6; 1387 -7.3; 1526 -7.6; 1678 -7.6; 1846 -7.1; 2031 -6.3; 2234 -6.1; 2457 -6.0; 2703 -4.7; 2973 -4.0; 3270 -4.6; 3597 -5.2; 3957 -3.7; 4353 -0.5; 4788 -0.5; 5267 -1.3; 5793 -2.5; 6373 -4.6; 7010 -7.9; 7711 -12.4; 8482 -11.4; 9330 -7.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iBasso IT04 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iBasso IT04 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 0.74 | 1.6 dB   |
| Peaking | 168 Hz  | 1.04 | -2.8 dB  |
| Peaking | 4651 Hz | 3.32 | 4.0 dB   |
| Peaking | 6130 Hz | 1.14 | 4.5 dB   |
| Peaking | 7839 Hz | 3.17 | -10.0 dB |
| Peaking | 303 Hz  | 1.87 | -1.0 dB  |
| Peaking | 967 Hz  | 0.71 | 2.7 dB   |
| Peaking | 1521 Hz | 1.5  | -3.4 dB  |
| Peaking | 2951 Hz | 5.29 | 1.4 dB   |
| Peaking | 3690 Hz | 8.48 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/iBasso%20IT04/iBasso%20IT04.png)