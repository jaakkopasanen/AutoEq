# Campfire Audio Polaris sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.2; 25 -8.2; 28 -8.2; 31 -8.1; 34 -8.0; 37 -7.9; 41 -7.9; 45 -7.9; 49 -7.8; 54 -7.6; 60 -7.4; 66 -7.3; 72 -7.3; 79 -7.3; 87 -7.2; 96 -7.2; 106 -7.2; 116 -7.2; 128 -7.0; 141 -6.9; 155 -6.8; 170 -6.4; 187 -6.1; 206 -5.6; 227 -5.3; 249 -4.8; 274 -4.4; 302 -4.1; 332 -3.7; 365 -3.3; 402 -3.0; 442 -2.8; 486 -2.5; 535 -2.3; 588 -2.1; 647 -1.9; 712 -1.8; 783 -1.7; 861 -1.7; 947 -2.2; 1042 -3.2; 1146 -4.6; 1261 -6.0; 1387 -7.1; 1526 -7.3; 1678 -6.8; 1846 -6.3; 2031 -5.6; 2234 -4.8; 2457 -4.4; 2703 -2.6; 2973 -0.6; 3270 -0.5; 3597 -1.8; 3957 -2.6; 4353 -1.7; 4788 -2.4; 5267 -6.4; 5793 -7.5; 6373 -3.9; 7010 -4.5; 7711 -8.9; 8482 -8.8; 9330 -4.8; 10263 -4.4; 11289 -4.4; 12418 -4.4; 13660 -4.4; 15026 -4.4; 16529 -5.5; 18182 -8.2; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Polaris sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Polaris sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.48 | -3.9 dB |
| Peaking | 123 Hz   | 1.56 | -2.0 dB |
| Peaking | 3263 Hz  | 3.6  | 4.4 dB  |
| Peaking | 8127 Hz  | 5.72 | -5.8 dB |
| Peaking | 18476 Hz | 1.54 | -4.3 dB |
| Peaking | 191 Hz   | 2.16 | -0.9 dB |
| Peaking | 936 Hz   | 0.69 | 5.0 dB  |
| Peaking | 1447 Hz  | 1.27 | -6.5 dB |
| Peaking | 5180 Hz  | 2.1  | 3.6 dB  |
| Peaking | 5498 Hz  | 5.75 | -7.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Polaris%20sample%202/Campfire%20Audio%20Polaris%20sample%202.png)