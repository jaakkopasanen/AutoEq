# Denon AH-D600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.1; 25 -7.4; 28 -7.8; 31 -8.1; 34 -8.3; 37 -8.5; 41 -8.6; 45 -8.5; 49 -8.3; 54 -7.9; 60 -8.0; 66 -8.5; 72 -9.3; 79 -9.7; 87 -9.9; 96 -10.1; 106 -10.3; 116 -10.5; 128 -10.6; 141 -10.7; 155 -10.8; 170 -10.0; 187 -10.1; 206 -9.5; 227 -8.2; 249 -6.6; 274 -5.9; 302 -6.2; 332 -6.5; 365 -6.2; 402 -6.3; 442 -5.7; 486 -5.0; 535 -5.7; 588 -5.7; 647 -5.9; 712 -6.2; 783 -6.3; 861 -6.1; 947 -6.2; 1042 -6.2; 1146 -6.3; 1261 -6.7; 1387 -7.4; 1526 -8.2; 1678 -8.7; 1846 -9.2; 2031 -9.0; 2234 -7.3; 2457 -7.0; 2703 -7.3; 2973 -6.7; 3270 -5.5; 3597 -3.5; 3957 -2.0; 4353 -0.9; 4788 -0.5; 5267 -1.6; 5793 -4.1; 6373 -6.2; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 67 Hz   | 0.31 | -1.3 dB |
| Peaking | 160 Hz  | 0.77 | -6.3 dB |
| Peaking | 247 Hz  | 0.56 | 4.0 dB  |
| Peaking | 1862 Hz | 2.07 | -3.1 dB |
| Peaking | 4585 Hz | 2.43 | 6.6 dB  |
| Peaking | 87 Hz   | 4.23 | -0.4 dB |
| Peaking | 208 Hz  | 3.17 | -2.1 dB |
| Peaking | 270 Hz  | 1.26 | 2.4 dB  |
| Peaking | 338 Hz  | 2.34 | -2.3 dB |
| Peaking | 3751 Hz | 9.65 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D600/Denon%20AH-D600.png)