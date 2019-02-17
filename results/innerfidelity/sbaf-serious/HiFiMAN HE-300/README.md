# HiFiMAN HE-300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.7; 25 -8.0; 28 -8.3; 31 -8.5; 34 -8.8; 37 -9.0; 41 -9.1; 45 -9.3; 49 -9.5; 54 -8.8; 60 -7.6; 66 -8.6; 72 -9.6; 79 -9.8; 87 -10.0; 96 -10.3; 106 -10.2; 116 -10.0; 128 -9.5; 141 -9.0; 155 -10.0; 170 -10.1; 187 -9.7; 206 -9.0; 227 -8.4; 249 -8.0; 274 -7.3; 302 -6.5; 332 -6.0; 365 -5.3; 402 -4.7; 442 -3.9; 486 -3.2; 535 -2.4; 588 -1.1; 647 -0.5; 712 -1.2; 783 -0.5; 861 -2.1; 947 -4.4; 1042 -6.8; 1146 -9.0; 1261 -11.1; 1387 -12.3; 1526 -14.0; 1678 -13.4; 1846 -10.6; 2031 -10.5; 2234 -8.0; 2457 -9.4; 2703 -11.1; 2973 -13.1; 3270 -14.1; 3597 -13.0; 3957 -11.8; 4353 -11.9; 4788 -11.4; 5267 -10.5; 5793 -8.5; 6373 -3.4; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -6.8; 10263 -7.5; 11289 -6.0; 12418 -5.8; 13660 -6.8; 15026 -6.5; 16529 -5.8; 18182 -5.8; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 0.34 | -2.6 dB |
| Peaking | 158 Hz   | 0.69 | -3.1 dB |
| Peaking | 700 Hz   | 1.13 | 6.9 dB  |
| Peaking | 1452 Hz  | 1.83 | -9.0 dB |
| Peaking | 3554 Hz  | 1.69 | -7.7 dB |
| Peaking | 3152 Hz  | 4.29 | -4.1 dB |
| Peaking | 3386 Hz  | 1.68 | 3.7 dB  |
| Peaking | 5160 Hz  | 1.92 | -4.0 dB |
| Peaking | 6659 Hz  | 4.88 | 6.8 dB  |
| Peaking | 10052 Hz | 7.42 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 5.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB |
| Peaking | 4000 Hz  | 1.41 | -6.4 dB |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-300/HiFiMAN%20HE-300.png)