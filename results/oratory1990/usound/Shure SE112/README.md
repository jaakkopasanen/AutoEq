# Shure SE112
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.4; 25 -9.5; 28 -9.6; 31 -9.7; 34 -9.8; 37 -9.8; 41 -10.0; 45 -10.1; 49 -10.2; 54 -10.4; 60 -10.7; 66 -10.9; 72 -11.2; 79 -11.5; 87 -11.8; 96 -12.1; 106 -12.4; 116 -12.7; 128 -12.8; 141 -12.9; 155 -13.0; 170 -12.9; 187 -12.8; 206 -12.6; 227 -12.4; 249 -12.1; 274 -11.8; 302 -11.4; 332 -10.9; 365 -10.5; 402 -10.0; 442 -9.6; 486 -9.1; 535 -8.6; 588 -8.1; 647 -7.6; 712 -7.1; 783 -6.6; 861 -6.4; 947 -6.4; 1042 -6.4; 1146 -6.8; 1261 -7.3; 1387 -7.6; 1526 -7.8; 1678 -7.8; 1846 -7.8; 2031 -8.0; 2234 -7.8; 2457 -7.0; 2703 -5.7; 2973 -4.6; 3270 -4.2; 3597 -4.7; 3957 -6.7; 4353 -10.8; 4788 -10.5; 5267 -3.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE112 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE112 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.24 | -2.8 dB |
| Peaking | 140 Hz  | 0.72 | -3.9 dB |
| Peaking | 290 Hz  | 0.9  | -2.8 dB |
| Peaking | 4604 Hz | 6.84 | -8.1 dB |
| Peaking | 5870 Hz | 3.17 | 7.1 dB  |
| Peaking | 904 Hz  | 2.21 | 1.3 dB  |
| Peaking | 2286 Hz | 0.91 | -2.7 dB |
| Peaking | 3182 Hz | 1.88 | 4.3 dB  |
| Peaking | 4230 Hz | 8.18 | -1.7 dB |
| Peaking | 8134 Hz | 4.76 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Shure%20SE112/Shure%20SE112.png)