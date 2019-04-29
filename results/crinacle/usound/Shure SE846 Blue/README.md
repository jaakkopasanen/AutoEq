# Shure SE846 Blue
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.6; 23 -8.7; 25 -8.8; 28 -8.9; 31 -8.9; 34 -8.9; 37 -8.9; 41 -8.9; 45 -8.9; 49 -8.9; 54 -9.0; 60 -9.0; 66 -9.1; 72 -9.2; 79 -9.3; 87 -9.4; 96 -9.6; 106 -9.7; 116 -9.7; 128 -9.7; 141 -9.7; 155 -9.7; 170 -9.6; 187 -9.5; 206 -9.4; 227 -9.3; 249 -9.2; 274 -9.0; 302 -9.0; 332 -8.9; 365 -8.9; 402 -8.9; 442 -9.0; 486 -8.9; 535 -8.8; 588 -8.6; 647 -8.3; 712 -8.0; 783 -7.5; 861 -7.1; 947 -6.9; 1042 -7.1; 1146 -7.7; 1261 -8.3; 1387 -8.4; 1526 -8.0; 1678 -7.3; 1846 -6.5; 2031 -5.8; 2234 -5.0; 2457 -4.1; 2703 -2.9; 2973 -1.8; 3270 -1.8; 3597 -2.6; 3957 -2.6; 4353 -1.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.7; 8482 -8.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Blue GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Blue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.04 | -1.4 dB |
| Peaking | 146 Hz  | 0.24 | -3.1 dB |
| Peaking | 1455 Hz | 2.73 | -1.9 dB |
| Peaking | 3076 Hz | 1.78 | 4.3 dB  |
| Peaking | 5382 Hz | 2.36 | 6.2 dB  |
| Peaking | 555 Hz  | 2.82 | -0.6 dB |
| Peaking | 908 Hz  | 4.88 | 0.7 dB  |
| Peaking | 6507 Hz | 6.92 | 2.5 dB  |
| Peaking | 8348 Hz | 3.52 | -3.4 dB |
| Peaking | 9025 Hz | 5.34 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shure%20SE846%20Blue/Shure%20SE846%20Blue.png)