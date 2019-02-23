# Philips SHE3590
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -12.7; 25 -12.6; 28 -12.3; 31 -12.0; 34 -11.8; 37 -11.6; 41 -11.3; 45 -11.0; 49 -10.7; 54 -10.4; 60 -10.2; 66 -10.0; 72 -9.8; 79 -9.6; 87 -9.4; 96 -9.3; 106 -8.9; 116 -8.5; 128 -8.3; 141 -7.9; 155 -7.6; 170 -7.1; 187 -6.8; 206 -6.3; 227 -5.7; 249 -5.3; 274 -4.8; 302 -4.3; 332 -3.8; 365 -3.3; 402 -2.9; 442 -2.3; 486 -2.1; 535 -1.7; 588 -1.2; 647 -1.0; 712 -1.1; 783 -0.9; 861 -0.9; 947 -1.2; 1042 -1.9; 1146 -2.5; 1261 -3.3; 1387 -4.3; 1526 -5.5; 1678 -6.5; 1846 -7.3; 2031 -8.0; 2234 -9.3; 2457 -10.1; 2703 -9.4; 2973 -5.9; 3270 -2.2; 3597 -0.5; 3957 -0.9; 4353 -3.5; 4788 -5.8; 5267 -7.1; 5793 -5.5; 6373 -3.5; 7010 -2.3; 7711 -4.1; 8482 -4.4; 9330 -4.4; 10263 -4.4; 11289 -4.4; 12418 -4.4; 13660 -4.4; 15026 -4.4; 16529 -4.4; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHE3590 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHE3590 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.58 | -7.3 dB |
| Peaking | 89 Hz   | 0.42 | -4.0 dB |
| Peaking | 763 Hz  | 0.6  | 4.5 dB  |
| Peaking | 2553 Hz | 1.1  | -8.4 dB |
| Peaking | 3517 Hz | 2.89 | 9.2 dB  |
| Peaking | 4105 Hz | 8.11 | 1.4 dB  |
| Peaking | 5309 Hz | 4.14 | -2.9 dB |
| Peaking | 6895 Hz | 3.6  | 3.1 dB  |
| Peaking | 7540 Hz | 4.65 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20SHE3590/Philips%20SHE3590.png)