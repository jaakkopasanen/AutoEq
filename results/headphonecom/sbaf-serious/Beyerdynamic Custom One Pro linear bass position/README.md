# Beyerdynamic Custom One Pro linear bass position
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.7; 25 -7.1; 28 -7.5; 31 -7.9; 34 -8.1; 37 -8.3; 41 -8.3; 45 -8.3; 49 -7.8; 54 -6.9; 60 -5.8; 66 -3.9; 72 -5.9; 79 -3.7; 87 -0.7; 96 -3.9; 106 -6.0; 116 -6.5; 128 -7.1; 141 -7.3; 155 -7.3; 170 -8.3; 187 -10.3; 206 -10.2; 227 -10.1; 249 -10.3; 274 -10.1; 302 -9.7; 332 -9.3; 365 -9.0; 402 -8.6; 442 -8.3; 486 -8.1; 535 -7.8; 588 -7.4; 647 -7.2; 712 -7.1; 783 -6.1; 861 -6.0; 947 -6.0; 1042 -5.8; 1146 -5.8; 1261 -6.1; 1387 -6.7; 1526 -7.8; 1678 -8.8; 1846 -9.7; 2031 -10.7; 2234 -10.7; 2457 -9.4; 2703 -7.4; 2973 -5.9; 3270 -4.8; 3597 -4.1; 3957 -3.8; 4353 -1.3; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Pro linear bass position GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Pro linear bass position ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 2.41 | -2.2 dB |
| Peaking | 86 Hz   | 4.63 | 6.3 dB  |
| Peaking | 248 Hz  | 1.12 | -4.0 dB |
| Peaking | 2120 Hz | 2.9  | -5.3 dB |
| Peaking | 5068 Hz | 1.81 | 6.9 dB  |
| Peaking | 65 Hz   | 9.41 | 1.8 dB  |
| Peaking | 1044 Hz | 2.85 | 1.2 dB  |
| Peaking | 6462 Hz | 3.55 | 2.4 dB  |
| Peaking | 7660 Hz | 1.64 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20Custom%20One%20Pro%20linear%20bass%20position/Beyerdynamic%20Custom%20One%20Pro%20linear%20bass%20position.png)