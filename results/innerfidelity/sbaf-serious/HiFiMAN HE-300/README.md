# HiFiMAN HE-300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.8; 25 -7.1; 28 -7.4; 31 -7.7; 34 -7.9; 37 -8.1; 41 -8.3; 45 -8.4; 49 -8.7; 54 -7.9; 60 -6.8; 66 -7.8; 72 -8.7; 79 -8.9; 87 -9.2; 96 -9.5; 106 -9.4; 116 -9.2; 128 -8.7; 141 -8.2; 155 -9.2; 170 -9.3; 187 -8.8; 206 -8.2; 227 -7.6; 249 -7.1; 274 -6.4; 302 -5.7; 332 -5.2; 365 -4.5; 402 -3.9; 442 -3.0; 486 -2.4; 535 -1.6; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -1.3; 947 -3.5; 1042 -6.0; 1146 -8.1; 1261 -10.3; 1387 -11.4; 1526 -13.2; 1678 -12.6; 1846 -9.8; 2031 -9.7; 2234 -7.2; 2457 -8.5; 2703 -10.2; 2973 -12.3; 3270 -13.3; 3597 -12.2; 3957 -11.0; 4353 -11.1; 4788 -10.6; 5267 -9.7; 5793 -7.7; 6373 -2.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 137 Hz  | 0.42 | -3.1 dB |
| Peaking | 698 Hz  | 0.76 | 7.9 dB  |
| Peaking | 1427 Hz | 1.88 | -8.9 dB |
| Peaking | 3652 Hz | 1.4  | -6.1 dB |
| Peaking | 6581 Hz | 6.56 | 6.2 dB  |
| Peaking | 1666 Hz | 8.59 | -1.6 dB |
| Peaking | 2259 Hz | 7.96 | 1.9 dB  |
| Peaking | 3122 Hz | 4.34 | -3.1 dB |
| Peaking | 4116 Hz | 1.21 | 2.9 dB  |
| Peaking | 4973 Hz | 2.41 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 6.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | -4.9 dB |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-300/HiFiMAN%20HE-300.png)