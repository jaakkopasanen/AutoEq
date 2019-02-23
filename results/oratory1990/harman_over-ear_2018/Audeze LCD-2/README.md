# Audeze LCD-2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -3.8; 25 -3.8; 28 -3.8; 31 -3.9; 34 -4.1; 37 -4.2; 41 -4.5; 45 -4.8; 49 -5.0; 54 -5.1; 60 -5.3; 66 -5.5; 72 -5.7; 79 -6.0; 87 -6.3; 96 -6.7; 106 -7.0; 116 -7.4; 128 -7.8; 141 -8.1; 155 -8.4; 170 -8.6; 187 -8.7; 206 -8.9; 227 -9.0; 249 -9.0; 274 -8.9; 302 -8.8; 332 -8.5; 365 -8.0; 402 -7.9; 442 -8.2; 486 -8.5; 535 -8.7; 588 -8.9; 647 -8.8; 712 -8.5; 783 -8.1; 861 -8.6; 947 -8.7; 1042 -8.4; 1146 -7.7; 1261 -6.9; 1387 -7.4; 1526 -7.5; 1678 -6.1; 1846 -5.2; 2031 -4.6; 2234 -4.5; 2457 -6.2; 2703 -6.2; 2973 -6.1; 3270 -4.6; 3597 -2.6; 3957 -0.9; 4353 -0.5; 4788 -1.4; 5267 -5.5; 5793 -7.4; 6373 -5.7; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -8.2; 12418 -10.3; 13660 -9.9; 15026 -10.4; 16529 -13.1; 18182 -15.2; 20000 -17.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 21 Hz    |  0.35 | 2.8 dB   |
| Peaking | 206 Hz   |  0.73 | -2.6 dB  |
| Peaking | 736 Hz   |  1.18 | -2.0 dB  |
| Peaking | 4207 Hz  |  2.63 | 6.7 dB   |
| Peaking | 19374 Hz |  0.49 | -10.3 dB |
| Peaking | 2053 Hz  |  2.91 | 4.1 dB   |
| Peaking | 2164 Hz  |  1.24 | -2.0 dB  |
| Peaking | 6944 Hz  | 11.29 | 2.5 dB   |
| Peaking | 10528 Hz |  2.89 | 2.0 dB   |
| Peaking | 12119 Hz |  3.67 | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -8.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-2/Audeze%20LCD-2.png)