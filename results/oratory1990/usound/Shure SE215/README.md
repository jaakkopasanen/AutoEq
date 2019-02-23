# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.9; 25 -7.0; 28 -7.2; 31 -7.3; 34 -7.4; 37 -7.5; 41 -7.7; 45 -7.8; 49 -8.0; 54 -8.1; 60 -8.3; 66 -8.6; 72 -8.8; 79 -9.1; 87 -9.3; 96 -9.6; 106 -9.8; 116 -10.0; 128 -10.1; 141 -10.2; 155 -10.1; 170 -10.0; 187 -9.8; 206 -9.5; 227 -9.2; 249 -8.9; 274 -8.5; 302 -8.0; 332 -7.6; 365 -7.1; 402 -6.7; 442 -6.2; 486 -5.7; 535 -5.2; 588 -4.8; 647 -4.3; 712 -3.9; 783 -3.5; 861 -3.4; 947 -3.5; 1042 -3.8; 1146 -4.4; 1261 -4.7; 1387 -4.8; 1526 -5.3; 1678 -5.5; 1846 -5.9; 2031 -6.5; 2234 -6.9; 2457 -6.5; 2703 -5.0; 2973 -3.4; 3270 -2.5; 3597 -2.3; 3957 -3.2; 4353 -5.4; 4788 -8.7; 5267 -7.3; 5793 -2.6; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 55 Hz    | 0.37 | -1.2 dB |
| Peaking | 156 Hz   | 0.62 | -3.7 dB |
| Peaking | 807 Hz   | 1.34 | 3.0 dB  |
| Peaking | 3455 Hz  | 4.03 | 4.1 dB  |
| Peaking | 21315 Hz | 2.36 | 2.4 dB  |
| Peaking | 2235 Hz  | 5.19 | -1.8 dB |
| Peaking | 5008 Hz  | 5.43 | -6.3 dB |
| Peaking | 6352 Hz  | 2.37 | 7.4 dB  |
| Peaking | 7509 Hz  | 2.41 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Shure%20SE215/Shure%20SE215.png)