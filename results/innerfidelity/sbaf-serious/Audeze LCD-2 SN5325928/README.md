# Audeze LCD-2 sn5325928
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.1; 25 -2.1; 28 -2.1; 31 -2.1; 34 -2.2; 37 -2.3; 41 -2.4; 45 -2.5; 49 -2.7; 54 -2.9; 60 -3.2; 66 -3.4; 72 -3.6; 79 -3.8; 87 -4.2; 96 -4.5; 106 -4.8; 116 -5.0; 128 -5.3; 141 -5.5; 155 -5.7; 170 -5.8; 187 -6.0; 206 -6.1; 227 -6.0; 249 -6.2; 274 -6.2; 302 -6.1; 332 -6.1; 365 -6.2; 402 -6.3; 442 -6.3; 486 -6.5; 535 -6.6; 588 -6.7; 647 -6.9; 712 -6.7; 783 -6.6; 861 -6.8; 947 -6.7; 1042 -6.3; 1146 -6.5; 1261 -6.4; 1387 -7.0; 1526 -7.5; 1678 -7.7; 1846 -6.7; 2031 -6.2; 2234 -5.6; 2457 -4.5; 2703 -3.9; 2973 -3.0; 3270 -1.7; 3597 -0.5; 3957 -0.5; 4353 -1.6; 4788 -2.4; 5267 -1.1; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.7; 18182 -9.2; 20000 -8.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 sn5325928 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 sn5325928 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.38 | 4.5 dB  |
| Peaking | 1636 Hz  | 3.04 | -1.7 dB |
| Peaking | 3682 Hz  | 1.76 | 5.6 dB  |
| Peaking | 6063 Hz  | 2.49 | 6.4 dB  |
| Peaking | 7570 Hz  | 1.7  | -2.2 dB |
| Peaking | 756 Hz   | 1.59 | -0.4 dB |
| Peaking | 1153 Hz  | 3.27 | 0.3 dB  |
| Peaking | 15381 Hz | 0.89 | 1.4 dB  |
| Peaking | 18539 Hz | 0.66 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20sn5325928/Audeze%20LCD-2%20sn5325928.png)