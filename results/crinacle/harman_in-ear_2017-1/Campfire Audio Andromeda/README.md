# Campfire Audio Andromeda
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.9; 25 -7.1; 28 -7.4; 31 -7.7; 34 -7.8; 37 -8.0; 41 -8.2; 45 -8.4; 49 -8.6; 54 -8.8; 60 -9.1; 66 -9.4; 72 -9.7; 79 -10.1; 87 -10.4; 96 -10.8; 106 -11.2; 116 -11.6; 128 -11.9; 141 -12.1; 155 -12.3; 170 -12.4; 187 -12.5; 206 -12.5; 227 -12.4; 249 -12.3; 274 -12.1; 302 -11.9; 332 -11.5; 365 -11.1; 402 -10.8; 442 -10.4; 486 -9.9; 535 -9.4; 588 -8.8; 647 -8.2; 712 -7.5; 783 -6.8; 861 -6.3; 947 -5.9; 1042 -5.9; 1146 -6.2; 1261 -6.5; 1387 -6.4; 1526 -6.0; 1678 -5.5; 1846 -4.7; 2031 -3.3; 2234 -1.4; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -2.8; 7010 -5.2; 7711 -6.2; 8482 -7.1; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.7; 15026 -24.7; 16529 -27.9; 18182 -24.2; 20000 -14.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 194 Hz   | 0.56 | -3.9 dB  |
| Peaking | 306 Hz   | 0.14 | -2.4 dB  |
| Peaking | 9908 Hz  | 0.16 | 10.2 dB  |
| Peaking | 16140 Hz | 0.77 | -28.1 dB |
| Peaking | 18413 Hz | 1.18 | -9.0 dB  |
| Peaking | 892 Hz   | 2.38 | 1.7 dB   |
| Peaking | 1689 Hz  | 1.28 | -4.5 dB  |
| Peaking | 2271 Hz  | 1.11 | 3.7 dB   |
| Peaking | 8125 Hz  | 2.68 | -3.4 dB  |
| Peaking | 12291 Hz | 4.39 | 5.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -5.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 16000 Hz | 1.41 | -24.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Andromeda/Campfire%20Audio%20Andromeda.png)