# BRAINWAVZ HM5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -0.8; 25 -1.0; 28 -1.1; 31 -1.2; 34 -1.2; 37 -1.2; 41 -1.2; 45 -1.3; 49 -1.4; 54 -1.6; 60 -2.0; 66 -2.4; 72 -2.7; 79 -3.2; 87 -3.7; 96 -4.4; 106 -5.0; 116 -5.6; 128 -6.0; 141 -6.3; 155 -6.4; 170 -6.4; 187 -6.3; 206 -6.1; 227 -5.6; 249 -4.9; 274 -3.7; 302 -2.1; 332 -0.8; 365 -0.5; 402 -1.3; 442 -2.4; 486 -3.5; 535 -4.3; 588 -4.8; 647 -5.2; 712 -5.2; 783 -4.9; 861 -4.6; 947 -4.8; 1042 -4.8; 1146 -4.8; 1261 -5.0; 1387 -5.4; 1526 -5.8; 1678 -6.6; 1846 -7.5; 2031 -7.8; 2234 -7.6; 2457 -7.1; 2703 -6.8; 2973 -5.0; 3270 -5.0; 3597 -8.4; 3957 -8.2; 4353 -8.2; 4788 -8.6; 5267 -7.1; 5793 -7.0; 6373 -5.0; 7010 -2.4; 7711 -4.6; 8482 -4.9; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -5.0; 13660 -6.9; 15026 -6.5; 16529 -4.9; 18182 -4.9; 20000 -11.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BRAINWAVZ HM5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BRAINWAVZ HM5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 25 Hz    |  1.23 | 4.1 dB  |
| Peaking | 51 Hz    |  2.02 | 2.9 dB  |
| Peaking | 363 Hz   |  3.42 | 4.9 dB  |
| Peaking | 2044 Hz  |  2.62 | -3.0 dB |
| Peaking | 4396 Hz  |  2.69 | -3.9 dB |
| Peaking | 163 Hz   |  2    | -2.1 dB |
| Peaking | 3134 Hz  | 14.7  | 2.3 dB  |
| Peaking | 6146 Hz  |  4.91 | -3.1 dB |
| Peaking | 6753 Hz  |  6.44 | 5.6 dB  |
| Peaking | 14243 Hz |  3.77 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/BRAINWAVZ%20HM5/BRAINWAVZ%20HM5.png)