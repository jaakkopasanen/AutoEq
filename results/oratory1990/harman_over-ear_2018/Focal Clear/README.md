# Focal Clear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.9; 28 -1.2; 31 -1.4; 34 -1.6; 37 -1.8; 41 -2.0; 45 -2.2; 49 -2.3; 54 -2.6; 60 -2.9; 66 -3.1; 72 -3.4; 79 -3.7; 87 -4.1; 96 -4.5; 106 -4.8; 116 -5.1; 128 -5.4; 141 -5.6; 155 -5.7; 170 -5.8; 187 -5.8; 206 -5.8; 227 -5.7; 249 -5.6; 274 -5.4; 302 -5.2; 332 -5.0; 365 -4.8; 402 -4.6; 442 -4.6; 486 -4.6; 535 -4.5; 588 -4.5; 647 -4.6; 712 -4.9; 783 -5.2; 861 -5.7; 947 -6.2; 1042 -6.8; 1146 -7.4; 1261 -7.9; 1387 -7.9; 1526 -7.3; 1678 -6.3; 1846 -5.3; 2031 -4.5; 2234 -4.0; 2457 -4.3; 2703 -4.8; 2973 -5.4; 3270 -5.1; 3597 -4.8; 3957 -1.6; 4353 -0.5; 4788 -0.9; 5267 -1.5; 5793 -4.9; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.4; 13660 -6.5; 15026 -6.5; 16529 -7.3; 18182 -10.5; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Clear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Clear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 20 Hz    |  0.6  | 5.5 dB  |
| Peaking | 58 Hz    |  0.79 | 2.3 dB  |
| Peaking | 473 Hz   |  1.33 | 2.2 dB  |
| Peaking | 2251 Hz  |  4.81 | 2.2 dB  |
| Peaking | 4702 Hz  |  2.06 | 6.1 dB  |
| Peaking | 715 Hz   |  3.68 | 0.8 dB  |
| Peaking | 1299 Hz  |  3.41 | -2.1 dB |
| Peaking | 5916 Hz  | 11.33 | -2.4 dB |
| Peaking | 6506 Hz  |  9.21 | 3.8 dB  |
| Peaking | 19670 Hz |  0.99 | -6.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Clear/Focal%20Clear.png)