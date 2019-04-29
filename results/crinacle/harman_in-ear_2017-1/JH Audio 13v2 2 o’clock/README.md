# JH Audio 13v2 2 o’clock
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -8.9; 25 -8.9; 28 -9.0; 31 -9.0; 34 -9.1; 37 -9.3; 41 -9.4; 45 -9.5; 49 -9.6; 54 -9.8; 60 -10.1; 66 -10.3; 72 -10.5; 79 -10.7; 87 -11.0; 96 -11.4; 106 -11.6; 116 -11.7; 128 -11.9; 141 -12.0; 155 -11.9; 170 -11.9; 187 -11.8; 206 -11.6; 227 -11.3; 249 -11.1; 274 -10.8; 302 -10.4; 332 -10.0; 365 -9.5; 402 -9.1; 442 -8.7; 486 -8.3; 535 -7.8; 588 -7.3; 647 -6.8; 712 -6.3; 783 -5.8; 861 -5.5; 947 -5.4; 1042 -5.6; 1146 -5.8; 1261 -5.9; 1387 -5.8; 1526 -5.5; 1678 -5.2; 1846 -5.1; 2031 -5.0; 2234 -4.9; 2457 -4.8; 2703 -3.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.3; 6373 -4.0; 7010 -8.9; 7711 -12.7; 8482 -9.9; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.3; 15026 -21.1; 16529 -30.1; 18182 -34.7; 20000 -28.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio 13v2 2 o’clock GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio 13v2 2 o’clock ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.14 | -2.0 dB  |
| Peaking | 176 Hz   | 0.49 | -4.2 dB  |
| Peaking | 7783 Hz  | 3.13 | -15.0 dB |
| Peaking | 8810 Hz  | 0.4  | 19.3 dB  |
| Peaking | 17955 Hz | 0.45 | -36.2 dB |
| Peaking | 2493 Hz  | 1.62 | -3.6 dB  |
| Peaking | 3065 Hz  | 2.45 | 4.2 dB   |
| Peaking | 4721 Hz  | 2.7  | 1.6 dB   |
| Peaking | 13081 Hz | 2.52 | 10.8 dB  |
| Peaking | 14389 Hz | 0.9  | -6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 16000 Hz | 1.41 | -25.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JH%20Audio%2013v2%202%20o%E2%80%99clock/JH%20Audio%2013v2%202%20o%E2%80%99clock.png)