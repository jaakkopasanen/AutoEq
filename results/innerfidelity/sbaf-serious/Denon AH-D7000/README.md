# Denon AH-D7000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.9; 28 -2.0; 31 -3.3; 34 -4.4; 37 -5.3; 41 -6.0; 45 -6.3; 49 -6.5; 54 -6.9; 60 -6.9; 66 -6.9; 72 -7.1; 79 -7.1; 87 -7.2; 96 -7.2; 106 -7.0; 116 -6.9; 128 -6.9; 141 -6.9; 155 -6.9; 170 -6.5; 187 -6.4; 206 -6.2; 227 -5.7; 249 -5.3; 274 -4.8; 302 -4.3; 332 -3.9; 365 -3.5; 402 -3.9; 442 -4.3; 486 -5.8; 535 -7.2; 588 -8.0; 647 -8.5; 712 -9.2; 783 -9.1; 861 -8.0; 947 -8.1; 1042 -8.6; 1146 -8.0; 1261 -7.5; 1387 -7.4; 1526 -7.2; 1678 -6.8; 1846 -6.2; 2031 -5.9; 2234 -5.6; 2457 -4.7; 2703 -4.0; 2973 -3.7; 3270 -4.1; 3597 -5.0; 3957 -6.1; 4353 -8.8; 4788 -7.8; 5267 -6.7; 5793 -7.7; 6373 -8.5; 7010 -8.5; 7711 -7.4; 8482 -6.5; 9330 -6.8; 10263 -10.1; 11289 -9.9; 12418 -6.9; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.8; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 23 Hz    |  2.07 | 6.4 dB  |
| Peaking | 370 Hz   |  1.04 | 9.5 dB  |
| Peaking | 452 Hz   |  0.53 | -6.7 dB |
| Peaking | 2901 Hz  |  1.65 | 4.3 dB  |
| Peaking | 6589 Hz  |  0.43 | -1.9 dB |
| Peaking | 11 Hz    |  1.94 | 1.3 dB  |
| Peaking | 4380 Hz  | 11.1  | -2.2 dB |
| Peaking | 8954 Hz  |  3.72 | 2.8 dB  |
| Peaking | 10796 Hz |  2.84 | -4.6 dB |
| Peaking | 12550 Hz |  1.55 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D7000/Denon%20AH-D7000.png)