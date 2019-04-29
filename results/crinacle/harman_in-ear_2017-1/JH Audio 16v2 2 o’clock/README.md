# JH Audio 16v2 2 o’clock
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.6; 23 -8.8; 25 -9.0; 28 -9.2; 31 -9.4; 34 -9.6; 37 -9.8; 41 -10.1; 45 -10.3; 49 -10.5; 54 -10.7; 60 -11.0; 66 -11.4; 72 -11.7; 79 -12.1; 87 -12.5; 96 -12.9; 106 -13.2; 116 -13.5; 128 -13.8; 141 -14.0; 155 -14.2; 170 -14.2; 187 -14.2; 206 -14.1; 227 -14.0; 249 -13.9; 274 -13.6; 302 -13.3; 332 -12.9; 365 -12.4; 402 -12.1; 442 -11.6; 486 -11.2; 535 -10.6; 588 -10.0; 647 -9.4; 712 -8.7; 783 -8.0; 861 -7.3; 947 -6.8; 1042 -6.7; 1146 -6.9; 1261 -6.7; 1387 -6.0; 1526 -4.8; 1678 -3.4; 1846 -2.2; 2031 -1.1; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -9.1; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -15.3; 16529 -19.9; 18182 -23.0; 20000 -27.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio 16v2 2 o’clock GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio 16v2 2 o’clock ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.79 | -0.8 dB  |
| Peaking | 185 Hz   | 0.48 | -4.6 dB  |
| Peaking | 284 Hz   | 0.11 | -3.4 dB  |
| Peaking | 3248 Hz  | 0.43 | 8.2 dB   |
| Peaking | 19292 Hz | 0.59 | -20.7 dB |
| Peaking | 1317 Hz  | 6.23 | -1.5 dB  |
| Peaking | 6131 Hz  | 4.54 | 2.3 dB   |
| Peaking | 8775 Hz  | 2.2  | -4.0 dB  |
| Peaking | 13427 Hz | 1.49 | 7.1 dB   |
| Peaking | 15625 Hz | 1.62 | -6.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -6.0 dB  |
| Peaking | 250 Hz   | 1.41 | -6.4 dB  |
| Peaking | 500 Hz   | 1.41 | -3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -15.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JH%20Audio%2016v2%202%20o%E2%80%99clock/JH%20Audio%2016v2%202%20o%E2%80%99clock.png)