# Audeze LCD-3 sn2312488
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.6; 25 -3.6; 28 -3.7; 31 -4.1; 34 -4.4; 37 -4.5; 41 -4.4; 45 -4.4; 49 -4.8; 54 -5.3; 60 -5.5; 66 -5.6; 72 -5.8; 79 -6.1; 87 -6.4; 96 -6.8; 106 -7.0; 116 -7.2; 128 -7.5; 141 -7.7; 155 -7.9; 170 -8.1; 187 -8.2; 206 -8.4; 227 -8.3; 249 -8.6; 274 -8.6; 302 -8.7; 332 -8.5; 365 -8.0; 402 -7.8; 442 -7.8; 486 -8.3; 535 -8.5; 588 -8.4; 647 -8.7; 712 -8.6; 783 -7.7; 861 -7.5; 947 -7.0; 1042 -6.1; 1146 -5.9; 1261 -5.3; 1387 -5.6; 1526 -6.3; 1678 -6.0; 1846 -5.2; 2031 -4.6; 2234 -4.8; 2457 -4.7; 2703 -5.3; 2973 -5.5; 3270 -5.8; 3597 -4.6; 3957 -2.7; 4353 -0.5; 4788 -0.5; 5267 -1.5; 5793 -4.1; 6373 -2.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.5; 18182 -11.2; 20000 -10.5
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

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.51 | 2.9 dB  |
| Peaking | 227 Hz   | 0.73 | -2.2 dB |
| Peaking | 638 Hz   | 2.81 | -1.9 dB |
| Peaking | 4728 Hz  | 1.83 | 6.1 dB  |
| Peaking | 18939 Hz | 1.1  | -5.6 dB |
| Peaking | 2288 Hz  | 2.13 | 1.5 dB  |
| Peaking | 3865 Hz  | 1.12 | -4.4 dB |
| Peaking | 4182 Hz  | 5.95 | 2.7 dB  |
| Peaking | 4954 Hz  | 0.44 | 2.5 dB  |
| Peaking | 8778 Hz  | 1.92 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2312488/Audeze%20LCD-3%20sn2312488.png)