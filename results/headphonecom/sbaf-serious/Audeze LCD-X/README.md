# Audeze LCD-X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.0; 25 -5.0; 28 -5.0; 31 -5.1; 34 -5.3; 37 -5.5; 41 -5.9; 45 -6.2; 49 -6.2; 54 -6.2; 60 -6.6; 66 -6.7; 72 -6.7; 79 -7.1; 87 -7.4; 96 -7.6; 106 -7.8; 116 -8.0; 128 -8.2; 141 -8.4; 155 -8.6; 170 -8.7; 187 -8.8; 206 -8.8; 227 -8.8; 249 -8.8; 274 -8.9; 302 -9.0; 332 -9.0; 365 -8.8; 402 -8.4; 442 -8.6; 486 -8.6; 535 -8.4; 588 -8.1; 647 -8.0; 712 -8.1; 783 -8.2; 861 -8.1; 947 -7.5; 1042 -7.6; 1146 -7.3; 1261 -8.0; 1387 -8.5; 1526 -9.3; 1678 -9.8; 1846 -9.2; 2031 -9.0; 2234 -9.6; 2457 -7.1; 2703 -6.0; 2973 -5.3; 3270 -1.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.4; 5267 -0.7; 5793 -1.0; 6373 -1.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.2; 16529 -11.2; 18182 -12.6; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 274 Hz   | 0.5  | -2.5 dB |
| Peaking | 2020 Hz  | 1.28 | -4.0 dB |
| Peaking | 3743 Hz  | 1.8  | 6.9 dB  |
| Peaking | 5743 Hz  | 2.67 | 4.6 dB  |
| Peaking | 18095 Hz | 1.15 | -6.7 dB |
| Peaking | 26 Hz    | 1.09 | 1.8 dB  |
| Peaking | 796 Hz   | 6.13 | -0.5 dB |
| Peaking | 1131 Hz  | 6.72 | 0.7 dB  |
| Peaking | 8042 Hz  | 6.01 | -1.2 dB |
| Peaking | 13580 Hz | 3.71 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -4.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-X/Audeze%20LCD-X.png)