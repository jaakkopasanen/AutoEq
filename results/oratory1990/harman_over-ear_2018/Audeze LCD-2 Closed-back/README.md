# Audeze LCD-2 Closed-back
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.6; 25 -4.7; 28 -4.9; 31 -5.1; 34 -5.2; 37 -5.4; 41 -5.6; 45 -5.8; 49 -6.0; 54 -6.2; 60 -6.5; 66 -6.7; 72 -6.8; 79 -7.0; 87 -7.3; 96 -7.6; 106 -8.0; 116 -8.3; 128 -8.5; 141 -8.6; 155 -8.7; 170 -8.8; 187 -8.8; 206 -8.7; 227 -8.4; 249 -8.1; 274 -7.5; 302 -6.7; 332 -5.9; 365 -5.2; 402 -5.1; 442 -5.5; 486 -5.8; 535 -6.0; 588 -6.0; 647 -6.0; 712 -5.9; 783 -5.7; 861 -6.0; 947 -6.4; 1042 -6.9; 1146 -7.2; 1261 -7.2; 1387 -8.1; 1526 -9.1; 1678 -9.0; 1846 -9.3; 2031 -9.5; 2234 -8.6; 2457 -8.0; 2703 -6.2; 2973 -3.9; 3270 -1.1; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -4.0; 5267 -6.0; 5793 -9.8; 6373 -10.7; 7010 -11.5; 7711 -10.3; 8482 -6.5; 9330 -6.5; 10263 -7.0; 11289 -13.3; 12418 -13.1; 13660 -10.3; 15026 -9.3; 16529 -11.0; 18182 -17.1; 20000 -28.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Closed-back GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Closed-back ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 159 Hz   | 1.49 | -2.6 dB  |
| Peaking | 2093 Hz  | 1.54 | -4.9 dB  |
| Peaking | 3833 Hz  | 1.42 | 8.6 dB   |
| Peaking | 6392 Hz  | 2.19 | -6.6 dB  |
| Peaking | 19971 Hz | 0.71 | -21.2 dB |
| Peaking | 24 Hz    | 1.23 | 2.1 dB   |
| Peaking | 414 Hz   | 2.41 | 1.7 dB   |
| Peaking | 9976 Hz  | 2.76 | 5.2 dB   |
| Peaking | 11570 Hz | 2.32 | -7.8 dB  |
| Peaking | 15545 Hz | 1.51 | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | -7.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-2%20Closed-back/Audeze%20LCD-2%20Closed-back.png)