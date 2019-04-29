# JH Audio Layla 2 o’clock
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.0; 25 -8.3; 28 -8.6; 31 -8.8; 34 -9.0; 37 -9.2; 41 -9.4; 45 -9.5; 49 -9.7; 54 -9.9; 60 -10.1; 66 -10.3; 72 -10.6; 79 -10.8; 87 -11.1; 96 -11.4; 106 -11.6; 116 -11.8; 128 -12.0; 141 -12.0; 155 -12.0; 170 -12.1; 187 -12.0; 206 -12.0; 227 -11.9; 249 -11.7; 274 -11.6; 302 -11.4; 332 -11.2; 365 -10.9; 402 -10.7; 442 -10.6; 486 -10.4; 535 -10.2; 588 -9.9; 647 -9.7; 712 -9.3; 783 -8.9; 861 -8.5; 947 -8.4; 1042 -8.9; 1146 -9.5; 1261 -9.5; 1387 -8.5; 1526 -6.9; 1678 -4.9; 1846 -2.8; 2031 -0.8; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.5; 8482 -9.3; 9330 -9.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.9; 15026 -18.2; 16529 -24.8; 18182 -29.9; 20000 -29.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio Layla 2 o’clock GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio Layla 2 o’clock ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 55 Hz    | 0.37 | -1.7 dB  |
| Peaking | 325 Hz   | 0.25 | -5.5 dB  |
| Peaking | 1270 Hz  | 1.97 | -5.9 dB  |
| Peaking | 7791 Hz  | 0.15 | 13.3 dB  |
| Peaking | 18504 Hz | 0.33 | -32.6 dB |
| Peaking | 686 Hz   | 3.73 | -0.6 dB  |
| Peaking | 6152 Hz  | 4.41 | 2.1 dB   |
| Peaking | 8608 Hz  | 2.87 | -5.8 dB  |
| Peaking | 12931 Hz | 1.59 | 7.1 dB   |
| Peaking | 15555 Hz | 1.59 | -5.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 16000 Hz | 1.41 | -21.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JH%20Audio%20Layla%202%20o%E2%80%99clock/JH%20Audio%20Layla%202%20o%E2%80%99clock.png)