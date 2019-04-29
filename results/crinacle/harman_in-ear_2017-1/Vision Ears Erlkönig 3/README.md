# Vision Ears Erlkönig 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.9; 31 -2.3; 34 -2.7; 37 -3.1; 41 -3.5; 45 -3.9; 49 -4.3; 54 -4.7; 60 -5.2; 66 -5.8; 72 -6.2; 79 -6.7; 87 -7.2; 96 -7.7; 106 -8.2; 116 -8.7; 128 -9.1; 141 -9.4; 155 -9.5; 170 -9.7; 187 -9.8; 206 -9.9; 227 -9.9; 249 -9.8; 274 -9.7; 302 -9.5; 332 -9.2; 365 -8.8; 402 -8.5; 442 -8.2; 486 -7.9; 535 -7.4; 588 -7.0; 647 -6.5; 712 -6.0; 783 -5.5; 861 -5.1; 947 -4.9; 1042 -5.0; 1146 -5.5; 1261 -5.8; 1387 -5.8; 1526 -5.3; 1678 -4.7; 1846 -4.1; 2031 -3.7; 2234 -3.5; 2457 -3.3; 2703 -2.9; 2973 -2.1; 3270 -2.1; 3597 -2.6; 3957 -2.7; 4353 -2.7; 4788 -2.8; 5267 -2.3; 5793 -1.3; 6373 -1.3; 7010 -3.3; 7711 -5.5; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -10.2; 15026 -20.0; 16529 -22.7; 18182 -12.1; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears Erlkönig 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears Erlkönig 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.36 | 6.0 dB   |
| Peaking | 199 Hz   | 0.5  | -4.5 dB  |
| Peaking | 6013 Hz  | 5.13 | 2.3 dB   |
| Peaking | 6099 Hz  | 0.24 | 3.2 dB   |
| Peaking | 16122 Hz | 1.71 | -20.9 dB |
| Peaking | 1402 Hz  | 4.69 | -1.3 dB  |
| Peaking | 3127 Hz  | 3.75 | 1.2 dB   |
| Peaking | 8241 Hz  | 3.84 | -2.1 dB  |
| Peaking | 12662 Hz | 5.86 | 3.6 dB   |
| Peaking | 19273 Hz | 3.86 | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB   |
| Peaking | 62 Hz    | 1.41 | 0.0 dB   |
| Peaking | 125 Hz   | 1.41 | -3.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 16000 Hz | 1.41 | -16.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Vision%20Ears%20Erlk%C3%B6nig%203/Vision%20Ears%20Erlk%C3%B6nig%203.png)