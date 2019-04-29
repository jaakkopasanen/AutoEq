# Simgot EN700 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.3; 23 -12.2; 25 -12.1; 28 -11.9; 31 -11.7; 34 -11.5; 37 -11.2; 41 -11.0; 45 -10.7; 49 -10.5; 54 -10.3; 60 -9.9; 66 -9.7; 72 -9.5; 79 -9.3; 87 -9.1; 96 -8.9; 106 -8.7; 116 -8.5; 128 -8.3; 141 -8.0; 155 -7.7; 170 -7.3; 187 -6.9; 206 -6.5; 227 -6.0; 249 -5.6; 274 -5.1; 302 -4.6; 332 -4.0; 365 -3.5; 402 -3.0; 442 -2.6; 486 -2.3; 535 -1.9; 588 -1.5; 647 -1.3; 712 -0.9; 783 -0.6; 861 -0.5; 947 -0.6; 1042 -1.1; 1146 -1.7; 1261 -2.3; 1387 -2.5; 1526 -2.4; 1678 -2.2; 1846 -2.1; 2031 -2.1; 2234 -2.2; 2457 -2.7; 2703 -3.4; 2973 -3.3; 3270 -2.5; 3597 -1.8; 3957 -1.8; 4353 -2.9; 4788 -5.1; 5267 -7.0; 5793 -4.6; 6373 -0.9; 7010 -0.8; 7711 -3.0; 8482 -3.2; 9330 -3.3; 10263 -3.3; 11289 -3.3; 12418 -3.3; 13660 -5.5; 15026 -17.3; 16529 -22.0; 18182 -14.7; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Simgot EN700 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Simgot EN700 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.58 | -7.2 dB  |
| Peaking | 92 Hz    | 0.32 | -4.9 dB  |
| Peaking | 850 Hz   | 0.53 | 3.4 dB   |
| Peaking | 1338 Hz  | 2.19 | -1.7 dB  |
| Peaking | 16623 Hz | 2.04 | -21.4 dB |
| Peaking | 3971 Hz  | 4.68 | 2.0 dB   |
| Peaking | 5308 Hz  | 3.63 | -4.9 dB  |
| Peaking | 6581 Hz  | 4.38 | 4.6 dB   |
| Peaking | 13320 Hz | 1.81 | 6.4 dB   |
| Peaking | 15066 Hz | 2.81 | -8.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.2 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 16000 Hz | 1.41 | -17.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Simgot%20EN700%20Pro/Simgot%20EN700%20Pro.png)