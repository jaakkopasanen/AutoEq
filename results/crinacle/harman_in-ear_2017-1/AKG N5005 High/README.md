# AKG N5005 High
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.4; 25 -7.5; 28 -7.6; 31 -7.5; 34 -7.5; 37 -7.4; 41 -7.3; 45 -7.2; 49 -7.1; 54 -6.9; 60 -6.8; 66 -6.6; 72 -6.4; 79 -6.2; 87 -6.1; 96 -5.9; 106 -5.7; 116 -5.5; 128 -5.3; 141 -5.2; 155 -5.2; 170 -5.1; 187 -5.1; 206 -5.1; 227 -5.1; 249 -5.1; 274 -5.1; 302 -5.1; 332 -4.9; 365 -4.8; 402 -4.7; 442 -4.7; 486 -4.6; 535 -4.4; 588 -4.2; 647 -4.0; 712 -3.7; 783 -3.4; 861 -3.1; 947 -2.9; 1042 -3.0; 1146 -3.6; 1261 -4.3; 1387 -4.6; 1526 -4.5; 1678 -4.4; 1846 -4.3; 2031 -4.2; 2234 -4.1; 2457 -4.0; 2703 -3.3; 2973 -2.3; 3270 -2.2; 3597 -2.2; 3957 -2.6; 4353 -4.6; 4788 -6.8; 5267 -4.9; 5793 -1.8; 6373 -0.5; 7010 -1.7; 7711 -5.7; 8482 -5.0; 9330 -4.1; 10263 -4.1; 11289 -4.1; 12418 -5.8; 13660 -13.9; 15026 -23.0; 16529 -28.3; 18182 -26.6; 20000 -21.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N5005 High GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N5005 High ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.12 | -3.3 dB  |
| Peaking | 1704 Hz  | 2.84 | -1.1 dB  |
| Peaking | 7688 Hz  | 0.34 | 13.7 dB  |
| Peaking | 12025 Hz | 1.57 | 11.7 dB  |
| Peaking | 16294 Hz | 0.29 | -32.0 dB |
| Peaking | 936 Hz   | 4.5  | 1.2 dB   |
| Peaking | 3595 Hz  | 3.16 | 1.6 dB   |
| Peaking | 4863 Hz  | 3.89 | -5.3 dB  |
| Peaking | 6544 Hz  | 2.25 | 4.3 dB   |
| Peaking | 7757 Hz  | 5.39 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 16000 Hz | 1.41 | -28.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/AKG%20N5005%20High/AKG%20N5005%20High.png)