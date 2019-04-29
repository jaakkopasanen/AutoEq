# Jomo Flamenco Bass Treble sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.5; 25 -2.0; 28 -2.6; 31 -3.1; 34 -3.4; 37 -3.7; 41 -4.1; 45 -4.4; 49 -4.8; 54 -5.1; 60 -5.4; 66 -5.8; 72 -6.2; 79 -6.5; 87 -7.0; 96 -7.4; 106 -7.8; 116 -8.2; 128 -8.4; 141 -8.7; 155 -8.7; 170 -8.8; 187 -8.9; 206 -9.0; 227 -8.8; 249 -8.6; 274 -8.4; 302 -8.1; 332 -7.8; 365 -7.4; 402 -6.9; 442 -6.5; 486 -5.9; 535 -5.3; 588 -4.6; 647 -3.9; 712 -3.0; 783 -2.1; 861 -1.2; 947 -0.6; 1042 -0.5; 1146 -0.9; 1261 -1.5; 1387 -2.0; 1526 -2.2; 1678 -2.5; 1846 -2.9; 2031 -3.6; 2234 -3.9; 2457 -3.0; 2703 -1.7; 2973 -0.9; 3270 -1.0; 3597 -1.7; 3957 -3.0; 4353 -4.0; 4788 -5.4; 5267 -7.7; 5793 -7.7; 6373 -6.3; 7010 -6.9; 7711 -8.0; 8482 -5.6; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco Bass Treble sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco Bass Treble sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.53 | 5.2 dB  |
| Peaking | 194 Hz  | 0.47 | -4.2 dB |
| Peaking | 995 Hz  | 1.15 | 5.1 dB  |
| Peaking | 3313 Hz | 1.91 | 4.6 dB  |
| Peaking | 5809 Hz | 1.48 | -3.3 dB |
| Peaking | 15 Hz   | 0.23 | 0.2 dB  |
| Peaking | 1695 Hz | 5.22 | 0.5 dB  |
| Peaking | 2194 Hz | 6.72 | -1.0 dB |
| Peaking | 7739 Hz | 5.75 | -3.7 dB |
| Peaking | 7980 Hz | 2.11 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Flamenco%20Bass%20Treble%20sample%202/Jomo%20Flamenco%20Bass%20Treble%20sample%202.png)