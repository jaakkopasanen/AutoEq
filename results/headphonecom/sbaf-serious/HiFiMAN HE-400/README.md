# HiFiMAN HE-400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -0.9; 72 -1.0; 79 -1.2; 87 -1.5; 96 -1.9; 106 -2.1; 116 -2.3; 128 -2.5; 141 -2.8; 155 -3.2; 170 -3.4; 187 -1.8; 206 -1.8; 227 -2.6; 249 -2.9; 274 -3.1; 302 -3.0; 332 -3.2; 365 -4.0; 402 -3.8; 442 -0.6; 486 -0.8; 535 -1.5; 588 -2.7; 647 -3.2; 712 -4.3; 783 -5.2; 861 -5.4; 947 -5.6; 1042 -6.1; 1146 -4.7; 1261 -4.1; 1387 -2.2; 1526 -1.3; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.5; 9330 -9.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.34 | 5.5 dB  |
| Peaking | 76 Hz   | 0.69 | 2.8 dB  |
| Peaking | 224 Hz  | 1.42 | 2.9 dB  |
| Peaking | 490 Hz  | 2.99 | 5.0 dB  |
| Peaking | 3012 Hz | 0.62 | 6.9 dB  |
| Peaking | 1036 Hz | 3.68 | -2.1 dB |
| Peaking | 1643 Hz | 2.89 | 2.0 dB  |
| Peaking | 2988 Hz | 2.14 | -1.2 dB |
| Peaking | 5923 Hz | 2.52 | 3.2 dB  |
| Peaking | 8852 Hz | 2.53 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 2.7 dB  |
| Peaking | 250 Hz   | 1.41 | 2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 4.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-400/HiFiMAN%20HE-400.png)