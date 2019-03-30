# Denon AH-C751
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.6; 31 -2.1; 34 -2.6; 37 -2.9; 41 -3.3; 45 -3.6; 49 -3.8; 54 -4.0; 60 -4.1; 66 -4.2; 72 -4.4; 79 -4.5; 87 -4.5; 96 -4.5; 106 -4.2; 116 -4.2; 128 -4.1; 141 -4.0; 155 -4.3; 170 -4.5; 187 -4.5; 206 -4.5; 227 -4.5; 249 -4.5; 274 -4.2; 302 -4.2; 332 -4.0; 365 -3.7; 402 -3.5; 442 -3.3; 486 -2.9; 535 -2.7; 588 -2.5; 647 -2.2; 712 -2.1; 783 -1.9; 861 -1.9; 947 -1.9; 1042 -1.9; 1146 -1.9; 1261 -2.2; 1387 -2.5; 1526 -2.9; 1678 -3.4; 1846 -4.5; 2031 -6.6; 2234 -8.9; 2457 -11.4; 2703 -15.3; 2973 -19.0; 3270 -19.8; 3597 -17.8; 3957 -14.4; 4353 -11.7; 4788 -10.4; 5267 -10.5; 5793 -12.3; 6373 -14.1; 7010 -13.8; 7711 -10.7; 8482 -6.9; 9330 -6.5; 10263 -7.7; 11289 -8.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C751 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C751 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.85 | 5.4 dB   |
| Peaking | 228 Hz   | 0.11 | 1.7 dB   |
| Peaking | 1469 Hz  | 0.48 | 5.2 dB   |
| Peaking | 3142 Hz  | 1.75 | -17.4 dB |
| Peaking | 6654 Hz  | 3.62 | -7.1 dB  |
| Peaking | 1773 Hz  | 6.72 | 0.8 dB   |
| Peaking | 4772 Hz  | 3.54 | 2.0 dB   |
| Peaking | 4875 Hz  | 1.22 | -1.2 dB  |
| Peaking | 8934 Hz  | 4.8  | 2.0 dB   |
| Peaking | 10953 Hz | 7.45 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.1 dB   |
| Peaking | 62 Hz    | 1.41 | 1.0 dB   |
| Peaking | 125 Hz   | 1.41 | 1.9 dB   |
| Peaking | 250 Hz   | 1.41 | 1.2 dB   |
| Peaking | 500 Hz   | 1.41 | 2.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -10.9 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 16000 Hz | 1.41 | 0.4 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Denon%20AH-C751/Denon%20AH-C751.png)