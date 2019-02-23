# Audeze LCD-X sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -2.9; 25 -3.1; 28 -3.4; 31 -3.8; 34 -4.4; 37 -5.6; 41 -6.8; 45 -7.0; 49 -6.8; 54 -6.5; 60 -6.4; 66 -6.5; 72 -6.7; 79 -6.8; 87 -7.1; 96 -7.4; 106 -7.6; 116 -7.9; 128 -8.2; 141 -8.4; 155 -8.6; 170 -8.8; 187 -8.9; 206 -9.0; 227 -9.0; 249 -9.1; 274 -9.0; 302 -8.9; 332 -8.7; 365 -8.4; 402 -8.1; 442 -8.1; 486 -8.5; 535 -8.4; 588 -7.8; 647 -8.1; 712 -8.2; 783 -7.8; 861 -7.4; 947 -6.7; 1042 -6.8; 1146 -6.7; 1261 -6.8; 1387 -7.4; 1526 -7.5; 1678 -7.3; 1846 -7.3; 2031 -7.5; 2234 -7.4; 2457 -6.5; 2703 -4.5; 2973 -2.6; 3270 -1.5; 3597 -0.5; 3957 -1.3; 4353 -5.3; 4788 -7.7; 5267 -1.0; 5793 -0.7; 6373 -3.1; 7010 -4.2; 7711 -6.1; 8482 -6.3; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -7.0; 16529 -9.9; 18182 -11.5; 20000 -13.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.48 | 3.8 dB  |
| Peaking | 283 Hz   | 0.36 | -2.5 dB |
| Peaking | 3494 Hz  | 3.68 | 6.4 dB  |
| Peaking | 5765 Hz  | 5    | 6.0 dB  |
| Peaking | 19493 Hz | 0.8  | -6.9 dB |
| Peaking | 1028 Hz  | 3.83 | 0.8 dB  |
| Peaking | 2007 Hz  | 2.5  | -1.4 dB |
| Peaking | 4525 Hz  | 2.1  | 2.4 dB  |
| Peaking | 4694 Hz  | 7.83 | -6.4 dB |
| Peaking | 13905 Hz | 4.05 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X%20sample%203/Audeze%20LCD-X%20sample%203.png)