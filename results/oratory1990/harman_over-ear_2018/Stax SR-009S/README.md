# Stax SR-009S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.7; 37 -0.9; 41 -1.2; 45 -1.6; 49 -1.9; 54 -2.4; 60 -2.7; 66 -3.2; 72 -3.8; 79 -4.4; 87 -4.7; 96 -4.9; 106 -5.3; 116 -5.4; 128 -5.7; 141 -6.0; 155 -6.3; 170 -6.6; 187 -6.8; 206 -6.8; 227 -6.9; 249 -6.9; 274 -7.0; 302 -6.9; 332 -6.9; 365 -6.9; 402 -7.1; 442 -7.3; 486 -7.6; 535 -7.8; 588 -8.1; 647 -8.6; 712 -8.9; 783 -8.7; 861 -9.6; 947 -10.4; 1042 -10.5; 1146 -10.0; 1261 -10.0; 1387 -9.9; 1526 -9.4; 1678 -8.3; 1846 -6.9; 2031 -4.5; 2234 -2.1; 2457 -2.7; 2703 -4.4; 2973 -5.2; 3270 -5.2; 3597 -6.2; 3957 -7.2; 4353 -7.8; 4788 -9.4; 5267 -8.3; 5793 -2.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -8.8; 12418 -10.4; 13660 -7.0; 15026 -6.5; 16529 -6.5; 18182 -9.6; 20000 -17.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-009S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.56 | 6.3 dB   |
| Peaking | 2085 Hz  | 0.47 | -8.4 dB  |
| Peaking | 2381 Hz  | 1.35 | 12.5 dB  |
| Peaking | 6315 Hz  | 4.7  | 8.1 dB   |
| Peaking | 19830 Hz | 1.38 | -10.2 dB |
| Peaking | 1552 Hz  | 0.67 | -1.3 dB  |
| Peaking | 2999 Hz  | 0.2  | 1.1 dB   |
| Peaking | 4980 Hz  | 6.51 | -3.3 dB  |
| Peaking | 12190 Hz | 4.45 | -4.6 dB  |
| Peaking | 16007 Hz | 1.6  | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -5.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Stax%20SR-009S/Stax%20SR-009S.png)