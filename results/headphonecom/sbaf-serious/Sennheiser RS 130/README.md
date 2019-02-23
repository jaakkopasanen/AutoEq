# Sennheiser RS 130
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.7; 87 -2.2; 96 -3.2; 106 -4.6; 116 -5.2; 128 -5.8; 141 -6.7; 155 -7.2; 170 -7.4; 187 -7.7; 206 -7.3; 227 -8.4; 249 -7.9; 274 -8.1; 302 -7.9; 332 -7.5; 365 -7.4; 402 -6.9; 442 -7.1; 486 -6.8; 535 -6.6; 588 -5.0; 647 -4.2; 712 -3.6; 783 -3.9; 861 -3.8; 947 -3.1; 1042 -2.1; 1146 -2.7; 1261 -4.8; 1387 -6.4; 1526 -7.9; 1678 -7.8; 1846 -8.3; 2031 -6.7; 2234 -4.6; 2457 -2.9; 2703 -6.8; 2973 -9.5; 3270 -8.6; 3597 -9.9; 3957 -6.6; 4353 -13.6; 4788 -10.6; 5267 -7.9; 5793 -8.5; 6373 -7.6; 7010 -4.0; 7711 -6.2; 8482 -7.9; 9330 -12.0; 10263 -8.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 130 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 130 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 55 Hz    |  0.37 | 9.7 dB  |
| Peaking | 516 Hz   |  0.11 | -6.6 dB |
| Peaking | 868 Hz   |  0.7  | 9.8 dB  |
| Peaking | 2412 Hz  |  5.8  | 6.9 dB  |
| Peaking | 22050 Hz |  2.03 | -2.2 dB |
| Peaking | 1102 Hz  |  9.83 | 2.1 dB  |
| Peaking | 4464 Hz  | 11.96 | -5.2 dB |
| Peaking | 6967 Hz  |  6.33 | 5.0 dB  |
| Peaking | 9419 Hz  |  7.45 | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 6.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20130/Sennheiser%20RS%20130.png)