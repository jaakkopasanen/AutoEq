# Munitio Pro40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -7.4; 25 -8.2; 28 -9.3; 31 -10.2; 34 -10.9; 37 -11.5; 41 -12.0; 45 -12.4; 49 -12.6; 54 -12.8; 60 -12.8; 66 -12.9; 72 -13.0; 79 -13.1; 87 -13.6; 96 -14.0; 106 -14.3; 116 -14.4; 128 -14.6; 141 -14.9; 155 -15.0; 170 -14.8; 187 -15.0; 206 -15.1; 227 -15.0; 249 -15.0; 274 -14.7; 302 -14.0; 332 -12.8; 365 -12.0; 402 -11.2; 442 -10.4; 486 -9.0; 535 -7.0; 588 -4.3; 647 -2.2; 712 -2.1; 783 -3.4; 861 -5.8; 947 -7.2; 1042 -7.8; 1146 -7.3; 1261 -6.4; 1387 -6.2; 1526 -5.7; 1678 -5.0; 1846 -3.9; 2031 -3.2; 2234 -2.3; 2457 -1.2; 2703 -1.2; 2973 -1.8; 3270 -1.8; 3597 -2.0; 3957 -1.9; 4353 -1.6; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Munitio Pro40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Munitio Pro40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 1.75 | -2.0 dB |
| Peaking | 266 Hz  | 0.2  | -9.2 dB |
| Peaking | 662 Hz  | 1.57 | 11.7 dB |
| Peaking | 2541 Hz | 0.94 | 6.6 dB  |
| Peaking | 5404 Hz | 2.37 | 5.3 dB  |
| Peaking | 776 Hz  | 6.45 | 0.9 dB  |
| Peaking | 1026 Hz | 2.74 | -1.3 dB |
| Peaking | 1254 Hz | 3.51 | 1.2 dB  |
| Peaking | 6253 Hz | 7.91 | 1.7 dB  |
| Peaking | 8153 Hz | 2.02 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -8.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Munitio%20Pro40/Munitio%20Pro40.png)