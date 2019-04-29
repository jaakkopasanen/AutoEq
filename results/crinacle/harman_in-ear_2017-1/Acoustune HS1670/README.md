# Acoustune HS1670
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.0; 25 -5.2; 28 -5.5; 31 -5.7; 34 -5.9; 37 -6.0; 41 -6.2; 45 -6.3; 49 -6.5; 54 -6.8; 60 -7.0; 66 -7.3; 72 -7.5; 79 -7.8; 87 -8.1; 96 -8.4; 106 -8.7; 116 -8.8; 128 -9.0; 141 -9.1; 155 -9.2; 170 -9.1; 187 -8.9; 206 -8.6; 227 -8.2; 249 -7.8; 274 -7.4; 302 -6.9; 332 -6.2; 365 -5.5; 402 -5.0; 442 -4.7; 486 -4.4; 535 -4.4; 588 -4.6; 647 -4.9; 712 -5.1; 783 -5.0; 861 -5.1; 947 -5.3; 1042 -5.7; 1146 -6.4; 1261 -6.9; 1387 -7.2; 1526 -7.2; 1678 -7.2; 1846 -7.4; 2031 -7.6; 2234 -7.6; 2457 -6.9; 2703 -5.2; 2973 -3.0; 3270 -1.4; 3597 -0.6; 3957 -0.5; 4353 -1.4; 4788 -3.4; 5267 -6.3; 5793 -7.5; 6373 -3.8; 7010 -3.3; 7711 -5.5; 8482 -6.1; 9330 -6.2; 10263 -5.8; 11289 -5.8; 12418 -7.4; 13660 -18.8; 15026 -27.9; 16529 -30.7; 18182 -27.8; 20000 -17.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1670 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1670 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 150 Hz   | 0.76 | -3.8 dB  |
| Peaking | 2341 Hz  | 0.55 | -16.4 dB |
| Peaking | 3380 Hz  | 0.43 | 25.1 dB  |
| Peaking | 11649 Hz | 1.01 | 17.7 dB  |
| Peaking | 15643 Hz | 0.37 | -35.3 dB |
| Peaking | 19 Hz    | 1.81 | 1.2 dB   |
| Peaking | 4369 Hz  | 3.72 | 1.4 dB   |
| Peaking | 5673 Hz  | 3.64 | -4.4 dB  |
| Peaking | 6675 Hz  | 5.16 | 5.0 dB   |
| Peaking | 11731 Hz | 4.01 | -0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB   |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 16000 Hz | 1.41 | -30.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Acoustune%20HS1670/Acoustune%20HS1670.png)