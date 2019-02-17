# Phiaton PS 320
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.3; 25 -4.5; 28 -4.6; 31 -4.8; 34 -4.9; 37 -4.9; 41 -5.0; 45 -5.2; 49 -5.5; 54 -5.7; 60 -5.9; 66 -6.1; 72 -5.8; 79 -5.8; 87 -6.7; 96 -7.7; 106 -8.7; 116 -8.8; 128 -9.3; 141 -9.7; 155 -10.1; 170 -9.9; 187 -9.9; 206 -9.5; 227 -8.6; 249 -8.8; 274 -9.7; 302 -9.6; 332 -8.9; 365 -7.7; 402 -6.4; 442 -4.8; 486 -3.6; 535 -3.1; 588 -2.3; 647 -2.3; 712 -3.4; 783 -4.3; 861 -5.3; 947 -6.1; 1042 -6.7; 1146 -7.1; 1261 -7.4; 1387 -8.7; 1526 -9.2; 1678 -9.6; 1846 -9.7; 2031 -9.7; 2234 -10.3; 2457 -8.7; 2703 -6.9; 2973 -5.0; 3270 -3.7; 3597 -1.4; 3957 -1.0; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.8; 6373 -5.4; 7010 -5.1; 7711 -6.2; 8482 -7.4; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.7; 18182 -10.0; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 320 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 320 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 226 Hz   |  0.73 | -3.9 dB |
| Peaking | 589 Hz   |  1.57 | 5.8 dB  |
| Peaking | 2000 Hz  |  1.23 | -4.9 dB |
| Peaking | 4294 Hz  |  1.48 | 7.7 dB  |
| Peaking | 18723 Hz |  0.86 | -3.8 dB |
| Peaking | 27 Hz    |  0.88 | 2.4 dB  |
| Peaking | 76 Hz    |  5.73 | 1.3 dB  |
| Peaking | 1424 Hz  |  2.86 | -0.1 dB |
| Peaking | 5634 Hz  | 10.77 | 2.7 dB  |
| Peaking | 8928 Hz  |  4.39 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%20320/Phiaton%20PS%20320.png)