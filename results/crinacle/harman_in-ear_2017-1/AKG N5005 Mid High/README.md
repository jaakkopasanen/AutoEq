# AKG N5005 Mid High
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.6; 28 -8.7; 31 -8.7; 34 -8.6; 37 -8.5; 41 -8.4; 45 -8.3; 49 -8.2; 54 -8.1; 60 -7.8; 66 -7.7; 72 -7.5; 79 -7.3; 87 -7.2; 96 -7.0; 106 -6.8; 116 -6.6; 128 -6.5; 141 -6.4; 155 -6.3; 170 -6.2; 187 -6.2; 206 -6.2; 227 -6.2; 249 -6.2; 274 -6.2; 302 -6.2; 332 -6.0; 365 -5.9; 402 -5.9; 442 -5.9; 486 -5.7; 535 -5.6; 588 -5.4; 647 -5.2; 712 -4.9; 783 -4.6; 861 -4.4; 947 -4.1; 1042 -4.3; 1146 -4.9; 1261 -5.6; 1387 -6.0; 1526 -6.0; 1678 -5.9; 1846 -5.8; 2031 -5.6; 2234 -5.0; 2457 -3.9; 2703 -2.5; 2973 -1.5; 3270 -1.6; 3597 -1.9; 3957 -2.7; 4353 -4.8; 4788 -6.2; 5267 -3.7; 5793 -1.2; 6373 -0.5; 7010 -2.4; 7711 -6.2; 8482 -5.4; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -5.4; 13660 -12.3; 15026 -21.6; 16529 -27.7; 18182 -26.5; 20000 -16.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N5005 Mid High GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N5005 Mid High ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.3  | -3.8 dB  |
| Peaking | 309 Hz   | 0.82 | -1.0 dB  |
| Peaking | 6703 Hz  | 0.57 | 8.7 dB   |
| Peaking | 12250 Hz | 1.53 | 12.6 dB  |
| Peaking | 16726 Hz | 0.41 | -27.0 dB |
| Peaking | 1873 Hz  | 1.86 | -2.1 dB  |
| Peaking | 3132 Hz  | 2    | 2.8 dB   |
| Peaking | 4780 Hz  | 3.72 | -5.6 dB  |
| Peaking | 6485 Hz  | 1.67 | 3.8 dB   |
| Peaking | 7753 Hz  | 4.72 | -4.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 16000 Hz | 1.41 | -25.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/AKG%20N5005%20Mid%20High/AKG%20N5005%20Mid%20High.png)