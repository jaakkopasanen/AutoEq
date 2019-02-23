# Focal Elear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.4; 25 -3.8; 28 -4.1; 31 -4.2; 34 -4.4; 37 -4.7; 41 -4.9; 45 -5.0; 49 -5.2; 54 -5.3; 60 -5.5; 66 -5.7; 72 -6.0; 79 -6.3; 87 -6.6; 96 -7.0; 106 -7.3; 116 -7.6; 128 -7.8; 141 -7.9; 155 -8.0; 170 -8.1; 187 -8.1; 206 -8.1; 227 -8.0; 249 -7.9; 274 -7.7; 302 -7.4; 332 -7.1; 365 -6.9; 402 -6.7; 442 -6.7; 486 -6.7; 535 -6.8; 588 -6.8; 647 -6.6; 712 -6.7; 783 -6.9; 861 -7.1; 947 -7.1; 1042 -7.1; 1146 -7.1; 1261 -7.3; 1387 -7.1; 1526 -7.2; 1678 -6.3; 1846 -4.7; 2031 -3.1; 2234 -2.6; 2457 -3.3; 2703 -3.7; 2973 -3.9; 3270 -3.5; 3597 -2.9; 3957 -0.6; 4353 -0.5; 4788 -0.6; 5267 -2.3; 5793 -6.4; 6373 -1.9; 7010 -2.7; 7711 -4.9; 8482 -5.1; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -6.6; 20000 -14.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 26 Hz    |  0.6  | 2.8 dB  |
| Peaking | 260 Hz   |  0.1  | -2.4 dB |
| Peaking | 2197 Hz  |  3.43 | 3.7 dB  |
| Peaking | 4323 Hz  |  2.03 | 5.5 dB  |
| Peaking | 22050 Hz |  2.21 | 0.8 dB  |
| Peaking | 187 Hz   |  1.3  | -1.0 dB |
| Peaking | 471 Hz   |  1.04 | 0.9 dB  |
| Peaking | 1446 Hz  |  3.11 | -1.0 dB |
| Peaking | 6678 Hz  | 13.35 | 3.7 dB  |
| Peaking | 19792 Hz |  1.8  | -9.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Elear/Focal%20Elear.png)