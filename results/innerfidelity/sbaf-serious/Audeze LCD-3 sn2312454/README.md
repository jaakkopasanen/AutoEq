# Audeze LCD-3 sn2312454
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -2.9; 25 -2.8; 28 -2.8; 31 -3.0; 34 -3.2; 37 -3.4; 41 -3.3; 45 -3.2; 49 -3.5; 54 -4.7; 60 -5.0; 66 -5.0; 72 -5.1; 79 -5.3; 87 -5.6; 96 -6.0; 106 -6.2; 116 -6.4; 128 -6.7; 141 -6.9; 155 -7.1; 170 -7.3; 187 -7.4; 206 -7.6; 227 -7.5; 249 -7.6; 274 -7.7; 302 -7.8; 332 -7.9; 365 -7.9; 402 -7.8; 442 -7.6; 486 -7.4; 535 -7.5; 588 -7.4; 647 -7.7; 712 -7.8; 783 -7.4; 861 -7.0; 947 -6.2; 1042 -5.7; 1146 -5.7; 1261 -5.3; 1387 -5.6; 1526 -6.0; 1678 -5.7; 1846 -5.1; 2031 -4.8; 2234 -5.1; 2457 -4.9; 2703 -5.1; 2973 -4.9; 3270 -4.5; 3597 -3.4; 3957 -3.5; 4353 -2.7; 4788 -0.6; 5267 -0.9; 5793 -1.3; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.1; 16529 -9.0; 18182 -12.6; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 sn2312454 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2312454 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.65 | 3.3 dB  |
| Peaking | 267 Hz   | 0.64 | -2.0 dB |
| Peaking | 692 Hz   | 3.57 | -1.3 dB |
| Peaking | 5263 Hz  | 1.59 | 5.6 dB  |
| Peaking | 18598 Hz | 1.23 | -7.4 dB |
| Peaking | 1991 Hz  | 2.2  | 0.7 dB  |
| Peaking | 5584 Hz  | 7.93 | -2.0 dB |
| Peaking | 6387 Hz  | 3.63 | 3.4 dB  |
| Peaking | 7550 Hz  | 2.35 | -2.4 dB |
| Peaking | 14652 Hz | 3.11 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2312454/Audeze%20LCD-3%20sn2312454.png)