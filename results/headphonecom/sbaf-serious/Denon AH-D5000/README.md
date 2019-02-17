# Denon AH-D5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.8; 28 -2.4; 31 -2.7; 34 -3.0; 37 -3.3; 41 -3.5; 45 -3.3; 49 -3.3; 54 -3.5; 60 -3.7; 66 -3.8; 72 -4.0; 79 -4.2; 87 -4.5; 96 -4.7; 106 -4.7; 116 -4.8; 128 -5.1; 141 -5.1; 155 -5.2; 170 -5.1; 187 -4.9; 206 -4.8; 227 -4.7; 249 -4.7; 274 -4.7; 302 -4.6; 332 -4.2; 365 -3.8; 402 -3.4; 442 -3.0; 486 -2.6; 535 -2.0; 588 -1.2; 647 -1.1; 712 -2.3; 783 -4.3; 861 -3.5; 947 -1.6; 1042 -3.3; 1146 -4.0; 1261 -4.5; 1387 -5.2; 1526 -5.8; 1678 -6.3; 1846 -6.3; 2031 -5.9; 2234 -5.2; 2457 -4.0; 2703 -1.5; 2973 -1.5; 3270 -2.2; 3597 -3.1; 3957 -4.7; 4353 -6.4; 4788 -5.8; 5267 -4.3; 5793 -2.9; 6373 -4.7; 7010 -6.9; 7711 -6.6; 8482 -6.2; 9330 -7.8; 10263 -3.7; 11289 -2.6; 12418 -2.6; 13660 -3.5; 15026 -2.6; 16529 -2.6; 18182 -2.6; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 2.65 | 2.6 dB  |
| Peaking | 146 Hz   | 0.65 | -2.6 dB |
| Peaking | 1729 Hz  | 2.34 | -4.0 dB |
| Peaking | 7987 Hz  | 1.51 | -4.3 dB |
| Peaking | 19837 Hz | 2.6  | -7.5 dB |
| Peaking | 606 Hz   | 5.04 | 2.3 dB  |
| Peaking | 2957 Hz  | 4.62 | 2.5 dB  |
| Peaking | 4455 Hz  | 3.69 | -3.2 dB |
| Peaking | 5825 Hz  | 6.98 | 2.3 dB  |
| Peaking | 16526 Hz | 0.56 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D5000/Denon%20AH-D5000.png)