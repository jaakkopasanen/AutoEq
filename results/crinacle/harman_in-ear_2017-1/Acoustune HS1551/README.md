# Acoustune HS1551
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.7; 25 -7.0; 28 -7.3; 31 -7.7; 34 -7.9; 37 -8.1; 41 -8.4; 45 -8.6; 49 -8.8; 54 -9.0; 60 -9.3; 66 -9.6; 72 -9.8; 79 -10.2; 87 -10.4; 96 -10.8; 106 -11.2; 116 -11.4; 128 -11.5; 141 -11.6; 155 -11.7; 170 -11.6; 187 -11.5; 206 -11.3; 227 -11.0; 249 -10.7; 274 -10.4; 302 -9.9; 332 -9.3; 365 -8.8; 402 -8.3; 442 -7.9; 486 -7.4; 535 -6.9; 588 -6.5; 647 -6.0; 712 -5.6; 783 -5.2; 861 -5.1; 947 -5.2; 1042 -5.8; 1146 -6.7; 1261 -7.6; 1387 -8.3; 1526 -8.7; 1678 -8.9; 1846 -8.8; 2031 -7.8; 2234 -5.9; 2457 -3.3; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.8; 5267 -6.4; 5793 -9.3; 6373 -4.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.3; 15026 -22.2; 16529 -24.5; 18182 -24.2; 20000 -19.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1551 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1551 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 129 Hz   | 0.52 | -5.2 dB  |
| Peaking | 271 Hz   | 0.95 | -2.6 dB  |
| Peaking | 1947 Hz  | 0.48 | -29.9 dB |
| Peaking | 2406 Hz  | 0.31 | 30.0 dB  |
| Peaking | 17501 Hz | 0.59 | -22.3 dB |
| Peaking | 852 Hz   | 4.83 | 1.1 dB   |
| Peaking | 4442 Hz  | 3.03 | 2.0 dB   |
| Peaking | 5617 Hz  | 6.25 | -7.6 dB  |
| Peaking | 12479 Hz | 2.54 | 6.8 dB   |
| Peaking | 14803 Hz | 2.67 | -6.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 16000 Hz | 1.41 | -21.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Acoustune%20HS1551/Acoustune%20HS1551.png)