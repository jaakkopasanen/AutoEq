# Sennheiser RS 220
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.0; 31 -1.6; 34 -2.0; 37 -2.5; 41 -3.0; 45 -3.4; 49 -3.8; 54 -4.2; 60 -4.8; 66 -4.6; 72 -4.2; 79 -5.6; 87 -6.3; 96 -6.9; 106 -7.3; 116 -7.5; 128 -7.8; 141 -8.0; 155 -8.0; 170 -8.0; 187 -8.1; 206 -8.2; 227 -7.8; 249 -7.5; 274 -7.4; 302 -7.3; 332 -7.2; 365 -6.9; 402 -7.0; 442 -7.0; 486 -6.6; 535 -6.2; 588 -6.2; 647 -6.1; 712 -6.0; 783 -6.1; 861 -6.2; 947 -6.3; 1042 -6.5; 1146 -6.5; 1261 -6.8; 1387 -5.3; 1526 -2.8; 1678 -2.2; 1846 -2.4; 2031 -4.6; 2234 -8.4; 2457 -10.4; 2703 -9.1; 2973 -7.2; 3270 -6.2; 3597 -3.7; 3957 -0.7; 4353 -0.5; 4788 -0.5; 5267 -2.3; 5793 -4.3; 6373 -1.4; 7010 -6.4; 7711 -7.0; 8482 -6.5; 9330 -6.7; 10263 -7.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 220 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.47 | 6.1 dB  |
| Peaking | 43 Hz   | 1.99 | 2.3 dB  |
| Peaking | 1810 Hz | 2.69 | 7.0 dB  |
| Peaking | 2441 Hz | 1.91 | -6.5 dB |
| Peaking | 4401 Hz | 1.9  | 7.3 dB  |
| Peaking | 72 Hz   | 3.96 | 2.0 dB  |
| Peaking | 162 Hz  | 0.75 | -1.8 dB |
| Peaking | 629 Hz  | 2.77 | 0.6 dB  |
| Peaking | 6370 Hz | 7.81 | 5.8 dB  |
| Peaking | 6996 Hz | 2.25 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20220/Sennheiser%20RS%20220.png)