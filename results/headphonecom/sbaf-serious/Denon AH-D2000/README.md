# Denon AH-D2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.6; 25 -3.2; 28 -3.9; 31 -4.3; 34 -4.4; 37 -4.3; 41 -4.0; 45 -4.2; 49 -4.3; 54 -4.4; 60 -4.0; 66 -3.9; 72 -4.3; 79 -4.5; 87 -4.7; 96 -4.9; 106 -5.1; 116 -5.3; 128 -5.3; 141 -5.5; 155 -5.6; 170 -5.4; 187 -5.7; 206 -5.4; 227 -5.4; 249 -5.4; 274 -5.2; 302 -5.0; 332 -5.0; 365 -4.9; 402 -4.8; 442 -4.9; 486 -4.9; 535 -5.5; 588 -6.0; 647 -6.2; 712 -6.3; 783 -4.9; 861 -5.4; 947 -5.9; 1042 -5.8; 1146 -5.3; 1261 -4.6; 1387 -4.0; 1526 -3.9; 1678 -4.2; 1846 -4.4; 2031 -3.6; 2234 -1.6; 2457 -0.5; 2703 -0.8; 2973 -1.8; 3270 -3.3; 3597 -4.3; 3957 -4.8; 4353 -3.8; 4788 -4.3; 5267 -3.4; 5793 -4.3; 6373 -6.3; 7010 -4.9; 7711 -4.4; 8482 -4.7; 9330 -8.3; 10263 -10.5; 11289 -6.1; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -5.7; 18182 -10.6; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 1.37 | 5.9 dB  |
| Peaking | 461 Hz   | 0.27 | -0.8 dB |
| Peaking | 2555 Hz  | 2.63 | 4.7 dB  |
| Peaking | 10078 Hz | 5.66 | -6.6 dB |
| Peaking | 18814 Hz | 1.58 | -7.1 dB |
| Peaking | 667 Hz   | 5.91 | -1.0 dB |
| Peaking | 1430 Hz  | 6.81 | 1.0 dB  |
| Peaking | 3749 Hz  | 5.27 | -0.5 dB |
| Peaking | 12523 Hz | 4.09 | 0.8 dB  |
| Peaking | 15703 Hz | 3.84 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D2000/Denon%20AH-D2000.png)