# Jomo Flamenco Bass Treble sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -1.8; 25 -2.2; 28 -2.6; 31 -3.0; 34 -3.3; 37 -3.5; 41 -3.9; 45 -4.1; 49 -4.3; 54 -4.6; 60 -5.0; 66 -5.3; 72 -5.7; 79 -6.1; 87 -6.5; 96 -7.0; 106 -7.4; 116 -7.8; 128 -8.1; 141 -8.3; 155 -8.6; 170 -8.7; 187 -8.7; 206 -8.7; 227 -8.6; 249 -8.5; 274 -8.3; 302 -8.0; 332 -7.8; 365 -7.4; 402 -7.0; 442 -6.6; 486 -6.0; 535 -5.4; 588 -4.7; 647 -4.0; 712 -3.1; 783 -2.1; 861 -1.2; 947 -0.6; 1042 -0.5; 1146 -0.9; 1261 -1.6; 1387 -2.2; 1526 -2.5; 1678 -2.8; 1846 -3.4; 2031 -4.5; 2234 -5.3; 2457 -5.1; 2703 -4.2; 2973 -3.8; 3270 -4.5; 3597 -5.1; 3957 -4.0; 4353 -4.2; 4788 -6.5; 5267 -9.0; 5793 -9.2; 6373 -9.5; 7010 -11.0; 7711 -9.7; 8482 -5.7; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.8; 16529 -7.4; 18182 -5.7; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco Bass Treble sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco Bass Treble sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.25 | 4.4 dB  |
| Peaking | 205 Hz   | 0.45 | -3.6 dB |
| Peaking | 1010 Hz  | 0.98 | 5.7 dB  |
| Peaking | 4125 Hz  | 4.71 | 2.5 dB  |
| Peaking | 6504 Hz  | 2.12 | -5.3 dB |
| Peaking | 2260 Hz  | 6.97 | -1.1 dB |
| Peaking | 2914 Hz  | 6.76 | 1.4 dB  |
| Peaking | 7498 Hz  | 7.09 | -3.3 dB |
| Peaking | 8430 Hz  | 2.53 | 2.0 dB  |
| Peaking | 16457 Hz | 3.66 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Flamenco%20Bass%20Treble%20sample%201/Jomo%20Flamenco%20Bass%20Treble%20sample%201.png)