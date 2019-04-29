# AKG N5005 Mid High
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -5.9; 25 -6.0; 28 -6.0; 31 -6.0; 34 -5.9; 37 -5.8; 41 -5.7; 45 -5.6; 49 -5.5; 54 -5.4; 60 -5.2; 66 -5.0; 72 -4.9; 79 -4.7; 87 -4.5; 96 -4.4; 106 -4.2; 116 -4.0; 128 -3.8; 141 -3.7; 155 -3.6; 170 -3.5; 187 -3.6; 206 -3.5; 227 -3.5; 249 -3.5; 274 -3.6; 302 -3.6; 332 -3.6; 365 -3.6; 402 -3.6; 442 -3.5; 486 -3.5; 535 -3.4; 588 -3.2; 647 -3.0; 712 -2.7; 783 -2.4; 861 -2.1; 947 -1.8; 1042 -1.9; 1146 -2.7; 1261 -3.6; 1387 -4.3; 1526 -4.6; 1678 -4.6; 1846 -4.5; 2031 -4.6; 2234 -4.6; 2457 -4.1; 2703 -3.1; 2973 -2.2; 3270 -2.3; 3597 -2.4; 3957 -2.8; 4353 -4.5; 4788 -5.6; 5267 -3.1; 5793 -0.8; 6373 -0.5; 7010 -2.9; 7711 -7.6; 8482 -5.5; 9330 -3.4; 10263 -3.4; 11289 -3.4; 12418 -3.4; 13660 -3.4; 15026 -3.9; 16529 -7.3; 18182 -8.5; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N5005 Mid High GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N5005 Mid High ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.48 | -2.7 dB |
| Peaking | 4772 Hz  | 4.89 | -4.6 dB |
| Peaking | 6501 Hz  | 1.45 | 5.1 dB  |
| Peaking | 7803 Hz  | 4.2  | -8.2 dB |
| Peaking | 17789 Hz | 1.46 | -5.9 dB |
| Peaking | 982 Hz   | 1.59 | 3.1 dB  |
| Peaking | 1595 Hz  | 0.67 | -2.4 dB |
| Peaking | 3162 Hz  | 2.35 | 1.9 dB  |
| Peaking | 14410 Hz | 3.75 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/AKG%20N5005%20Mid%20High/AKG%20N5005%20Mid%20High.png)