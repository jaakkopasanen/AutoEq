# Jomo Flamenco Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.5; 25 -4.8; 28 -5.2; 31 -5.6; 34 -5.9; 37 -6.2; 41 -6.5; 45 -6.7; 49 -7.0; 54 -7.3; 60 -7.6; 66 -8.0; 72 -8.4; 79 -8.8; 87 -9.2; 96 -9.7; 106 -10.1; 116 -10.4; 128 -10.7; 141 -11.0; 155 -11.2; 170 -11.4; 187 -11.4; 206 -11.4; 227 -11.3; 249 -11.1; 274 -10.9; 302 -10.7; 332 -10.4; 365 -10.0; 402 -9.5; 442 -9.1; 486 -8.5; 535 -7.9; 588 -7.1; 647 -6.3; 712 -5.3; 783 -4.3; 861 -3.2; 947 -2.5; 1042 -2.2; 1146 -2.4; 1261 -2.9; 1387 -3.2; 1526 -3.3; 1678 -3.3; 1846 -3.6; 2031 -4.7; 2234 -5.8; 2457 -5.8; 2703 -5.1; 2973 -4.8; 3270 -5.6; 3597 -6.1; 3957 -3.3; 4353 -0.5; 4788 -0.9; 5267 -5.3; 5793 -5.2; 6373 -5.9; 7010 -6.7; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.9; 16529 -10.0; 18182 -7.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.29 | 2.8 dB  |
| Peaking | 228 Hz   | 0.34 | -5.4 dB |
| Peaking | 1051 Hz  | 0.81 | 5.8 dB  |
| Peaking | 4306 Hz  | 0.86 | -1.0 dB |
| Peaking | 4497 Hz  | 4.02 | 7.2 dB  |
| Peaking | 1356 Hz  | 4.16 | -1.0 dB |
| Peaking | 1820 Hz  | 1.67 | 1.7 dB  |
| Peaking | 2375 Hz  | 1.76 | -2.0 dB |
| Peaking | 2835 Hz  | 5.34 | 2.0 dB  |
| Peaking | 16543 Hz | 2.43 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Flamenco%20Bass/Jomo%20Flamenco%20Bass.png)