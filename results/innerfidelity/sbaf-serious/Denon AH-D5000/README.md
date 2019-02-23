# Denon AH-D5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.1; 28 -2.4; 31 -3.6; 34 -4.7; 37 -5.4; 41 -5.9; 45 -6.2; 49 -6.5; 54 -6.6; 60 -6.5; 66 -6.5; 72 -6.7; 79 -6.8; 87 -6.7; 96 -6.7; 106 -6.7; 116 -6.7; 128 -6.8; 141 -6.9; 155 -7.0; 170 -6.8; 187 -6.7; 206 -6.5; 227 -6.3; 249 -6.1; 274 -5.9; 302 -5.7; 332 -5.3; 365 -5.0; 402 -4.8; 442 -4.5; 486 -4.7; 535 -5.3; 588 -6.1; 647 -7.3; 712 -8.6; 783 -9.4; 861 -10.2; 947 -8.0; 1042 -7.9; 1146 -8.3; 1261 -7.6; 1387 -7.2; 1526 -7.0; 1678 -6.4; 1846 -5.7; 2031 -5.0; 2234 -4.6; 2457 -5.1; 2703 -6.1; 2973 -7.2; 3270 -7.9; 3597 -8.4; 3957 -7.4; 4353 -6.7; 4788 -5.3; 5267 -4.2; 5793 -5.6; 6373 -6.4; 7010 -5.9; 7711 -6.2; 8482 -6.5; 9330 -9.5; 10263 -10.1; 11289 -9.0; 12418 -8.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.1; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 2.13 | 6.4 dB  |
| Peaking | 472 Hz   | 1.6  | 2.8 dB  |
| Peaking | 809 Hz   | 1.7  | -3.7 dB |
| Peaking | 2192 Hz  | 4.57 | 2.3 dB  |
| Peaking | 10389 Hz | 3.25 | -4.0 dB |
| Peaking | 11 Hz    | 0.98 | 1.4 dB  |
| Peaking | 80 Hz    | 0.58 | -0.5 dB |
| Peaking | 3529 Hz  | 4.15 | -2.1 dB |
| Peaking | 5258 Hz  | 5.48 | 2.7 dB  |
| Peaking | 7405 Hz  | 5.94 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D5000/Denon%20AH-D5000.png)