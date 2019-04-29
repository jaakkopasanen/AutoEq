# Sony MH750
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.4; 25 -11.6; 28 -11.7; 31 -11.7; 34 -11.7; 37 -11.7; 41 -11.7; 45 -11.6; 49 -11.5; 54 -11.4; 60 -11.3; 66 -11.2; 72 -11.1; 79 -11.0; 87 -10.9; 96 -10.8; 106 -10.8; 116 -10.6; 128 -10.5; 141 -10.3; 155 -10.0; 170 -9.6; 187 -9.3; 206 -8.9; 227 -8.4; 249 -8.0; 274 -7.5; 302 -7.0; 332 -6.4; 365 -5.9; 402 -5.4; 442 -5.0; 486 -4.5; 535 -4.1; 588 -3.6; 647 -3.2; 712 -2.8; 783 -2.4; 861 -2.1; 947 -2.1; 1042 -2.4; 1146 -3.0; 1261 -3.5; 1387 -3.4; 1526 -3.2; 1678 -2.4; 1846 -1.9; 2031 -1.4; 2234 -0.8; 2457 -0.9; 2703 -1.3; 2973 -1.7; 3270 -2.2; 3597 -2.3; 3957 -1.8; 4353 -1.2; 4788 -0.8; 5267 -0.5; 5793 -0.7; 6373 -2.1; 7010 -3.6; 7711 -3.7; 8482 -3.9; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -9.1; 15026 -21.9; 16529 -26.6; 18182 -20.8; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH750 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.13 | -7.6 dB  |
| Peaking | 716 Hz   | 1.04 | 2.1 dB   |
| Peaking | 6601 Hz  | 0.41 | 6.9 dB   |
| Peaking | 12652 Hz | 1.71 | 12.3 dB  |
| Peaking | 16089 Hz | 0.68 | -28.3 dB |
| Peaking | 1392 Hz  | 4.64 | -1.0 dB  |
| Peaking | 2286 Hz  | 2.06 | 2.1 dB   |
| Peaking | 5383 Hz  | 0.69 | -3.5 dB  |
| Peaking | 5387 Hz  | 1.87 | 4.3 dB   |
| Peaking | 9506 Hz  | 2.01 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB  |
| Peaking | 62 Hz    | 1.41 | -5.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 16000 Hz | 1.41 | -23.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20MH750/Sony%20MH750.png)