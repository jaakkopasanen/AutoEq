# KZ ZST
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.7; 25 -9.9; 28 -10.1; 31 -10.2; 34 -10.3; 37 -10.4; 41 -10.5; 45 -10.5; 49 -10.6; 54 -10.6; 60 -10.7; 66 -10.8; 72 -10.8; 79 -10.9; 87 -11.0; 96 -11.0; 106 -11.0; 116 -10.9; 128 -10.6; 141 -10.4; 155 -10.3; 170 -10.8; 187 -10.4; 206 -9.9; 227 -9.5; 249 -9.1; 274 -8.7; 302 -8.3; 332 -7.9; 365 -7.6; 402 -7.3; 442 -7.0; 486 -6.7; 535 -6.4; 588 -6.2; 647 -6.1; 712 -5.8; 783 -5.8; 861 -6.2; 947 -6.2; 1042 -6.8; 1146 -7.4; 1261 -8.1; 1387 -8.7; 1526 -9.4; 1678 -10.3; 1846 -11.0; 2031 -11.2; 2234 -10.4; 2457 -9.4; 2703 -8.0; 2973 -7.8; 3270 -8.5; 3597 -7.6; 3957 -3.3; 4353 -0.5; 4788 -2.4; 5267 -7.9; 5793 -7.9; 6373 -9.8; 7010 -11.3; 7711 -7.7; 8482 -6.5; 9330 -6.5; 10263 -11.2; 11289 -15.4; 12418 -15.2; 13660 -13.7; 15026 -10.3; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZST GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZST ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 71 Hz    | 0.33 | -4.7 dB  |
| Peaking | 1977 Hz  | 1.89 | -4.9 dB  |
| Peaking | 4391 Hz  | 5.95 | 7.8 dB   |
| Peaking | 6731 Hz  | 6.52 | -4.8 dB  |
| Peaking | 12383 Hz | 2.02 | -10.0 dB |
| Peaking | 190 Hz   | 2.67 | -1.0 dB  |
| Peaking | 706 Hz   | 1.26 | 1.6 dB   |
| Peaking | 3175 Hz  | 0.21 | -0.4 dB  |
| Peaking | 9139 Hz  | 3.39 | 3.3 dB   |
| Peaking | 10850 Hz | 6.51 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -4.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/KZ%20ZST/KZ%20ZST.png)