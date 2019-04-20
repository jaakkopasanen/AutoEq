# Advanced GT-R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.4; 25 -5.6; 28 -5.8; 31 -6.0; 34 -6.1; 37 -6.1; 41 -6.1; 45 -6.2; 49 -6.3; 54 -6.4; 60 -6.6; 66 -6.7; 72 -7.0; 79 -7.4; 87 -7.9; 96 -8.4; 106 -8.8; 116 -9.1; 128 -9.4; 141 -9.8; 155 -10.2; 170 -10.4; 187 -10.7; 206 -10.9; 227 -11.2; 249 -11.2; 274 -11.0; 302 -10.1; 332 -8.6; 365 -8.9; 402 -10.0; 442 -10.7; 486 -11.3; 535 -10.9; 588 -10.4; 647 -9.5; 712 -11.4; 783 -10.7; 861 -10.0; 947 -9.9; 1042 -9.0; 1146 -7.7; 1261 -5.7; 1387 -3.1; 1526 -3.2; 1678 -0.5; 1846 -2.5; 2031 -5.6; 2234 -7.3; 2457 -7.0; 2703 -5.0; 2973 -2.5; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -8.3; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -6.9; 16529 -8.3; 18182 -11.4; 20000 -17.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT-R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT-R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 202 Hz  | 0.87 | -4.5 dB |
| Peaking | 490 Hz  | 3.46 | -2.9 dB |
| Peaking | 803 Hz  | 1.68 | -4.0 dB |
| Peaking | 1631 Hz | 4.19 | 6.1 dB  |
| Peaking | 4484 Hz | 1.4  | 7.1 dB  |
| Peaking | 17 Hz   | 0.69 | 1.3 dB  |
| Peaking | 2366 Hz | 5.25 | -3.0 dB |
| Peaking | 3250 Hz | 4.26 | 3.1 dB  |
| Peaking | 6308 Hz | 2.77 | 7.1 dB  |
| Peaking | 6912 Hz | 1.12 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Advanced%20GT-R/Advanced%20GT-R.png)