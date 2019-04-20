# Focal Elear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.4; 25 -3.7; 28 -4.1; 31 -4.3; 34 -4.5; 37 -4.7; 41 -4.9; 45 -5.1; 49 -5.2; 54 -5.3; 60 -5.5; 66 -5.8; 72 -6.1; 79 -6.4; 87 -6.7; 96 -7.0; 106 -7.3; 116 -7.6; 128 -7.8; 141 -8.0; 155 -8.1; 170 -8.1; 187 -8.2; 206 -8.2; 227 -8.1; 249 -7.9; 274 -7.7; 302 -7.5; 332 -7.2; 365 -6.9; 402 -6.8; 442 -6.7; 486 -6.7; 535 -6.8; 588 -6.8; 647 -6.6; 712 -6.7; 783 -7.0; 861 -7.2; 947 -7.2; 1042 -7.1; 1146 -7.2; 1261 -7.3; 1387 -7.2; 1526 -7.2; 1678 -6.3; 1846 -4.8; 2031 -3.1; 2234 -2.7; 2457 -3.3; 2703 -3.8; 2973 -4.0; 3270 -3.6; 3597 -2.9; 3957 -0.7; 4353 -0.5; 4788 -0.6; 5267 -2.6; 5793 -6.1; 6373 -2.1; 7010 -2.7; 7711 -4.9; 8482 -5.2; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -6.7; 20000 -14.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 26 Hz    |  0.6  | 2.8 dB  |
| Peaking | 265 Hz   |  0.09 | -2.4 dB |
| Peaking | 2192 Hz  |  3.39 | 3.7 dB  |
| Peaking | 4325 Hz  |  2.04 | 5.5 dB  |
| Peaking | 22050 Hz |  2.2  | 0.8 dB  |
| Peaking | 189 Hz   |  1.3  | -1.0 dB |
| Peaking | 471 Hz   |  0.99 | 0.9 dB  |
| Peaking | 1452 Hz  |  3.9  | -0.9 dB |
| Peaking | 5732 Hz  | 10.54 | -3.5 dB |
| Peaking | 6612 Hz  |  8.34 | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Elear/Focal%20Elear.png)