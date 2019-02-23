# Audeze LCD-3 sn2312488
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.1; 25 -4.1; 28 -4.3; 31 -4.7; 34 -5.0; 37 -5.0; 41 -4.9; 45 -4.9; 49 -5.3; 54 -5.9; 60 -6.0; 66 -6.1; 72 -6.3; 79 -6.6; 87 -6.9; 96 -7.3; 106 -7.5; 116 -7.7; 128 -8.0; 141 -8.3; 155 -8.5; 170 -8.6; 187 -8.8; 206 -8.9; 227 -8.9; 249 -9.1; 274 -9.1; 302 -9.2; 332 -9.0; 365 -8.6; 402 -8.3; 442 -8.4; 486 -8.8; 535 -9.1; 588 -9.0; 647 -9.2; 712 -9.1; 783 -8.3; 861 -8.1; 947 -7.6; 1042 -6.7; 1146 -6.5; 1261 -5.8; 1387 -6.1; 1526 -6.9; 1678 -6.6; 1846 -5.8; 2031 -5.1; 2234 -5.3; 2457 -5.2; 2703 -5.8; 2973 -6.0; 3270 -6.3; 3597 -5.1; 3957 -3.2; 4353 -0.5; 4788 -0.6; 5267 -2.1; 5793 -4.6; 6373 -3.5; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.0; 18182 -11.8; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 sn2312488 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2312488 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 23 Hz    |  0.54 | 2.4 dB  |
| Peaking | 228 Hz   |  0.63 | -2.6 dB |
| Peaking | 647 Hz   |  2.31 | -2.2 dB |
| Peaking | 4703 Hz  |  2.33 | 6.2 dB  |
| Peaking | 18921 Hz |  1.11 | -6.2 dB |
| Peaking | 2174 Hz  |  3.42 | 0.8 dB  |
| Peaking | 2273 Hz  |  1.22 | 0.4 dB  |
| Peaking | 3280 Hz  |  4.27 | -1.6 dB |
| Peaking | 6705 Hz  | 10.26 | 2.0 dB  |
| Peaking | 14848 Hz |  3.76 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2312488/Audeze%20LCD-3%20sn2312488.png)