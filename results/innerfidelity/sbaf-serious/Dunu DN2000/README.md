# Dunu DN2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.4; 25 -10.3; 28 -10.1; 31 -10.0; 34 -9.8; 37 -9.6; 41 -9.5; 45 -9.3; 49 -9.2; 54 -9.0; 60 -9.0; 66 -8.9; 72 -8.9; 79 -9.0; 87 -9.1; 96 -9.2; 106 -9.3; 116 -9.2; 128 -9.3; 141 -9.4; 155 -9.4; 170 -9.4; 187 -9.4; 206 -9.3; 227 -9.2; 249 -9.1; 274 -8.9; 302 -8.8; 332 -8.6; 365 -8.5; 402 -8.3; 442 -8.0; 486 -7.8; 535 -7.5; 588 -7.0; 647 -6.8; 712 -6.7; 783 -6.2; 861 -6.2; 947 -6.2; 1042 -6.1; 1146 -6.0; 1261 -5.9; 1387 -5.9; 1526 -5.9; 1678 -5.6; 1846 -4.8; 2031 -3.7; 2234 -3.0; 2457 -2.2; 2703 -2.1; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -1.8; 4353 -6.2; 4788 -8.6; 5267 -5.6; 5793 -2.4; 6373 -2.0; 7010 -4.0; 7711 -7.2; 8482 -11.5; 9330 -12.3; 10263 -8.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.27 | -4.1 dB |
| Peaking | 188 Hz  | 0.56 | -2.7 dB |
| Peaking | 3020 Hz | 1.72 | 6.2 dB  |
| Peaking | 6432 Hz | 5    | 5.3 dB  |
| Peaking | 8996 Hz | 3.74 | -7.1 dB |
| Peaking | 455 Hz  | 1.34 | -1.0 dB |
| Peaking | 615 Hz  | 0.7  | 0.9 dB  |
| Peaking | 3827 Hz | 6.25 | 3.2 dB  |
| Peaking | 4729 Hz | 4.07 | -4.7 dB |
| Peaking | 5659 Hz | 6.35 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN2000/Dunu%20DN2000.png)