# Focal Elear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.8; 25 -3.2; 28 -3.5; 31 -3.7; 34 -3.9; 37 -4.1; 41 -4.3; 45 -4.4; 49 -4.6; 54 -4.7; 60 -4.9; 66 -5.1; 72 -5.4; 79 -5.7; 87 -6.0; 96 -6.4; 106 -6.7; 116 -7.0; 128 -7.2; 141 -7.3; 155 -7.4; 170 -7.5; 187 -7.5; 206 -7.5; 227 -7.4; 249 -7.3; 274 -7.1; 302 -6.8; 332 -6.5; 365 -6.3; 402 -6.1; 442 -6.1; 486 -6.1; 535 -6.2; 588 -6.2; 647 -6.0; 712 -6.1; 783 -6.3; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.5; 1261 -6.7; 1387 -6.5; 1526 -6.6; 1678 -5.7; 1846 -4.1; 2031 -2.5; 2234 -2.1; 2457 -2.7; 2703 -3.1; 2973 -3.3; 3270 -2.9; 3597 -2.3; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -1.8; 5793 -5.8; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.7; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 22 Hz    |  1.19 | 3.8 dB  |
| Peaking | 50 Hz    |  2.15 | 1.5 dB  |
| Peaking | 2227 Hz  |  2.91 | 3.7 dB  |
| Peaking | 4388 Hz  |  1.69 | 6.2 dB  |
| Peaking | 20387 Hz |  2.53 | -0.6 dB |
| Peaking | 176 Hz   |  1.61 | -1.3 dB |
| Peaking | 1458 Hz  |  4.63 | -1.0 dB |
| Peaking | 6385 Hz  | 11.94 | 3.8 dB  |
| Peaking | 6527 Hz  |  2.63 | -2.6 dB |
| Peaking | 6767 Hz  |  8.16 | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Elear/Focal%20Elear.png)