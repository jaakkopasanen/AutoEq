# Denon AH-D2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.6; 25 -3.2; 28 -3.9; 31 -4.3; 34 -4.4; 37 -4.3; 41 -4.0; 45 -4.2; 49 -4.3; 54 -4.4; 60 -4.0; 66 -3.9; 72 -4.3; 79 -4.5; 87 -4.7; 96 -4.9; 106 -5.1; 116 -5.3; 128 -5.3; 141 -5.5; 155 -5.6; 170 -5.4; 187 -5.7; 206 -5.4; 227 -5.4; 249 -5.4; 274 -5.2; 302 -5.0; 332 -5.0; 365 -4.9; 402 -4.8; 442 -4.9; 486 -4.9; 535 -5.5; 588 -6.0; 647 -6.2; 712 -6.3; 783 -4.9; 861 -5.4; 947 -5.9; 1042 -5.8; 1146 -5.3; 1261 -4.6; 1387 -4.0; 1526 -3.9; 1678 -4.2; 1846 -4.4; 2031 -3.6; 2234 -1.6; 2457 -0.5; 2703 -0.8; 2973 -1.8; 3270 -3.3; 3597 -4.3; 3957 -4.8; 4353 -3.8; 4788 -4.3; 5267 -3.4; 5793 -4.3; 6373 -6.3; 7010 -4.9; 7711 -5.5; 8482 -5.8; 9330 -8.3; 10263 -10.5; 11289 -6.5; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -6.1; 18182 -10.6; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 2549 Hz  | 3.12 | 4.3 dB  |
| Peaking | 3195 Hz  | 0.45 | 1.4 dB  |
| Peaking | 9599 Hz  | 5.67 | -2.3 dB |
| Peaking | 10308 Hz | 5.57 | -3.9 dB |
| Peaking | 18 Hz    | 1.43 | 5.2 dB  |
| Peaking | 62 Hz    | 1.11 | 1.5 dB  |
| Peaking | 364 Hz   | 2.42 | 1.0 dB  |
| Peaking | 16254 Hz | 1.08 | 2.3 dB  |
| Peaking | 18554 Hz | 1.05 | -6.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D2000/Denon%20AH-D2000.png)