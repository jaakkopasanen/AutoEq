# Sennheiser HD 228
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.5; 25 -8.9; 28 -9.4; 31 -9.8; 34 -10.1; 37 -10.4; 41 -10.8; 45 -11.1; 49 -11.4; 54 -11.7; 60 -12.1; 66 -12.5; 72 -12.8; 79 -13.1; 87 -13.0; 96 -12.5; 106 -12.4; 116 -13.3; 128 -14.4; 141 -14.9; 155 -14.7; 170 -14.0; 187 -13.2; 206 -11.4; 227 -9.8; 249 -11.3; 274 -10.9; 302 -10.1; 332 -9.4; 365 -8.8; 402 -8.0; 442 -7.0; 486 -6.2; 535 -5.5; 588 -4.9; 647 -4.6; 712 -4.5; 783 -4.8; 861 -5.1; 947 -5.4; 1042 -5.5; 1146 -5.2; 1261 -4.8; 1387 -4.6; 1526 -4.6; 1678 -5.8; 1846 -4.9; 2031 -4.6; 2234 -3.9; 2457 -3.2; 2703 -2.8; 2973 -2.3; 3270 -1.6; 3597 -0.5; 3957 -1.5; 4353 -6.4; 4788 -9.3; 5267 -6.1; 5793 -3.2; 6373 -4.1; 7010 -4.7; 7711 -6.2; 8482 -7.5; 9330 -5.9; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -7.2; 18182 -10.5; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 228 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 228 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 62 Hz    | 0.54 | -6.3 dB |
| Peaking | 153 Hz   | 1.62 | -6.4 dB |
| Peaking | 290 Hz   | 2.56 | -3.1 dB |
| Peaking | 3809 Hz  | 1.46 | 6.4 dB  |
| Peaking | 4633 Hz  | 4.59 | -8.6 dB |
| Peaking | 391 Hz   | 4.85 | -1.0 dB |
| Peaking | 649 Hz   | 2.1  | 1.5 dB  |
| Peaking | 5821 Hz  | 9.08 | 1.7 dB  |
| Peaking | 19410 Hz | 0.96 | -6.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -7.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20228/Sennheiser%20HD%20228.png)