# Advanced GT3 Superbass Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.9; 25 -10.0; 28 -10.0; 31 -10.0; 34 -10.0; 37 -9.9; 41 -9.8; 45 -9.7; 49 -9.6; 54 -9.4; 60 -9.3; 66 -9.3; 72 -9.4; 79 -9.5; 87 -9.5; 96 -9.8; 106 -9.9; 116 -10.1; 128 -10.2; 141 -10.3; 155 -10.5; 170 -10.5; 187 -10.6; 206 -10.6; 227 -10.6; 249 -10.5; 274 -10.5; 302 -10.4; 332 -10.4; 365 -10.3; 402 -10.2; 442 -10.0; 486 -9.8; 535 -9.9; 588 -9.5; 647 -9.0; 712 -8.5; 783 -8.1; 861 -7.7; 947 -7.4; 1042 -7.3; 1146 -7.4; 1261 -7.6; 1387 -7.3; 1526 -6.7; 1678 -5.6; 1846 -4.4; 2031 -3.4; 2234 -2.5; 2457 -2.0; 2703 -2.0; 2973 -2.4; 3270 -3.4; 3597 -4.7; 3957 -6.5; 4353 -7.2; 4788 -4.7; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.6; 16529 -12.7; 18182 -15.1; 20000 -15.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT3 Superbass Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT3 Superbass Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.6  | -3.2 dB  |
| Peaking | 245 Hz   | 0.33 | -4.1 dB  |
| Peaking | 2492 Hz  | 2.02 | 5.2 dB   |
| Peaking | 5918 Hz  | 3.5  | 6.8 dB   |
| Peaking | 19017 Hz | 0.79 | -10.3 dB |
| Peaking | 1368 Hz  | 7.11 | -0.8 dB  |
| Peaking | 3294 Hz  | 3.89 | 1.4 dB   |
| Peaking | 4283 Hz  | 3.5  | -2.8 dB  |
| Peaking | 5154 Hz  | 8.2  | 2.5 dB   |
| Peaking | 13052 Hz | 3.3  | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -6.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20GT3%20Superbass%20Treble/Advanced%20GT3%20Superbass%20Treble.png)