# Munitio Pro40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -6.1; 25 -6.9; 28 -8.0; 31 -8.9; 34 -9.6; 37 -10.2; 41 -10.7; 45 -11.1; 49 -11.3; 54 -11.5; 60 -11.5; 66 -11.6; 72 -11.7; 79 -11.8; 87 -12.3; 96 -12.7; 106 -13.0; 116 -13.1; 128 -13.3; 141 -13.6; 155 -13.7; 170 -13.5; 187 -13.7; 206 -13.8; 227 -13.7; 249 -13.7; 274 -13.4; 302 -12.7; 332 -11.5; 365 -10.7; 402 -9.9; 442 -9.1; 486 -7.7; 535 -5.7; 588 -3.0; 647 -0.9; 712 -0.8; 783 -2.1; 861 -4.4; 947 -5.9; 1042 -6.5; 1146 -6.0; 1261 -5.0; 1387 -4.9; 1526 -4.4; 1678 -3.7; 1846 -2.6; 2031 -1.8; 2234 -1.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Munitio Pro40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Munitio Pro40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.61 | 4.0 dB  |
| Peaking | 38 Hz   | 0.95 | -3.3 dB |
| Peaking | 194 Hz  | 0.33 | -7.4 dB |
| Peaking | 657 Hz  | 2.22 | 9.3 dB  |
| Peaking | 3377 Hz | 0.68 | 6.9 dB  |
| Peaking | 1040 Hz | 5.66 | -1.5 dB |
| Peaking | 2254 Hz | 3.31 | 1.0 dB  |
| Peaking | 3470 Hz | 2.54 | -1.1 dB |
| Peaking | 6263 Hz | 2.08 | 5.6 dB  |
| Peaking | 7396 Hz | 1.43 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -7.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Munitio%20Pro40/Munitio%20Pro40.png)