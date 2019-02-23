# Audeze LCD-4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.7; 25 -3.8; 28 -3.9; 31 -4.1; 34 -4.2; 37 -4.2; 41 -4.3; 45 -4.5; 49 -4.6; 54 -4.8; 60 -5.0; 66 -5.1; 72 -5.3; 79 -5.6; 87 -6.0; 96 -6.3; 106 -6.6; 116 -6.7; 128 -7.0; 141 -7.3; 155 -7.5; 170 -7.6; 187 -7.7; 206 -7.8; 227 -7.7; 249 -7.8; 274 -7.8; 302 -8.0; 332 -8.0; 365 -8.0; 402 -8.1; 442 -8.2; 486 -8.4; 535 -8.3; 588 -8.2; 647 -8.2; 712 -8.2; 783 -8.1; 861 -8.4; 947 -8.2; 1042 -8.3; 1146 -8.6; 1261 -8.6; 1387 -8.8; 1526 -9.6; 1678 -9.5; 1846 -9.0; 2031 -8.8; 2234 -8.5; 2457 -7.0; 2703 -6.3; 2973 -5.2; 3270 -3.3; 3597 -3.5; 3957 -1.0; 4353 -0.5; 4788 -1.4; 5267 -1.8; 5793 -3.2; 6373 -4.5; 7010 -4.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.9; 18182 -12.0; 20000 -15.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.38 | 2.9 dB  |
| Peaking | 64 Hz    | 0.96 | 1.0 dB  |
| Peaking | 428 Hz   | 0.21 | -1.7 dB |
| Peaking | 1781 Hz  | 1.53 | -2.5 dB |
| Peaking | 4367 Hz  | 1.64 | 6.6 dB  |
| Peaking | 494 Hz   | 5.42 | -0.2 dB |
| Peaking | 5513 Hz  | 8.07 | 0.8 dB  |
| Peaking | 15737 Hz | 1.21 | 3.1 dB  |
| Peaking | 19787 Hz | 0.51 | -9.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-4/Audeze%20LCD-4.png)