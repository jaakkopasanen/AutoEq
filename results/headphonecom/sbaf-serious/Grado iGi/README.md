# Grado iGi
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.1; 25 -6.4; 28 -6.8; 31 -7.2; 34 -7.4; 37 -7.7; 41 -8.0; 45 -8.3; 49 -8.5; 54 -8.8; 60 -9.3; 66 -9.6; 72 -9.7; 79 -9.9; 87 -10.2; 96 -10.3; 106 -10.4; 116 -10.4; 128 -10.5; 141 -10.5; 155 -10.5; 170 -10.4; 187 -10.2; 206 -10.0; 227 -9.7; 249 -9.4; 274 -9.0; 302 -8.6; 332 -8.3; 365 -8.0; 402 -7.7; 442 -7.5; 486 -7.3; 535 -7.1; 588 -6.9; 647 -6.8; 712 -6.9; 783 -7.1; 861 -7.5; 947 -8.3; 1042 -9.0; 1146 -9.6; 1261 -10.1; 1387 -10.2; 1526 -10.1; 1678 -10.8; 1846 -9.7; 2031 -7.7; 2234 -5.0; 2457 -2.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -1.2; 5793 -3.1; 6373 -8.0; 7010 -6.6; 7711 -6.2; 8482 -6.5; 9330 -7.2; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado iGi GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado iGi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.53 | 1.6 dB  |
| Peaking | 88 Hz   | 0.6  | -3.2 dB |
| Peaking | 193 Hz  | 0.97 | -2.2 dB |
| Peaking | 1631 Hz | 1.33 | -7.1 dB |
| Peaking | 3138 Hz | 1.03 | 8.5 dB  |
| Peaking | 1999 Hz | 4.19 | -0.7 dB |
| Peaking | 2556 Hz | 4.94 | 1.7 dB  |
| Peaking | 3249 Hz | 3.49 | -1.5 dB |
| Peaking | 5360 Hz | 2.35 | 6.8 dB  |
| Peaking | 6167 Hz | 1.86 | -6.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20iGi/Grado%20iGi.png)