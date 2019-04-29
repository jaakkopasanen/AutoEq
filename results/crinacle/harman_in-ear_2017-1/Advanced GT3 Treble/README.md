# Advanced GT3 Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.1; 25 -7.2; 28 -7.3; 31 -7.3; 34 -7.2; 37 -7.1; 41 -7.1; 45 -7.1; 49 -7.1; 54 -7.1; 60 -7.1; 66 -7.2; 72 -7.3; 79 -7.4; 87 -7.5; 96 -7.8; 106 -8.0; 116 -8.2; 128 -8.4; 141 -8.5; 155 -8.6; 170 -8.7; 187 -8.7; 206 -8.6; 227 -8.5; 249 -8.3; 274 -8.1; 302 -7.8; 332 -7.4; 365 -7.0; 402 -6.6; 442 -6.2; 486 -5.7; 535 -5.2; 588 -4.7; 647 -4.1; 712 -3.5; 783 -2.9; 861 -2.4; 947 -2.2; 1042 -2.3; 1146 -2.6; 1261 -2.9; 1387 -2.7; 1526 -2.1; 1678 -1.6; 1846 -1.1; 2031 -0.8; 2234 -0.5; 2457 -0.9; 2703 -2.2; 2973 -4.3; 3270 -6.4; 3597 -6.9; 3957 -5.8; 4353 -5.2; 4788 -6.7; 5267 -9.3; 5793 -10.8; 6373 -7.9; 7010 -5.5; 7711 -8.0; 8482 -11.2; 9330 -9.3; 10263 -5.8; 11289 -5.7; 12418 -9.3; 13660 -20.0; 15026 -28.8; 16529 -31.6; 18182 -33.2; 20000 -37.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT3 Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT3 Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 183 Hz   | 0.36 | -3.0 dB  |
| Peaking | 913 Hz   | 0.88 | 4.0 dB   |
| Peaking | 2154 Hz  | 2.3  | 5.1 dB   |
| Peaking | 16431 Hz | 1.48 | -18.4 dB |
| Peaking | 19408 Hz | 0.9  | -29.0 dB |
| Peaking | 5707 Hz  | 4.6  | -5.0 dB  |
| Peaking | 7055 Hz  | 5.15 | 3.0 dB   |
| Peaking | 8591 Hz  | 3.87 | -5.4 dB  |
| Peaking | 11528 Hz | 1.58 | 9.1 dB   |
| Peaking | 14352 Hz | 3.11 | -7.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 16000 Hz | 1.41 | -35.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Advanced%20GT3%20Treble/Advanced%20GT3%20Treble.png)