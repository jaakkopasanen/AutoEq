# AKG K240 Sextett
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.2; 45 -1.7; 49 -2.2; 54 -3.0; 60 -3.4; 66 -3.6; 72 -4.7; 79 -7.1; 87 -9.1; 96 -10.4; 106 -11.2; 116 -11.7; 128 -11.6; 141 -11.2; 155 -11.9; 170 -11.7; 187 -11.5; 206 -11.6; 227 -11.4; 249 -11.0; 274 -10.6; 302 -10.1; 332 -9.5; 365 -9.0; 402 -8.7; 442 -8.4; 486 -8.0; 535 -7.1; 588 -5.3; 647 -4.7; 712 -3.9; 783 -2.9; 861 -2.4; 947 -1.8; 1042 -1.1; 1146 -0.7; 1261 -0.6; 1387 -0.8; 1526 -1.4; 1678 -1.8; 1846 -2.5; 2031 -3.3; 2234 -3.5; 2457 -3.4; 2703 -2.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -2.4; 4353 -5.0; 4788 -8.6; 5267 -8.7; 5793 -10.2; 6373 -14.3; 7010 -12.3; 7711 -10.6; 8482 -9.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.0; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240 Sextett GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 Sextett ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 52 Hz   |  0.35 | 14.1 dB  |
| Peaking | 110 Hz  |  0.4  | -14.6 dB |
| Peaking | 1123 Hz |  0.83 | 6.6 dB   |
| Peaking | 3365 Hz |  2.4  | 6.2 dB   |
| Peaking | 6530 Hz |  2.41 | -8.1 dB  |
| Peaking | 70 Hz   |  6.1  | 1.7 dB   |
| Peaking | 92 Hz   |  3.37 | -1.0 dB  |
| Peaking | 4792 Hz | 12.49 | -2.2 dB  |
| Peaking | 9707 Hz |  5.55 | 1.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K240%20Sextett/AKG%20K240%20Sextett.png)