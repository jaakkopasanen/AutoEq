# Campfire Audio Polaris
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -7.9; 25 -7.9; 28 -7.8; 31 -7.8; 34 -7.7; 37 -7.6; 41 -7.6; 45 -7.5; 49 -7.4; 54 -7.3; 60 -7.2; 66 -7.2; 72 -7.2; 79 -7.2; 87 -7.1; 96 -7.1; 106 -7.1; 116 -7.0; 128 -6.9; 141 -6.8; 155 -6.6; 170 -6.3; 187 -6.0; 206 -5.5; 227 -5.1; 249 -4.7; 274 -4.3; 302 -3.9; 332 -3.5; 365 -3.1; 402 -2.7; 442 -2.4; 486 -2.1; 535 -1.9; 588 -1.6; 647 -1.4; 712 -1.2; 783 -1.1; 861 -1.1; 947 -1.3; 1042 -2.2; 1146 -3.5; 1261 -4.9; 1387 -6.0; 1526 -6.5; 1678 -6.6; 1846 -6.6; 2031 -6.3; 2234 -5.6; 2457 -4.8; 2703 -2.6; 2973 -0.6; 3270 -0.5; 3597 -1.7; 3957 -2.6; 4353 -1.9; 4788 -1.9; 5267 -4.8; 5793 -6.9; 6373 -4.9; 7010 -6.0; 7711 -9.7; 8482 -7.8; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -4.3; 18182 -6.3; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Polaris GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Polaris ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.29 | -3.7 dB |
| Peaking | 131 Hz  | 1.16 | -1.8 dB |
| Peaking | 645 Hz  | 1.46 | 3.4 dB  |
| Peaking | 3271 Hz | 4.29 | 4.2 dB  |
| Peaking | 7832 Hz | 5.05 | -6.1 dB |
| Peaking | 375 Hz  | 3.37 | 0.8 dB  |
| Peaking | 965 Hz  | 3.41 | 2.4 dB  |
| Peaking | 1660 Hz | 1.55 | -3.3 dB |
| Peaking | 5003 Hz | 2.11 | 3.6 dB  |
| Peaking | 5629 Hz | 5.02 | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Polaris/Campfire%20Audio%20Polaris.png)