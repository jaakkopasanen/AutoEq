# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.4; 25 -7.5; 28 -7.7; 31 -7.8; 34 -7.9; 37 -8.1; 41 -8.2; 45 -8.3; 49 -8.5; 54 -8.6; 60 -8.9; 66 -9.1; 72 -9.3; 79 -9.6; 87 -9.8; 96 -10.1; 106 -10.3; 116 -10.5; 128 -10.6; 141 -10.7; 155 -10.6; 170 -10.5; 187 -10.3; 206 -10.1; 227 -9.7; 249 -9.4; 274 -9.0; 302 -8.5; 332 -8.1; 365 -7.6; 402 -7.2; 442 -6.7; 486 -6.2; 535 -5.7; 588 -5.3; 647 -4.8; 712 -4.4; 783 -4.0; 861 -3.9; 947 -4.0; 1042 -4.3; 1146 -4.9; 1261 -5.2; 1387 -5.3; 1526 -5.8; 1678 -6.0; 1846 -6.4; 2031 -7.0; 2234 -7.5; 2457 -7.0; 2703 -5.5; 2973 -3.9; 3270 -3.0; 3597 -2.8; 3957 -3.7; 4353 -5.9; 4788 -9.2; 5267 -7.8; 5793 -3.2; 6373 -0.5; 7010 -1.6; 7711 -4.1; 8482 -6.1; 9330 -4.4; 10263 -4.2; 11289 -4.2; 12418 -5.2; 13660 -4.2; 15026 -4.2; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 53 Hz   | 0.27 | -3.6 dB  |
| Peaking | 180 Hz  | 0.62 | -4.3 dB  |
| Peaking | 2156 Hz | 2.42 | -3.7 dB  |
| Peaking | 4943 Hz | 4.24 | -11.8 dB |
| Peaking | 5137 Hz | 1.5  | 5.8 dB   |
| Peaking | 821 Hz  | 3.68 | 1.2 dB   |
| Peaking | 3396 Hz | 5.79 | 1.4 dB   |
| Peaking | 6456 Hz | 5.47 | 4.1 dB   |
| Peaking | 7150 Hz | 4.37 | 3.1 dB   |
| Peaking | 7576 Hz | 1.97 | -4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Shure%20SE215/Shure%20SE215.png)