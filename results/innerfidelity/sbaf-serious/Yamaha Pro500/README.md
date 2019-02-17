# Yamaha Pro500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.1; 31 -1.6; 34 -2.0; 37 -2.4; 41 -2.8; 45 -3.2; 49 -3.5; 54 -3.9; 60 -4.3; 66 -4.4; 72 -3.8; 79 -4.6; 87 -5.6; 96 -5.4; 106 -6.1; 116 -7.0; 128 -7.6; 141 -8.0; 155 -8.3; 170 -8.0; 187 -8.5; 206 -8.6; 227 -8.3; 249 -7.7; 274 -6.9; 302 -6.2; 332 -4.7; 365 -3.5; 402 -2.5; 442 -1.7; 486 -2.3; 535 -2.4; 588 -3.1; 647 -3.7; 712 -4.6; 783 -5.2; 861 -6.0; 947 -5.8; 1042 -6.6; 1146 -6.8; 1261 -6.9; 1387 -7.8; 1526 -8.1; 1678 -7.9; 1846 -6.8; 2031 -5.5; 2234 -4.2; 2457 -2.4; 2703 -0.9; 2973 -0.5; 3270 -1.7; 3597 -3.1; 3957 -2.1; 4353 -1.1; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha Pro500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha Pro500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.03 | 6.3 dB  |
| Peaking | 72 Hz   | 5.01 | 1.9 dB  |
| Peaking | 480 Hz  | 2.35 | 5.1 dB  |
| Peaking | 2866 Hz | 3.42 | 5.7 dB  |
| Peaking | 5210 Hz | 1.92 | 6.6 dB  |
| Peaking | 198 Hz  | 1.33 | -2.6 dB |
| Peaking | 363 Hz  | 4.18 | 1.8 dB  |
| Peaking | 658 Hz  | 4.56 | 1.2 dB  |
| Peaking | 1542 Hz | 3.55 | -2.5 dB |
| Peaking | 8323 Hz | 4.59 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 5.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20Pro500/Yamaha%20Pro500.png)