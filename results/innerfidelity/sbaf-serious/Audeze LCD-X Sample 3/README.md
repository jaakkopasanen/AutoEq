# Audeze LCD-X sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.5; 25 -2.7; 28 -3.0; 31 -3.4; 34 -4.0; 37 -5.2; 41 -6.4; 45 -6.6; 49 -6.4; 54 -6.1; 60 -6.0; 66 -6.1; 72 -6.3; 79 -6.4; 87 -6.7; 96 -7.0; 106 -7.2; 116 -7.5; 128 -7.8; 141 -8.0; 155 -8.2; 170 -8.3; 187 -8.5; 206 -8.6; 227 -8.6; 249 -8.7; 274 -8.6; 302 -8.5; 332 -8.3; 365 -7.9; 402 -7.7; 442 -7.7; 486 -8.1; 535 -8.0; 588 -7.4; 647 -7.7; 712 -7.8; 783 -7.4; 861 -7.0; 947 -6.3; 1042 -6.4; 1146 -6.3; 1261 -6.4; 1387 -7.0; 1526 -7.1; 1678 -6.9; 1846 -6.9; 2031 -7.1; 2234 -7.0; 2457 -6.0; 2703 -4.1; 2973 -2.2; 3270 -1.1; 3597 -0.5; 3957 -1.0; 4353 -4.9; 4788 -7.3; 5267 -1.1; 5793 -0.6; 6373 -2.7; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.8; 16529 -9.5; 18182 -11.1; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.26 | 4.3 dB  |
| Peaking | 257 Hz   | 0.53 | -2.1 dB |
| Peaking | 3463 Hz  | 3.31 | 6.5 dB  |
| Peaking | 5810 Hz  | 4.53 | 6.1 dB  |
| Peaking | 19411 Hz | 0.81 | -6.3 dB |
| Peaking | 74 Hz    | 3.57 | 0.5 dB  |
| Peaking | 1069 Hz  | 5.37 | 0.7 dB  |
| Peaking | 2055 Hz  | 3.77 | -1.2 dB |
| Peaking | 8695 Hz  | 2.65 | -0.1 dB |
| Peaking | 14007 Hz | 3.08 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X%20sample%203/Audeze%20LCD-X%20sample%203.png)