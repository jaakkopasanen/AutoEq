# Sennheiser HD 448
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.3; 54 -2.3; 60 -3.1; 66 -3.5; 72 -4.0; 79 -4.8; 87 -6.1; 96 -6.0; 106 -5.0; 116 -5.4; 128 -7.0; 141 -8.8; 155 -9.4; 170 -9.5; 187 -10.0; 206 -9.6; 227 -9.4; 249 -8.8; 274 -8.2; 302 -7.3; 332 -6.8; 365 -6.9; 402 -7.1; 442 -7.1; 486 -7.4; 535 -7.7; 588 -7.6; 647 -8.0; 712 -8.4; 783 -8.2; 861 -8.1; 947 -7.9; 1042 -8.1; 1146 -8.5; 1261 -9.4; 1387 -10.3; 1526 -11.2; 1678 -12.1; 1846 -11.8; 2031 -10.7; 2234 -9.0; 2457 -5.8; 2703 -6.5; 2973 -5.7; 3270 -5.5; 3597 -4.6; 3957 -2.7; 4353 -0.5; 4788 -0.5; 5267 -4.7; 5793 -2.4; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 448 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 448 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.56 | 6.5 dB  |
| Peaking | 186 Hz  | 1.41 | -4.1 dB |
| Peaking | 1655 Hz | 1.75 | -5.8 dB |
| Peaking | 4402 Hz | 2.82 | 6.4 dB  |
| Peaking | 6304 Hz | 6.2  | 5.2 dB  |
| Peaking | 89 Hz   | 5.17 | -1.3 dB |
| Peaking | 110 Hz  | 6.73 | 1.7 dB  |
| Peaking | 702 Hz  | 2.97 | -1.3 dB |
| Peaking | 2155 Hz | 4.71 | -1.7 dB |
| Peaking | 2437 Hz | 4.82 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | -5.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20448/Sennheiser%20HD%20448.png)