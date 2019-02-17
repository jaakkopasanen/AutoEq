# Audeze LCD-X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.1; 31 -1.8; 34 -2.3; 37 -2.8; 41 -3.3; 45 -3.5; 49 -3.6; 54 -3.7; 60 -3.8; 66 -4.0; 72 -4.2; 79 -4.4; 87 -4.8; 96 -5.2; 106 -5.6; 116 -6.0; 128 -6.4; 141 -6.7; 155 -7.0; 170 -7.2; 187 -7.4; 206 -7.5; 227 -7.6; 249 -7.6; 274 -7.6; 302 -7.4; 332 -7.2; 365 -7.0; 402 -6.9; 442 -6.9; 486 -7.0; 535 -6.9; 588 -6.8; 647 -6.8; 712 -6.8; 783 -6.8; 861 -6.8; 947 -6.6; 1042 -6.4; 1146 -6.1; 1261 -6.0; 1387 -6.2; 1526 -5.9; 1678 -5.4; 1846 -5.1; 2031 -5.3; 2234 -5.1; 2457 -4.7; 2703 -4.0; 2973 -3.9; 3270 -3.8; 3597 -3.8; 3957 -3.7; 4353 -2.7; 4788 -2.8; 5267 -2.2; 5793 -2.2; 6373 -3.0; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.4; 13660 -9.3; 15026 -9.5; 16529 -12.5; 18182 -17.9; 20000 -25.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.91 | 5.9 dB   |
| Peaking | 71 Hz    | 0.91 | 1.9 dB   |
| Peaking | 210 Hz   | 0.7  | -1.4 dB  |
| Peaking | 3185 Hz  | 1.17 | 2.5 dB   |
| Peaking | 5558 Hz  | 2.58 | 4.0 dB   |
| Peaking | 391 Hz   | 6.41 | 0.2 dB   |
| Peaking | 1751 Hz  | 7.14 | 0.5 dB   |
| Peaking | 13944 Hz | 0.48 | 1.8 dB   |
| Peaking | 19784 Hz | 0.56 | -18.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -8.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-X/Audeze%20LCD-X.png)