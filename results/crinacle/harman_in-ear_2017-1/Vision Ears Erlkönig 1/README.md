# Vision Ears Erlkönig 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.4; 25 -10.6; 28 -10.9; 31 -11.1; 34 -11.2; 37 -11.3; 41 -11.5; 45 -11.7; 49 -11.8; 54 -12.0; 60 -12.2; 66 -12.4; 72 -12.6; 79 -12.8; 87 -13.1; 96 -13.3; 106 -13.4; 116 -13.6; 128 -13.7; 141 -13.6; 155 -13.5; 170 -13.4; 187 -13.2; 206 -13.0; 227 -12.5; 249 -12.1; 274 -11.6; 302 -11.1; 332 -10.5; 365 -9.8; 402 -9.2; 442 -8.6; 486 -7.9; 535 -7.2; 588 -6.5; 647 -5.8; 712 -5.1; 783 -4.5; 861 -3.9; 947 -3.8; 1042 -3.9; 1146 -4.4; 1261 -4.8; 1387 -4.8; 1526 -4.4; 1678 -3.8; 1846 -3.2; 2031 -2.9; 2234 -2.6; 2457 -2.5; 2703 -2.0; 2973 -1.0; 3270 -1.1; 3597 -1.7; 3957 -1.9; 4353 -2.0; 4788 -2.0; 5267 -1.6; 5793 -0.5; 6373 -0.7; 7010 -3.6; 7711 -5.8; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -9.8; 15026 -19.5; 16529 -23.2; 18182 -13.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears Erlkönig 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears Erlkönig 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 55 Hz    | 0.25 | -5.0 dB  |
| Peaking | 214 Hz   | 0.53 | -5.2 dB  |
| Peaking | 3219 Hz  | 0.08 | 2.6 dB   |
| Peaking | 4269 Hz  | 0.84 | 2.6 dB   |
| Peaking | 16280 Hz | 1.67 | -21.0 dB |
| Peaking | 1398 Hz  | 5.95 | -1.2 dB  |
| Peaking | 6354 Hz  | 3.74 | 4.8 dB   |
| Peaking | 7356 Hz  | 1.57 | -3.4 dB  |
| Peaking | 12863 Hz | 2.68 | 4.0 dB   |
| Peaking | 14776 Hz | 4.19 | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -6.4 dB  |
| Peaking | 250 Hz   | 1.41 | -5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 16000 Hz | 1.41 | -16.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Vision%20Ears%20Erlk%C3%B6nig%201/Vision%20Ears%20Erlk%C3%B6nig%201.png)