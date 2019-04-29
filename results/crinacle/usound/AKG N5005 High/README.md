# AKG N5005 High
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -4.7; 25 -4.8; 28 -4.9; 31 -4.9; 34 -4.8; 37 -4.7; 41 -4.6; 45 -4.5; 49 -4.4; 54 -4.3; 60 -4.1; 66 -3.9; 72 -3.7; 79 -3.6; 87 -3.4; 96 -3.2; 106 -3.0; 116 -2.9; 128 -2.7; 141 -2.6; 155 -2.5; 170 -2.4; 187 -2.5; 206 -2.4; 227 -2.4; 249 -2.5; 274 -2.5; 302 -2.5; 332 -2.4; 365 -2.4; 402 -2.4; 442 -2.3; 486 -2.3; 535 -2.2; 588 -2.0; 647 -1.8; 712 -1.5; 783 -1.2; 861 -0.9; 947 -0.6; 1042 -0.7; 1146 -1.4; 1261 -2.3; 1387 -2.9; 1526 -3.1; 1678 -3.1; 1846 -3.0; 2031 -3.2; 2234 -3.7; 2457 -4.2; 2703 -3.9; 2973 -3.1; 3270 -2.9; 3597 -2.6; 3957 -2.7; 4353 -4.3; 4788 -6.1; 5267 -4.2; 5793 -1.4; 6373 -0.5; 7010 -2.5; 7711 -7.2; 8482 -5.2; 9330 -2.6; 10263 -2.6; 11289 -2.6; 12418 -2.6; 13660 -3.5; 15026 -5.2; 16529 -7.9; 18182 -8.7; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N5005 High GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N5005 High ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.67 | -2.4 dB |
| Peaking | 930 Hz   | 1.61 | 2.5 dB  |
| Peaking | 2748 Hz  | 0.39 | -1.1 dB |
| Peaking | 17055 Hz | 1.79 | -4.4 dB |
| Peaking | 19450 Hz | 0.99 | -5.4 dB |
| Peaking | 3820 Hz  | 4.16 | 1.4 dB  |
| Peaking | 4869 Hz  | 4.43 | -4.0 dB |
| Peaking | 6417 Hz  | 2.73 | 4.2 dB  |
| Peaking | 7853 Hz  | 4.25 | -7.0 dB |
| Peaking | 9126 Hz  | 1.49 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -5.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/AKG%20N5005%20High/AKG%20N5005%20High.png)