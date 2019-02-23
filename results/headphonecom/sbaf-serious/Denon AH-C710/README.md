# Denon AH-C710
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.9; 23 -12.8; 25 -12.8; 28 -12.8; 31 -12.7; 34 -12.7; 37 -12.6; 41 -12.5; 45 -12.5; 49 -12.4; 54 -12.4; 60 -12.4; 66 -12.3; 72 -12.3; 79 -12.2; 87 -12.0; 96 -11.9; 106 -11.6; 116 -11.4; 128 -11.1; 141 -10.8; 155 -10.4; 170 -10.0; 187 -9.5; 206 -9.0; 227 -8.4; 249 -7.8; 274 -7.2; 302 -6.3; 332 -5.6; 365 -5.1; 402 -4.5; 442 -3.8; 486 -3.2; 535 -2.5; 588 -1.9; 647 -1.4; 712 -0.9; 783 -0.6; 861 -0.5; 947 -0.7; 1042 -0.9; 1146 -1.0; 1261 -1.5; 1387 -2.3; 1526 -3.1; 1678 -3.6; 1846 -3.9; 2031 -4.5; 2234 -5.1; 2457 -6.0; 2703 -6.9; 2973 -6.4; 3270 -3.8; 3597 -1.4; 3957 -1.6; 4353 -3.5; 4788 -5.2; 5267 -7.1; 5793 -11.1; 6373 -8.5; 7010 -4.1; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.3; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C710 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C710 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.29 | -7.3 dB |
| Peaking | 125 Hz  | 0.57 | -4.4 dB |
| Peaking | 802 Hz  | 0.93 | 5.2 dB  |
| Peaking | 3816 Hz | 6.23 | 4.4 dB  |
| Peaking | 5868 Hz | 6.76 | -7.2 dB |
| Peaking | 1194 Hz | 7.19 | 0.7 dB  |
| Peaking | 1347 Hz | 4.13 | 0.5 dB  |
| Peaking | 2836 Hz | 3.12 | -3.7 dB |
| Peaking | 3329 Hz | 3.33 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C710/Denon%20AH-C710.png)