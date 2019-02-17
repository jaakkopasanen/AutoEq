# Adam SP-5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.2; 31 -2.2; 34 -3.1; 37 -4.0; 41 -5.0; 45 -5.9; 49 -6.8; 54 -7.6; 60 -8.4; 66 -8.9; 72 -9.2; 79 -8.6; 87 -8.2; 96 -7.7; 106 -7.3; 116 -7.8; 128 -7.9; 141 -8.3; 155 -8.2; 170 -7.8; 187 -6.9; 206 -6.8; 227 -6.2; 249 -5.4; 274 -4.9; 302 -4.4; 332 -4.6; 365 -6.1; 402 -5.1; 442 -4.6; 486 -4.4; 535 -4.3; 588 -4.3; 647 -4.5; 712 -4.8; 783 -5.2; 861 -5.7; 947 -6.3; 1042 -6.7; 1146 -6.8; 1261 -6.3; 1387 -7.8; 1526 -8.7; 1678 -9.1; 1846 -9.2; 2031 -9.0; 2234 -8.7; 2457 -8.0; 2703 -7.5; 2973 -0.6; 3270 -5.7; 3597 -5.3; 3957 -3.3; 4353 -2.7; 4788 -1.3; 5267 -7.0; 5793 -17.5; 6373 -12.4; 7010 -4.9; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -7.5; 11289 -13.0; 12418 -17.7; 13660 -15.4; 15026 -9.6; 16529 -8.7; 18182 -9.4; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Adam SP-5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Adam SP-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 24 Hz    |  2.21 | 6.6 dB   |
| Peaking | 4802 Hz  |  3    | 7.9 dB   |
| Peaking | 5840 Hz  |  5.5  | -16.7 dB |
| Peaking | 9270 Hz  |  0.99 | 4.7 dB   |
| Peaking | 12555 Hz |  1.73 | -14.0 dB |
| Peaking | 94 Hz    |  0.76 | -2.0 dB  |
| Peaking | 291 Hz   |  3.5  | 2.0 dB   |
| Peaking | 576 Hz   |  1.31 | 2.5 dB   |
| Peaking | 1965 Hz  |  1.45 | -3.3 dB  |
| Peaking | 2952 Hz  | 10.79 | 7.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -6.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Adam%20SP-5/Adam%20SP-5.png)