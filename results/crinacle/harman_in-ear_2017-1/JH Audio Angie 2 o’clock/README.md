# JH Audio Angie 2 o’clock
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.0; 25 -5.2; 28 -5.5; 31 -5.8; 34 -6.0; 37 -6.3; 41 -6.6; 45 -6.9; 49 -7.1; 54 -7.4; 60 -7.7; 66 -8.1; 72 -8.4; 79 -8.8; 87 -9.2; 96 -9.6; 106 -10.0; 116 -10.2; 128 -10.5; 141 -10.8; 155 -10.9; 170 -11.0; 187 -11.0; 206 -11.0; 227 -11.0; 249 -10.9; 274 -10.8; 302 -10.6; 332 -10.4; 365 -10.2; 402 -10.1; 442 -9.9; 486 -9.7; 535 -9.5; 588 -9.3; 647 -9.1; 712 -8.8; 783 -8.6; 861 -8.6; 947 -9.1; 1042 -10.2; 1146 -11.5; 1261 -12.2; 1387 -12.2; 1526 -11.2; 1678 -9.4; 1846 -7.1; 2031 -4.6; 2234 -2.4; 2457 -1.1; 2703 -1.1; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.4; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.4; 15026 -15.0; 16529 -21.7; 18182 -27.8; 20000 -31.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio Angie 2 o’clock GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio Angie 2 o’clock ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.2  | 2.2 dB   |
| Peaking | 266 Hz   | 0.23 | -5.3 dB  |
| Peaking | 1390 Hz  | 1.46 | -10.9 dB |
| Peaking | 6562 Hz  | 0.13 | 10.8 dB  |
| Peaking | 19119 Hz | 0.33 | -29.5 dB |
| Peaking | 6111 Hz  | 3.96 | 2.0 dB   |
| Peaking | 8491 Hz  | 2.65 | -4.8 dB  |
| Peaking | 10171 Hz | 2.91 | 0.8 dB   |
| Peaking | 13382 Hz | 1.97 | 6.1 dB   |
| Peaking | 16212 Hz | 1.45 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB   |
| Peaking | 62 Hz    | 1.41 | -1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -17.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JH%20Audio%20Angie%202%20o%E2%80%99clock/JH%20Audio%20Angie%202%20o%E2%80%99clock.png)