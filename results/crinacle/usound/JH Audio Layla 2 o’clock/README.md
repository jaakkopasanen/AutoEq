# JH Audio Layla 2 o’clock
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.8; 25 -7.1; 28 -7.4; 31 -7.7; 34 -7.9; 37 -8.0; 41 -8.2; 45 -8.4; 49 -8.6; 54 -8.8; 60 -9.0; 66 -9.2; 72 -9.5; 79 -9.7; 87 -10.0; 96 -10.2; 106 -10.4; 116 -10.7; 128 -10.8; 141 -10.8; 155 -10.9; 170 -10.9; 187 -10.9; 206 -10.9; 227 -10.7; 249 -10.6; 274 -10.5; 302 -10.3; 332 -10.2; 365 -10.0; 402 -9.9; 442 -9.8; 486 -9.6; 535 -9.5; 588 -9.3; 647 -9.0; 712 -8.7; 783 -8.2; 861 -7.8; 947 -7.6; 1042 -8.1; 1146 -8.8; 1261 -9.0; 1387 -8.4; 1526 -7.0; 1678 -5.0; 1846 -3.0; 2031 -1.3; 2234 -0.5; 2457 -0.5; 2703 -0.7; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.7; 6373 -1.0; 7010 -5.3; 7711 -9.2; 8482 -11.1; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -13.4; 20000 -17.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio Layla 2 o’clock GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio Layla 2 o’clock ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 133 Hz   | 1.17 | -0.6 dB |
| Peaking | 251 Hz   | 0.22 | -4.2 dB |
| Peaking | 1323 Hz  | 2.35 | -4.9 dB |
| Peaking | 3200 Hz  | 0.43 | 7.5 dB  |
| Peaking | 8392 Hz  | 3.28 | -8.5 dB |
| Peaking | 2176 Hz  | 3.42 | 2.0 dB  |
| Peaking | 2718 Hz  | 1.1  | -1.1 dB |
| Peaking | 6035 Hz  | 4.57 | 2.3 dB  |
| Peaking | 19241 Hz | 1.41 | -7.5 dB |
| Peaking | 20460 Hz | 0.7  | -6.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JH%20Audio%20Layla%202%20o%E2%80%99clock/JH%20Audio%20Layla%202%20o%E2%80%99clock.png)