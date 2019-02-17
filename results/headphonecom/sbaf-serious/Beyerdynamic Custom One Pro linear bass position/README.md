# Beyerdynamic Custom One Pro linear bass position
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.3; 25 -7.7; 28 -8.2; 31 -8.5; 34 -8.8; 37 -8.9; 41 -9.0; 45 -8.9; 49 -8.4; 54 -7.6; 60 -6.4; 66 -4.6; 72 -6.6; 79 -4.4; 87 -1.3; 96 -4.6; 106 -6.7; 116 -7.2; 128 -7.8; 141 -8.0; 155 -7.9; 170 -8.9; 187 -11.0; 206 -10.9; 227 -10.8; 249 -11.0; 274 -10.8; 302 -10.4; 332 -10.0; 365 -9.6; 402 -9.3; 442 -9.0; 486 -8.8; 535 -8.5; 588 -8.0; 647 -7.8; 712 -7.8; 783 -6.8; 861 -6.7; 947 -6.7; 1042 -6.5; 1146 -6.5; 1261 -6.8; 1387 -7.4; 1526 -8.4; 1678 -9.5; 1846 -10.4; 2031 -11.4; 2234 -11.4; 2457 -10.0; 2703 -8.1; 2973 -6.6; 3270 -5.5; 3597 -4.8; 3957 -4.5; 4353 -2.0; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -3.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Pro linear bass position GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Pro linear bass position ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 38 Hz   |  1.81 | -2.7 dB |
| Peaking | 86 Hz   |  5.19 | 6.3 dB  |
| Peaking | 257 Hz  |  0.91 | -4.6 dB |
| Peaking | 2113 Hz |  2.49 | -5.7 dB |
| Peaking | 5138 Hz |  2.04 | 6.9 dB  |
| Peaking | 157 Hz  | 11.55 | 1.2 dB  |
| Peaking | 906 Hz  |  0.87 | -1.5 dB |
| Peaking | 991 Hz  |  1.51 | 2.2 dB  |
| Peaking | 6210 Hz |  4.59 | 1.0 dB  |
| Peaking | 8823 Hz |  2.68 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20Custom%20One%20Pro%20linear%20bass%20position/Beyerdynamic%20Custom%20One%20Pro%20linear%20bass%20position.png)