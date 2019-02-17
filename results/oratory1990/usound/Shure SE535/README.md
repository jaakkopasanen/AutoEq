# Shure SE535
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -1.7; 25 -1.8; 28 -1.9; 31 -2.0; 34 -2.1; 37 -2.3; 41 -2.4; 45 -2.6; 49 -2.8; 54 -3.0; 60 -3.3; 66 -3.7; 72 -4.1; 79 -4.5; 87 -4.9; 96 -5.4; 106 -5.9; 116 -6.3; 128 -6.7; 141 -7.0; 155 -7.3; 170 -7.5; 187 -7.7; 206 -7.9; 227 -8.0; 249 -8.0; 274 -8.1; 302 -8.1; 332 -8.1; 365 -8.0; 402 -7.9; 442 -7.8; 486 -7.7; 535 -7.5; 588 -7.3; 647 -7.0; 712 -6.6; 783 -6.3; 861 -6.0; 947 -5.9; 1042 -6.0; 1146 -6.1; 1261 -6.2; 1387 -6.0; 1526 -5.6; 1678 -5.0; 1846 -4.4; 2031 -4.0; 2234 -3.3; 2457 -2.6; 2703 -2.3; 2973 -2.6; 3270 -2.8; 3597 -2.2; 3957 -1.2; 4353 -0.5; 4788 -0.5; 5267 -1.1; 5793 -1.9; 6373 -2.6; 7010 -5.3; 7711 -6.8; 8482 -7.2; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE535 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.58 | 4.0 dB  |
| Peaking | 56 Hz   | 0.83 | 2.0 dB  |
| Peaking | 255 Hz  | 0.51 | -2.4 dB |
| Peaking | 2585 Hz | 1.69 | 3.0 dB  |
| Peaking | 4714 Hz | 2.01 | 5.5 dB  |
| Peaking | 887 Hz  | 4.17 | 0.5 dB  |
| Peaking | 1308 Hz | 4.9  | -0.5 dB |
| Peaking | 6291 Hz | 5.21 | 2.0 dB  |
| Peaking | 7895 Hz | 3.02 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Shure%20SE535/Shure%20SE535.png)