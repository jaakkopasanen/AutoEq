# KZ ZS10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -12.4; 25 -12.7; 28 -12.6; 31 -12.4; 34 -12.6; 37 -12.6; 41 -12.6; 45 -12.6; 49 -12.6; 54 -12.9; 60 -13.1; 66 -13.4; 72 -13.4; 79 -13.6; 87 -13.6; 96 -13.1; 106 -13.4; 116 -13.1; 128 -13.1; 141 -12.8; 155 -12.4; 170 -12.3; 187 -12.0; 206 -11.7; 227 -11.3; 249 -10.9; 274 -10.4; 302 -10.0; 332 -9.5; 365 -9.0; 402 -8.5; 442 -8.1; 486 -7.6; 535 -7.2; 588 -6.8; 647 -6.4; 712 -6.1; 783 -6.0; 861 -5.7; 947 -5.7; 1042 -6.2; 1146 -7.1; 1261 -8.1; 1387 -9.0; 1526 -9.8; 1678 -10.4; 1846 -11.3; 2031 -12.4; 2234 -12.8; 2457 -12.0; 2703 -11.0; 2973 -10.7; 3270 -10.2; 3597 -11.0; 3957 -8.8; 4353 -3.9; 4788 -0.8; 5267 -4.7; 5793 -1.4; 6373 -0.5; 7010 -3.5; 7711 -8.2; 8482 -9.2; 9330 -6.1; 10263 -6.0; 11289 -6.0; 12418 -6.1; 13660 -10.1; 15026 -9.3; 16529 -6.4; 18182 -9.1; 20000 -15.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 44 Hz    |  0.27 | -6.6 dB |
| Peaking | 175 Hz   |  0.69 | -3.1 dB |
| Peaking | 2147 Hz  |  1.67 | -6.7 dB |
| Peaking | 3793 Hz  |  2.29 | -8.5 dB |
| Peaking | 4588 Hz  |  1.98 | 9.3 dB  |
| Peaking | 866 Hz   |  2.98 | 1.6 dB  |
| Peaking | 5390 Hz  | 12.03 | -4.0 dB |
| Peaking | 6205 Hz  |  5.27 | 5.8 dB  |
| Peaking | 12194 Hz |  0.42 | -1.7 dB |
| Peaking | 19881 Hz |  1.45 | -9.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -3.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/KZ%20ZS10/KZ%20ZS10.png)