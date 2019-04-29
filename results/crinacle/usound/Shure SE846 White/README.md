# Shure SE846 White
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.1; 25 -6.2; 28 -6.2; 31 -6.2; 34 -6.2; 37 -6.3; 41 -6.3; 45 -6.3; 49 -6.3; 54 -6.4; 60 -6.4; 66 -6.5; 72 -6.7; 79 -6.7; 87 -6.9; 96 -7.0; 106 -7.1; 116 -7.1; 128 -7.1; 141 -7.2; 155 -7.1; 170 -7.0; 187 -6.9; 206 -6.7; 227 -6.6; 249 -6.5; 274 -6.4; 302 -6.3; 332 -6.3; 365 -6.3; 402 -6.3; 442 -6.4; 486 -6.4; 535 -6.4; 588 -6.3; 647 -6.1; 712 -5.8; 783 -5.4; 861 -5.0; 947 -4.9; 1042 -5.2; 1146 -5.8; 1261 -6.4; 1387 -6.6; 1526 -6.3; 1678 -5.8; 1846 -5.2; 2031 -4.7; 2234 -4.1; 2457 -3.1; 2703 -1.9; 2973 -0.9; 3270 -1.1; 3597 -2.1; 3957 -3.1; 4353 -3.0; 4788 -1.8; 5267 -0.9; 5793 -0.5; 6373 -1.6; 7010 -4.8; 7711 -8.3; 8482 -8.7; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 White GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 White ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 124 Hz  | 0.27 | -1.9 dB |
| Peaking | 1441 Hz | 3.26 | -1.7 dB |
| Peaking | 3030 Hz | 2.62 | 4.1 dB  |
| Peaking | 5763 Hz | 2.18 | 5.0 dB  |
| Peaking | 7981 Hz | 4.36 | -5.7 dB |
| Peaking | 21 Hz   | 1.51 | -0.4 dB |
| Peaking | 562 Hz  | 3.24 | -0.5 dB |
| Peaking | 912 Hz  | 4.64 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shure%20SE846%20White/Shure%20SE846%20White.png)