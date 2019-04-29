# Campfire Audio Polaris sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -7.7; 25 -7.6; 28 -7.6; 31 -7.5; 34 -7.5; 37 -7.4; 41 -7.4; 45 -7.3; 49 -7.2; 54 -7.2; 60 -7.1; 66 -7.1; 72 -7.2; 79 -7.1; 87 -7.1; 96 -7.1; 106 -7.1; 116 -7.0; 128 -6.9; 141 -6.7; 155 -6.5; 170 -6.2; 187 -5.9; 206 -5.5; 227 -5.1; 249 -4.7; 274 -4.3; 302 -3.8; 332 -3.4; 365 -3.0; 402 -2.5; 442 -2.2; 486 -1.8; 535 -1.5; 588 -1.3; 647 -1.0; 712 -0.8; 783 -0.6; 861 -0.5; 947 -0.5; 1042 -1.2; 1146 -2.5; 1261 -4.0; 1387 -5.0; 1526 -5.9; 1678 -6.6; 1846 -7.1; 2031 -7.1; 2234 -6.5; 2457 -5.3; 2703 -2.7; 2973 -0.7; 3270 -0.6; 3597 -1.7; 3957 -2.8; 4353 -2.1; 4788 -1.5; 5267 -3.3; 5793 -6.3; 6373 -6.0; 7010 -7.6; 7711 -10.5; 8482 -6.8; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -4.0; 18182 -4.5; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Polaris sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Polaris sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.13 | -3.5 dB |
| Peaking | 875 Hz   | 0.56 | 5.6 dB  |
| Peaking | 1999 Hz  | 0.92 | -8.6 dB |
| Peaking | 3067 Hz  | 1.43 | 6.9 dB  |
| Peaking | 7579 Hz  | 4.4  | -7.0 dB |
| Peaking | 3967 Hz  | 5.31 | -1.6 dB |
| Peaking | 4840 Hz  | 3.14 | 2.5 dB  |
| Peaking | 5838 Hz  | 6.4  | -3.0 dB |
| Peaking | 9295 Hz  | 6.97 | 1.3 dB  |
| Peaking | 19793 Hz | 1.83 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Polaris%20sample%201/Campfire%20Audio%20Polaris%20sample%201.png)