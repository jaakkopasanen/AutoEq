# Vision Ears Erlkönig 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.4; 25 -1.9; 28 -2.4; 31 -2.8; 34 -3.2; 37 -3.5; 41 -4.0; 45 -4.5; 49 -4.9; 54 -5.3; 60 -5.8; 66 -6.3; 72 -6.7; 79 -7.1; 87 -7.7; 96 -8.2; 106 -8.7; 116 -9.2; 128 -9.5; 141 -9.8; 155 -10.0; 170 -10.1; 187 -10.3; 206 -10.4; 227 -10.4; 249 -10.2; 274 -10.1; 302 -9.9; 332 -9.6; 365 -9.2; 402 -8.9; 442 -8.6; 486 -8.2; 535 -7.8; 588 -7.4; 647 -6.9; 712 -6.4; 783 -5.9; 861 -5.4; 947 -5.3; 1042 -5.4; 1146 -5.9; 1261 -6.2; 1387 -6.2; 1526 -5.7; 1678 -5.1; 1846 -4.5; 2031 -4.1; 2234 -3.9; 2457 -3.7; 2703 -3.2; 2973 -2.4; 3270 -2.3; 3597 -2.8; 3957 -2.6; 4353 -2.7; 4788 -2.8; 5267 -2.3; 5793 -1.0; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -8.3; 15026 -18.6; 16529 -23.9; 18182 -11.1; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears Erlkönig 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears Erlkönig 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.39 | 5.9 dB   |
| Peaking | 197 Hz   | 0.52 | -4.8 dB  |
| Peaking | 4003 Hz  | 0.58 | 3.5 dB   |
| Peaking | 6176 Hz  | 5.38 | 3.6 dB   |
| Peaking | 16365 Hz | 2.25 | -20.6 dB |
| Peaking | 900 Hz   | 2.98 | 1.2 dB   |
| Peaking | 1355 Hz  | 3.44 | -1.2 dB  |
| Peaking | 8043 Hz  | 4.63 | -1.5 dB  |
| Peaking | 13123 Hz | 2.52 | 4.0 dB   |
| Peaking | 15086 Hz | 3.92 | -4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB   |
| Peaking | 62 Hz    | 1.41 | -0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 16000 Hz | 1.41 | -15.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Vision%20Ears%20Erlk%C3%B6nig%204/Vision%20Ears%20Erlk%C3%B6nig%204.png)