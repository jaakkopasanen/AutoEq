# Sennheiser HD 228
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.9; 25 -8.3; 28 -8.8; 31 -9.2; 34 -9.6; 37 -9.9; 41 -10.3; 45 -10.6; 49 -10.9; 54 -11.2; 60 -11.6; 66 -11.9; 72 -12.3; 79 -12.6; 87 -12.5; 96 -12.0; 106 -11.9; 116 -12.7; 128 -13.9; 141 -14.3; 155 -14.2; 170 -13.5; 187 -12.7; 206 -10.9; 227 -9.3; 249 -10.8; 274 -10.3; 302 -9.6; 332 -8.9; 365 -8.2; 402 -7.5; 442 -6.4; 486 -5.6; 535 -4.9; 588 -4.4; 647 -4.1; 712 -4.0; 783 -4.3; 861 -4.6; 947 -4.8; 1042 -5.0; 1146 -4.7; 1261 -4.3; 1387 -4.0; 1526 -4.1; 1678 -5.3; 1846 -4.4; 2031 -4.1; 2234 -3.4; 2457 -2.6; 2703 -2.2; 2973 -1.8; 3270 -1.1; 3597 -0.5; 3957 -1.6; 4353 -5.9; 4788 -8.8; 5267 -5.5; 5793 -2.6; 6373 -3.6; 7010 -4.2; 7711 -6.1; 8482 -6.9; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.9; 18182 -9.9; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 228 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 228 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 66 Hz    | 0.63 | -5.1 dB |
| Peaking | 153 Hz   | 1.73 | -5.9 dB |
| Peaking | 287 Hz   | 2.78 | -2.6 dB |
| Peaking | 2014 Hz  | 0.39 | 3.2 dB  |
| Peaking | 6272 Hz  | 6.21 | 2.0 dB  |
| Peaking | 634 Hz   | 2.98 | 1.6 dB  |
| Peaking | 1725 Hz  | 1.11 | -1.6 dB |
| Peaking | 3676 Hz  | 1.76 | 4.5 dB  |
| Peaking | 4652 Hz  | 5.02 | -7.0 dB |
| Peaking | 19617 Hz | 0.98 | -5.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20228/Sennheiser%20HD%20228.png)