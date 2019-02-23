# Campfire Audio Andromeda
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.4; 25 -5.7; 28 -6.1; 31 -6.4; 34 -6.6; 37 -6.8; 41 -7.1; 45 -7.4; 49 -7.6; 54 -7.9; 60 -8.2; 66 -8.6; 72 -8.9; 79 -9.3; 87 -9.6; 96 -10.0; 106 -10.4; 116 -10.7; 128 -11.0; 141 -11.2; 155 -11.3; 170 -11.4; 187 -11.3; 206 -11.3; 227 -11.2; 249 -11.1; 274 -11.2; 302 -11.1; 332 -10.8; 365 -10.4; 402 -10.1; 442 -9.8; 486 -9.4; 535 -8.9; 588 -8.4; 647 -8.0; 712 -7.6; 783 -7.0; 861 -6.8; 947 -6.7; 1042 -6.7; 1146 -6.8; 1261 -6.9; 1387 -6.7; 1526 -6.5; 1678 -6.0; 1846 -5.2; 2031 -3.9; 2234 -2.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -3.0; 4788 -2.9; 5267 -2.0; 5793 -4.1; 6373 -5.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.7; 15026 -24.7; 16529 -24.3; 18182 -18.1; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.68 | 2.6 dB   |
| Peaking | 178 Hz   | 0.56 | -2.8 dB  |
| Peaking | 365 Hz   | 0.19 | -2.5 dB  |
| Peaking | 8714 Hz  | 0.19 | 9.0 dB   |
| Peaking | 16068 Hz | 0.78 | -27.2 dB |
| Peaking | 1705 Hz  | 1.31 | -6.3 dB  |
| Peaking | 2313 Hz  | 0.69 | 6.7 dB   |
| Peaking | 5748 Hz  | 0.45 | -3.6 dB  |
| Peaking | 12499 Hz | 1.87 | 7.4 dB   |
| Peaking | 14379 Hz | 3.6  | -6.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB   |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 16000 Hz | 1.41 | -21.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Campfire%20Audio%20Andromeda/Campfire%20Audio%20Andromeda.png)