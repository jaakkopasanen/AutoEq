# Grado iGi
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.8; 25 -4.1; 28 -4.5; 31 -4.9; 34 -5.1; 37 -5.4; 41 -5.7; 45 -6.0; 49 -6.2; 54 -6.5; 60 -7.0; 66 -7.3; 72 -7.4; 79 -7.6; 87 -7.9; 96 -8.0; 106 -8.1; 116 -8.1; 128 -8.2; 141 -8.2; 155 -8.2; 170 -8.1; 187 -7.9; 206 -7.7; 227 -7.4; 249 -7.1; 274 -6.7; 302 -6.3; 332 -6.0; 365 -5.7; 402 -5.4; 442 -5.2; 486 -5.0; 535 -4.8; 588 -4.6; 647 -4.5; 712 -4.6; 783 -4.8; 861 -5.2; 947 -6.0; 1042 -6.7; 1146 -7.3; 1261 -7.9; 1387 -7.9; 1526 -7.8; 1678 -8.5; 1846 -7.4; 2031 -5.4; 2234 -2.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.9; 6373 -5.7; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado iGi GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado iGi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.61 | 3.7 dB  |
| Peaking | 127 Hz  | 0.6  | -2.1 dB |
| Peaking | 582 Hz  | 0.89 | 2.2 dB  |
| Peaking | 1606 Hz | 1.4  | -5.8 dB |
| Peaking | 3108 Hz | 0.78 | 7.9 dB  |
| Peaking | 1942 Hz | 5.42 | -1.0 dB |
| Peaking | 2401 Hz | 4.07 | 1.8 dB  |
| Peaking | 3162 Hz | 3.33 | -1.0 dB |
| Peaking | 5406 Hz | 2.85 | 4.5 dB  |
| Peaking | 6594 Hz | 1.12 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20iGi/Grado%20iGi.png)