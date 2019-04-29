# Lime Ears Model X Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.6; 25 -4.8; 28 -5.0; 31 -5.2; 34 -5.4; 37 -5.5; 41 -5.7; 45 -5.9; 49 -6.1; 54 -6.3; 60 -6.5; 66 -6.8; 72 -7.2; 79 -7.5; 87 -7.9; 96 -8.3; 106 -8.7; 116 -9.1; 128 -9.4; 141 -9.6; 155 -9.8; 170 -9.9; 187 -10.0; 206 -10.1; 227 -10.0; 249 -9.9; 274 -9.7; 302 -9.6; 332 -9.3; 365 -9.0; 402 -8.7; 442 -8.4; 486 -7.9; 535 -7.5; 588 -7.0; 647 -6.4; 712 -5.7; 783 -5.0; 861 -4.3; 947 -3.9; 1042 -3.8; 1146 -4.1; 1261 -4.6; 1387 -4.8; 1526 -4.5; 1678 -4.0; 1846 -3.6; 2031 -3.4; 2234 -3.3; 2457 -2.4; 2703 -1.0; 2973 -0.5; 3270 -1.0; 3597 -2.0; 3957 -1.7; 4353 -2.3; 4788 -4.6; 5267 -4.1; 5793 -1.7; 6373 -1.0; 7010 -3.4; 7711 -7.5; 8482 -8.6; 9330 -6.5; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Model X Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Model X Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 219 Hz  | 0.53 | -4.4 dB |
| Peaking | 946 Hz  | 1.76 | 2.5 dB  |
| Peaking | 3055 Hz | 1.34 | 5.1 dB  |
| Peaking | 6379 Hz | 3.96 | 5.1 dB  |
| Peaking | 8124 Hz | 3.88 | -4.1 dB |
| Peaking | 15 Hz   | 0.69 | 0.2 dB  |
| Peaking | 22 Hz   | 0.92 | 1.3 dB  |
| Peaking | 471 Hz  | 3.44 | -0.2 dB |
| Peaking | 1778 Hz | 8.14 | 0.6 dB  |
| Peaking | 9655 Hz | 6.16 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Lime%20Ears%20Model%20X%20Bass/Lime%20Ears%20Model%20X%20Bass.png)