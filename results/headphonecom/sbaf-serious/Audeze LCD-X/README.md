# Audeze LCD-X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -3.9; 25 -3.9; 28 -3.9; 31 -4.0; 34 -4.2; 37 -4.5; 41 -4.8; 45 -5.1; 49 -5.1; 54 -5.1; 60 -5.5; 66 -5.6; 72 -5.6; 79 -6.1; 87 -6.3; 96 -6.5; 106 -6.7; 116 -6.9; 128 -7.1; 141 -7.3; 155 -7.5; 170 -7.6; 187 -7.7; 206 -7.7; 227 -7.7; 249 -7.7; 274 -7.8; 302 -7.9; 332 -7.9; 365 -7.7; 402 -7.3; 442 -7.5; 486 -7.5; 535 -7.3; 588 -7.0; 647 -6.9; 712 -7.0; 783 -7.1; 861 -7.0; 947 -6.4; 1042 -6.5; 1146 -6.2; 1261 -6.9; 1387 -7.4; 1526 -8.2; 1678 -8.8; 1846 -8.1; 2031 -8.0; 2234 -8.5; 2457 -6.1; 2703 -4.9; 2973 -4.2; 3270 -0.8; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.2; 16529 -10.1; 18182 -11.5; 20000 -7.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.39 | 2.7 dB  |
| Peaking | 235 Hz   | 0.55 | -1.5 dB |
| Peaking | 2015 Hz  | 1.68 | -3.8 dB |
| Peaking | 4273 Hz  | 1.04 | 7.3 dB  |
| Peaking | 18055 Hz | 1.14 | -5.4 dB |
| Peaking | 3380 Hz  | 8.09 | 1.9 dB  |
| Peaking | 4334 Hz  | 1.74 | -1.1 dB |
| Peaking | 6339 Hz  | 2.71 | 4.3 dB  |
| Peaking | 7505 Hz  | 2.01 | -3.4 dB |
| Peaking | 14265 Hz | 3.67 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-X/Audeze%20LCD-X.png)