# Sennheiser HD 540 reference-II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.9; 41 -1.5; 45 -1.9; 49 -2.3; 54 -2.8; 60 -3.2; 66 -3.4; 72 -3.8; 79 -4.8; 87 -6.0; 96 -6.9; 106 -7.6; 116 -8.2; 128 -8.7; 141 -9.1; 155 -9.4; 170 -9.6; 187 -9.7; 206 -9.8; 227 -9.8; 249 -9.7; 274 -9.5; 302 -9.2; 332 -8.9; 365 -8.6; 402 -8.4; 442 -8.1; 486 -7.9; 535 -7.6; 588 -7.3; 647 -6.9; 712 -6.6; 783 -6.4; 861 -5.7; 947 -4.3; 1042 -4.4; 1146 -4.6; 1261 -4.3; 1387 -3.7; 1526 -3.0; 1678 -2.4; 1846 -2.2; 2031 -2.5; 2234 -3.4; 2457 -4.3; 2703 -5.2; 2973 -5.5; 3270 -4.8; 3597 -3.5; 3957 -5.1; 4353 -5.8; 4788 -8.3; 5267 -7.1; 5793 -7.6; 6373 -10.0; 7010 -5.9; 7711 -6.7; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -7.7; 12418 -13.6; 13660 -12.7; 15026 -7.5; 16529 -6.8; 18182 -10.1; 20000 -11.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 540 reference-II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 540 reference-II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 34 Hz    |  0.27 | 6.9 dB  |
| Peaking | 152 Hz   |  0.48 | -5.9 dB |
| Peaking | 978 Hz   |  3.96 | 1.7 dB  |
| Peaking | 1801 Hz  |  1.41 | 4.4 dB  |
| Peaking | 13009 Hz |  3.37 | -8.5 dB |
| Peaking | 101 Hz   |  4.87 | -0.2 dB |
| Peaking | 3676 Hz  |  3.9  | 4.2 dB  |
| Peaking | 4067 Hz  |  1.65 | -2.2 dB |
| Peaking | 6176 Hz  | 12.8  | -4.3 dB |
| Peaking | 10539 Hz |  4.83 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20540%20reference-II/Sennheiser%20HD%20540%20reference-II.png)