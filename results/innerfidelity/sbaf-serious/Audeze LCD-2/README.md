# Audeze LCD-2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.5; 25 -3.6; 28 -3.6; 31 -3.6; 34 -3.6; 37 -3.6; 41 -3.8; 45 -4.0; 49 -4.2; 54 -4.3; 60 -4.7; 66 -5.1; 72 -5.4; 79 -5.6; 87 -5.8; 96 -6.2; 106 -6.4; 116 -6.6; 128 -6.9; 141 -7.2; 155 -7.4; 170 -7.5; 187 -7.6; 206 -7.8; 227 -7.8; 249 -8.0; 274 -8.0; 302 -8.0; 332 -8.0; 365 -8.0; 402 -7.9; 442 -7.7; 486 -7.7; 535 -7.6; 588 -7.6; 647 -7.9; 712 -8.2; 783 -8.1; 861 -8.2; 947 -7.6; 1042 -6.7; 1146 -5.8; 1261 -5.6; 1387 -6.1; 1526 -6.6; 1678 -6.1; 1846 -5.0; 2031 -4.7; 2234 -5.1; 2457 -4.5; 2703 -4.3; 2973 -3.7; 3270 -3.0; 3597 -1.7; 3957 -0.5; 4353 -1.4; 4788 -2.7; 5267 -3.0; 5793 -2.6; 6373 -2.1; 7010 -3.4; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -6.4; 18182 -9.5; 20000 -9.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.79 | 1.9 dB  |
| Peaking | 42 Hz    | 0.78 | 1.8 dB  |
| Peaking | 332 Hz   | 0.36 | -2.3 dB |
| Peaking | 3948 Hz  | 1.71 | 4.9 dB  |
| Peaking | 6341 Hz  | 5.04 | 3.0 dB  |
| Peaking | 516 Hz   | 2.04 | 0.5 dB  |
| Peaking | 846 Hz   | 2.3  | -1.3 dB |
| Peaking | 1167 Hz  | 3.63 | 1.4 dB  |
| Peaking | 19204 Hz | 1.2  | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2/Audeze%20LCD-2.png)