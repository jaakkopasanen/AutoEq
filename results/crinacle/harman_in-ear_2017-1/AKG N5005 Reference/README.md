# AKG N5005 Reference
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -9.9; 28 -10.0; 31 -10.0; 34 -9.9; 37 -9.8; 41 -9.7; 45 -9.6; 49 -9.4; 54 -9.3; 60 -9.0; 66 -8.8; 72 -8.7; 79 -8.5; 87 -8.4; 96 -8.2; 106 -8.0; 116 -7.8; 128 -7.7; 141 -7.5; 155 -7.5; 170 -7.4; 187 -7.5; 206 -7.5; 227 -7.5; 249 -7.5; 274 -7.5; 302 -7.5; 332 -7.4; 365 -7.3; 402 -7.2; 442 -7.1; 486 -7.1; 535 -6.9; 588 -6.7; 647 -6.5; 712 -6.2; 783 -6.0; 861 -5.7; 947 -5.5; 1042 -5.7; 1146 -6.4; 1261 -7.1; 1387 -7.5; 1526 -7.5; 1678 -7.4; 1846 -7.2; 2031 -6.4; 2234 -5.0; 2457 -3.2; 2703 -1.4; 2973 -0.5; 3270 -1.0; 3597 -1.6; 3957 -2.7; 4353 -4.8; 4788 -5.5; 5267 -2.8; 5793 -0.9; 6373 -0.6; 7010 -3.2; 7711 -7.0; 8482 -6.2; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -11.2; 15026 -21.4; 16529 -28.8; 18182 -27.2; 20000 -12.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N5005 Reference GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N5005 Reference ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.05 | -3.0 dB  |
| Peaking | 1637 Hz  | 1.57 | -5.0 dB  |
| Peaking | 5439 Hz  | 0.32 | 7.2 dB   |
| Peaking | 12458 Hz | 1.75 | 10.5 dB  |
| Peaking | 16823 Hz | 0.6  | -27.8 dB |
| Peaking | 29 Hz    | 1.55 | -1.4 dB  |
| Peaking | 2980 Hz  | 4.89 | 2.2 dB   |
| Peaking | 4657 Hz  | 3.9  | -5.2 dB  |
| Peaking | 6334 Hz  | 1.98 | 4.2 dB   |
| Peaking | 7734 Hz  | 5.07 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 16000 Hz | 1.41 | -24.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/AKG%20N5005%20Reference/AKG%20N5005%20Reference.png)