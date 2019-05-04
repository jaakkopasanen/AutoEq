# AuGlamour F300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -8.9; 25 -9.0; 28 -9.2; 31 -9.3; 34 -9.4; 37 -9.5; 41 -9.6; 45 -9.6; 49 -9.7; 54 -9.8; 60 -10.0; 66 -10.2; 72 -10.3; 79 -10.5; 87 -10.7; 96 -10.9; 106 -10.9; 116 -10.7; 128 -10.8; 141 -10.9; 155 -10.8; 170 -10.6; 187 -10.3; 206 -10.1; 227 -9.8; 249 -9.4; 274 -9.0; 302 -8.7; 332 -8.4; 365 -8.0; 402 -7.7; 442 -7.4; 486 -7.0; 535 -6.6; 588 -6.4; 647 -6.2; 712 -5.9; 783 -5.6; 861 -5.4; 947 -5.2; 1042 -5.2; 1146 -5.3; 1261 -5.5; 1387 -5.7; 1526 -5.8; 1678 -5.9; 1846 -6.2; 2031 -6.8; 2234 -7.7; 2457 -8.4; 2703 -8.4; 2973 -7.9; 3270 -8.1; 3597 -8.8; 3957 -9.1; 4353 -8.4; 4788 -5.8; 5267 -1.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AuGlamour F300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AuGlamour F300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.42 | -2.7 dB |
| Peaking | 118 Hz  | 0.92 | -2.9 dB |
| Peaking | 221 Hz  | 1.41 | -1.9 dB |
| Peaking | 4061 Hz | 1.58 | -4.1 dB |
| Peaking | 5737 Hz | 2.81 | 8.4 dB  |
| Peaking | 400 Hz  | 1.44 | -0.9 dB |
| Peaking | 1035 Hz | 0.59 | 1.4 dB  |
| Peaking | 2444 Hz | 3.75 | -1.9 dB |
| Peaking | 8127 Hz | 4.94 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/AuGlamour%20F300/AuGlamour%20F300.png)