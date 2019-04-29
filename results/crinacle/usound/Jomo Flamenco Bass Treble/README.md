# Jomo Flamenco Bass Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.7; 25 -2.1; 28 -2.6; 31 -3.0; 34 -3.3; 37 -3.6; 41 -4.0; 45 -4.3; 49 -4.6; 54 -4.9; 60 -5.2; 66 -5.6; 72 -5.9; 79 -6.3; 87 -6.8; 96 -7.2; 106 -7.6; 116 -8.0; 128 -8.2; 141 -8.5; 155 -8.7; 170 -8.8; 187 -8.8; 206 -8.8; 227 -8.7; 249 -8.5; 274 -8.3; 302 -8.1; 332 -7.8; 365 -7.4; 402 -7.0; 442 -6.5; 486 -6.0; 535 -5.4; 588 -4.7; 647 -3.9; 712 -3.0; 783 -2.1; 861 -1.2; 947 -0.6; 1042 -0.5; 1146 -0.9; 1261 -1.5; 1387 -2.1; 1526 -2.4; 1678 -2.6; 1846 -3.2; 2031 -4.0; 2234 -4.6; 2457 -4.1; 2703 -2.9; 2973 -2.3; 3270 -2.7; 3597 -3.4; 3957 -3.5; 4353 -4.1; 4788 -6.0; 5267 -8.3; 5793 -8.5; 6373 -7.9; 7010 -9.0; 7711 -8.9; 8482 -5.5; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco Bass Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco Bass Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.34 | 4.9 dB  |
| Peaking | 199 Hz  | 0.48 | -3.9 dB |
| Peaking | 999 Hz  | 1.13 | 5.4 dB  |
| Peaking | 3550 Hz | 1.53 | 3.1 dB  |
| Peaking | 6097 Hz | 1.63 | -4.4 dB |
| Peaking | 1760 Hz | 2.84 | 1.4 dB  |
| Peaking | 2368 Hz | 1.41 | -1.8 dB |
| Peaking | 2801 Hz | 4.11 | 2.0 dB  |
| Peaking | 7565 Hz | 5.73 | -4.0 dB |
| Peaking | 7983 Hz | 1.93 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Flamenco%20Bass%20Treble/Jomo%20Flamenco%20Bass%20Treble.png)