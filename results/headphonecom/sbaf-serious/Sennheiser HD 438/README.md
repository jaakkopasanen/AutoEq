# Sennheiser HD 438
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.1; 45 -1.6; 49 -1.9; 54 -1.8; 60 -2.0; 66 -2.9; 72 -3.3; 79 -1.7; 87 -0.6; 96 -2.3; 106 -3.2; 116 -3.6; 128 -3.9; 141 -4.1; 155 -3.8; 170 -3.9; 187 -3.0; 206 -2.7; 227 -2.2; 249 -1.9; 274 -2.2; 302 -1.7; 332 -1.9; 365 -2.6; 402 -3.0; 442 -3.0; 486 -3.5; 535 -4.0; 588 -4.4; 647 -4.3; 712 -4.3; 783 -4.7; 861 -5.6; 947 -6.5; 1042 -6.1; 1146 -5.7; 1261 -6.1; 1387 -6.7; 1526 -5.5; 1678 -4.5; 1846 -3.4; 2031 -2.0; 2234 -1.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 438 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 438 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.45 | 6.1 dB  |
| Peaking | 88 Hz   | 4.54 | 3.2 dB  |
| Peaking | 272 Hz  | 1.09 | 4.2 dB  |
| Peaking | 472 Hz  | 1.84 | 1.3 dB  |
| Peaking | 3682 Hz | 0.82 | 6.9 dB  |
| Peaking | 1391 Hz | 3.07 | -2.0 dB |
| Peaking | 2301 Hz | 2.52 | 2.0 dB  |
| Peaking | 3583 Hz | 2.25 | -1.3 dB |
| Peaking | 6201 Hz | 2.41 | 4.7 dB  |
| Peaking | 7575 Hz | 1.53 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 3.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | 3.9 dB  |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20438/Sennheiser%20HD%20438.png)