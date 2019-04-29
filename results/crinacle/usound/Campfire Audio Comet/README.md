# Campfire Audio Comet
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.3; 25 -5.4; 28 -5.5; 31 -5.6; 34 -5.7; 37 -5.8; 41 -5.9; 45 -6.0; 49 -6.1; 54 -6.2; 60 -6.5; 66 -6.7; 72 -6.9; 79 -7.2; 87 -7.6; 96 -8.1; 106 -8.6; 116 -8.9; 128 -9.2; 141 -9.4; 155 -9.7; 170 -9.8; 187 -9.8; 206 -9.6; 227 -9.7; 249 -9.6; 274 -9.5; 302 -9.4; 332 -9.2; 365 -8.8; 402 -8.7; 442 -8.4; 486 -8.1; 535 -7.6; 588 -7.0; 647 -6.6; 712 -6.1; 783 -5.3; 861 -4.8; 947 -4.4; 1042 -4.5; 1146 -4.8; 1261 -5.3; 1387 -5.4; 1526 -4.9; 1678 -4.1; 1846 -3.3; 2031 -2.9; 2234 -2.9; 2457 -3.7; 2703 -5.5; 2973 -8.4; 3270 -9.3; 3597 -6.1; 3957 -2.6; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -2.0; 6373 -7.5; 7010 -8.6; 7711 -6.4; 8482 -7.3; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Comet GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Comet ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 217 Hz   | 0.64 | -3.4 dB  |
| Peaking | 928 Hz   | 1.94 | 2.6 dB   |
| Peaking | 2382 Hz  | 0.97 | 15.8 dB  |
| Peaking | 3076 Hz  | 0.79 | -18.8 dB |
| Peaking | 4534 Hz  | 1.66 | 13.4 dB  |
| Peaking | 24 Hz    | 1.15 | 1.3 dB   |
| Peaking | 46 Hz    | 2.12 | 0.7 dB   |
| Peaking | 5600 Hz  | 8.07 | 3.1 dB   |
| Peaking | 6619 Hz  | 7.56 | -3.8 dB  |
| Peaking | 12246 Hz | 2    | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Comet/Campfire%20Audio%20Comet.png)