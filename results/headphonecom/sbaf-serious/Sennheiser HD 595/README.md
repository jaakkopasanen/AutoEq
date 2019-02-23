# Sennheiser HD 595
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.3; 41 -2.0; 45 -2.7; 49 -3.2; 54 -3.3; 60 -3.6; 66 -3.9; 72 -3.1; 79 -4.7; 87 -5.8; 96 -6.5; 106 -6.9; 116 -7.2; 128 -7.7; 141 -8.1; 155 -8.3; 170 -8.3; 187 -8.5; 206 -8.5; 227 -8.5; 249 -8.7; 274 -8.7; 302 -8.6; 332 -8.4; 365 -8.0; 402 -7.7; 442 -7.3; 486 -7.5; 535 -7.6; 588 -7.7; 647 -7.4; 712 -6.7; 783 -7.1; 861 -7.0; 947 -7.2; 1042 -7.3; 1146 -6.9; 1261 -6.5; 1387 -6.1; 1526 -5.9; 1678 -5.7; 1846 -5.8; 2031 -6.4; 2234 -6.8; 2457 -6.3; 2703 -5.5; 2973 -5.9; 3270 -6.3; 3597 -5.6; 3957 -4.8; 4353 -3.5; 4788 -4.7; 5267 -3.8; 5793 -0.7; 6373 -2.3; 7010 -6.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.7; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 595 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 595 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 18 Hz   |  0.28 | 6.3 dB  |
| Peaking | 137 Hz  |  0.97 | -2.4 dB |
| Peaking | 278 Hz  |  1.28 | -1.8 dB |
| Peaking | 576 Hz  |  3.28 | -0.8 dB |
| Peaking | 5799 Hz |  3.93 | 5.9 dB  |
| Peaking | 689 Hz  |  6.34 | 0.4 dB  |
| Peaking | 1006 Hz |  3.03 | -0.8 dB |
| Peaking | 1614 Hz |  3.06 | 0.9 dB  |
| Peaking | 4251 Hz |  6.8  | 2.2 dB  |
| Peaking | 6949 Hz | 10.71 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20595/Sennheiser%20HD%20595.png)