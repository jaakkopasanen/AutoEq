# FitEar Private 223
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -1.6; 25 -1.6; 28 -1.7; 31 -1.9; 34 -2.0; 37 -2.1; 41 -2.3; 45 -2.4; 49 -2.6; 54 -2.8; 60 -3.0; 66 -3.4; 72 -4.0; 79 -4.5; 87 -4.6; 96 -5.1; 106 -5.8; 116 -6.0; 128 -6.2; 141 -6.5; 155 -6.9; 170 -7.2; 187 -7.3; 206 -7.3; 227 -7.4; 249 -7.3; 274 -7.3; 302 -7.2; 332 -7.0; 365 -6.7; 402 -6.6; 442 -6.4; 486 -6.2; 535 -6.0; 588 -5.7; 647 -5.5; 712 -5.1; 783 -4.9; 861 -4.8; 947 -5.0; 1042 -5.5; 1146 -6.4; 1261 -7.2; 1387 -7.7; 1526 -8.1; 1678 -8.3; 1846 -7.7; 2031 -5.9; 2234 -4.8; 2457 -4.3; 2703 -2.8; 2973 -0.9; 3270 -0.5; 3597 -1.9; 3957 -5.4; 4353 -6.2; 4788 -6.7; 5267 -11.3; 5793 -15.0; 6373 -10.8; 7010 -8.2; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -10.1; 11289 -9.9; 12418 -9.6; 13660 -19.2; 15026 -27.6; 16529 -19.4; 18182 -7.8; 20000 -13.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Private 223 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Private 223 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 1.04 | 4.7 dB   |
| Peaking | 54 Hz    | 1.81 | 2.5 dB   |
| Peaking | 3186 Hz  | 3.21 | 6.7 dB   |
| Peaking | 5799 Hz  | 5.82 | -9.4 dB  |
| Peaking | 15181 Hz | 2.41 | -23.8 dB |
| Peaking | 232 Hz   | 1.14 | -1.4 dB  |
| Peaking | 831 Hz   | 1.9  | 1.7 dB   |
| Peaking | 1553 Hz  | 2.84 | -2.8 dB  |
| Peaking | 8554 Hz  | 3.03 | 2.4 dB   |
| Peaking | 14187 Hz | 9.51 | -4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB   |
| Peaking | 62 Hz    | 1.41 | 2.3 dB   |
| Peaking | 125 Hz   | 1.41 | -0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -19.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20Private%20223/FitEar%20Private%20223.png)