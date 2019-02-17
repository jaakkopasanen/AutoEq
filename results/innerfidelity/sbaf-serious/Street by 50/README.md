# Street by 50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -6.3; 25 -7.1; 28 -8.2; 31 -9.1; 34 -10.0; 37 -10.7; 41 -11.6; 45 -12.4; 49 -13.2; 54 -13.9; 60 -14.6; 66 -15.2; 72 -15.7; 79 -16.2; 87 -16.6; 96 -16.9; 106 -17.1; 116 -17.0; 128 -17.1; 141 -17.0; 155 -16.8; 170 -16.4; 187 -16.0; 206 -15.4; 227 -14.9; 249 -16.3; 274 -15.6; 302 -14.8; 332 -14.2; 365 -13.4; 402 -13.1; 442 -12.6; 486 -12.3; 535 -10.6; 588 -6.7; 647 -4.8; 712 -3.7; 783 -3.9; 861 -5.2; 947 -6.0; 1042 -6.4; 1146 -7.0; 1261 -7.1; 1387 -5.8; 1526 -6.5; 1678 -8.5; 1846 -10.1; 2031 -11.3; 2234 -12.1; 2457 -12.0; 2703 -11.6; 2973 -10.6; 3270 -9.5; 3597 -7.8; 3957 -5.8; 4353 -3.5; 4788 -0.5; 5267 -1.8; 5793 -7.1; 6373 -3.0; 7010 -4.4; 7711 -6.0; 8482 -6.5; 9330 -10.1; 10263 -10.9; 11289 -7.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Street by 50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Street by 50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 74 Hz   |  0.73 | -7.8 dB |
| Peaking | 155 Hz  |  0.95 | -6.6 dB |
| Peaking | 319 Hz  |  1.55 | -6.1 dB |
| Peaking | 2485 Hz |  1.98 | -6.6 dB |
| Peaking | 4853 Hz |  4.39 | 6.9 dB  |
| Peaking | 20 Hz   |  2.38 | 1.9 dB  |
| Peaking | 496 Hz  |  3.66 | -4.2 dB |
| Peaking | 694 Hz  |  2.26 | 4.7 dB  |
| Peaking | 6673 Hz | 11.01 | 4.5 dB  |
| Peaking | 9957 Hz |  4.75 | -5.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -7.7 dB |
| Peaking | 125 Hz   | 1.41 | -8.7 dB |
| Peaking | 250 Hz   | 1.41 | -8.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Street%20by%2050/Street%20by%2050.png)