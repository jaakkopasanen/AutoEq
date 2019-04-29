# Acoustune HS1650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.7; 28 -8.9; 31 -9.0; 34 -9.1; 37 -9.2; 41 -9.2; 45 -9.3; 49 -9.4; 54 -9.5; 60 -9.6; 66 -9.7; 72 -9.8; 79 -10.0; 87 -10.1; 96 -10.2; 106 -10.4; 116 -10.4; 128 -10.4; 141 -10.3; 155 -10.1; 170 -9.8; 187 -9.5; 206 -9.0; 227 -8.5; 249 -8.0; 274 -7.3; 302 -6.6; 332 -6.0; 365 -5.3; 402 -4.9; 442 -4.6; 486 -4.6; 535 -4.7; 588 -5.0; 647 -5.3; 712 -5.3; 783 -5.2; 861 -5.0; 947 -5.1; 1042 -5.4; 1146 -6.0; 1261 -6.5; 1387 -6.7; 1526 -6.8; 1678 -6.8; 1846 -7.0; 2031 -7.2; 2234 -7.4; 2457 -6.9; 2703 -5.3; 2973 -3.1; 3270 -1.3; 3597 -0.5; 3957 -0.6; 4353 -1.5; 4788 -3.5; 5267 -6.1; 5793 -6.2; 6373 -2.7; 7010 -3.3; 7711 -5.6; 8482 -5.9; 9330 -6.2; 10263 -5.9; 11289 -5.9; 12418 -6.5; 13660 -17.1; 15026 -26.7; 16529 -30.3; 18182 -28.1; 20000 -17.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.52 | -3.3 dB  |
| Peaking | 112 Hz   | 1.29 | -3.1 dB  |
| Peaking | 183 Hz   | 2.2  | -2.4 dB  |
| Peaking | 10060 Hz | 0.37 | 17.5 dB  |
| Peaking | 16475 Hz | 0.47 | -36.1 dB |
| Peaking | 2173 Hz  | 1.73 | -3.1 dB  |
| Peaking | 3579 Hz  | 2.77 | 5.3 dB   |
| Peaking | 8767 Hz  | 2.18 | -2.6 dB  |
| Peaking | 12382 Hz | 3.14 | 6.1 dB   |
| Peaking | 14539 Hz | 3.47 | -5.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 16000 Hz | 1.41 | -29.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Acoustune%20HS1650/Acoustune%20HS1650.png)