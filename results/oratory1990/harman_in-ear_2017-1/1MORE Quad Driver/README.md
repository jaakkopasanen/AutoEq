# 1MORE Quad Driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -3.0; 25 -3.6; 28 -4.0; 31 -4.6; 34 -5.3; 37 -5.8; 41 -6.5; 45 -7.0; 49 -7.5; 54 -8.3; 60 -9.0; 66 -9.8; 72 -10.2; 79 -10.9; 87 -11.1; 96 -11.4; 106 -12.0; 116 -12.0; 128 -12.5; 141 -12.4; 155 -12.5; 170 -12.5; 187 -12.5; 206 -12.5; 227 -12.3; 249 -12.0; 274 -11.7; 302 -11.3; 332 -10.8; 365 -10.2; 402 -9.7; 442 -9.1; 486 -8.5; 535 -7.9; 588 -7.2; 647 -6.5; 712 -5.8; 783 -5.0; 861 -4.4; 947 -4.0; 1042 -4.0; 1146 -4.2; 1261 -4.3; 1387 -4.2; 1526 -4.0; 1678 -3.6; 1846 -3.3; 2031 -3.0; 2234 -2.8; 2457 -2.8; 2703 -2.9; 2973 -2.6; 3270 -2.2; 3597 -2.3; 3957 -3.6; 4353 -5.0; 4788 -4.5; 5267 -2.7; 5793 -0.9; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.1; 12418 -10.9; 13660 -20.5; 15026 -29.6; 16529 -33.3; 18182 -32.2; 20000 -25.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Quad Driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Quad Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.74 | 4.9 dB   |
| Peaking | 167 Hz   | 0.4  | -7.2 dB  |
| Peaking | 6549 Hz  | 0.24 | 22.0 dB  |
| Peaking | 11500 Hz | 1.86 | 11.2 dB  |
| Peaking | 16171 Hz | 0.22 | -40.0 dB |
| Peaking | 898 Hz   | 4.53 | 1.1 dB   |
| Peaking | 4522 Hz  | 4.53 | -3.4 dB  |
| Peaking | 6283 Hz  | 4.12 | 3.4 dB   |
| Peaking | 7515 Hz  | 4.93 | -1.8 dB  |
| Peaking | 14590 Hz | 7.54 | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB   |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -5.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 10.7 dB  |
| Peaking | 16000 Hz | 1.41 | -36.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/1MORE%20Quad%20Driver/1MORE%20Quad%20Driver.png)