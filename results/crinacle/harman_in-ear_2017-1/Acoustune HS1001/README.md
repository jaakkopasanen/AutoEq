# Acoustune HS1001
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.7; 23 -12.8; 25 -12.9; 28 -13.0; 31 -13.1; 34 -13.1; 37 -13.1; 41 -13.1; 45 -13.1; 49 -13.1; 54 -13.1; 60 -13.1; 66 -13.1; 72 -13.2; 79 -13.2; 87 -13.3; 96 -13.4; 106 -13.3; 116 -13.3; 128 -13.2; 141 -13.0; 155 -12.8; 170 -12.5; 187 -12.1; 206 -11.6; 227 -11.1; 249 -10.6; 274 -10.0; 302 -9.3; 332 -8.6; 365 -7.8; 402 -7.1; 442 -6.5; 486 -5.7; 535 -5.0; 588 -4.2; 647 -3.4; 712 -2.7; 783 -1.9; 861 -1.3; 947 -1.1; 1042 -1.3; 1146 -1.8; 1261 -2.2; 1387 -2.4; 1526 -2.3; 1678 -2.0; 1846 -1.6; 2031 -1.1; 2234 -0.6; 2457 -0.5; 2703 -0.8; 2973 -1.2; 3270 -1.3; 3597 -1.1; 3957 -1.2; 4353 -1.9; 4788 -3.6; 5267 -6.7; 5793 -9.6; 6373 -7.2; 7010 -4.8; 7711 -6.3; 8482 -7.6; 9330 -5.9; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -14.0; 15026 -25.0; 16529 -27.5; 18182 -21.5; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1001 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 65 Hz    | 0.15 | -7.9 dB  |
| Peaking | 819 Hz   | 0.7  | 5.6 dB   |
| Peaking | 2493 Hz  | 1.49 | 4.3 dB   |
| Peaking | 3934 Hz  | 3.59 | 3.6 dB   |
| Peaking | 16693 Hz | 1.51 | -24.6 dB |
| Peaking | 2643 Hz  | 2.76 | -0.2 dB  |
| Peaking | 5826 Hz  | 5.05 | -6.8 dB  |
| Peaking | 5955 Hz  | 1.78 | 2.2 dB   |
| Peaking | 12462 Hz | 1.89 | 8.4 dB   |
| Peaking | 14722 Hz | 2.53 | -9.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -5.3 dB  |
| Peaking | 125 Hz   | 1.41 | -6.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -23.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Acoustune%20HS1001/Acoustune%20HS1001.png)