# Denon AH-D5000 (balanced)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.1; 28 -2.8; 31 -3.2; 34 -3.5; 37 -3.6; 41 -3.9; 45 -4.0; 49 -3.8; 54 -3.6; 60 -3.8; 66 -4.0; 72 -4.2; 79 -4.4; 87 -4.6; 96 -4.6; 106 -4.8; 116 -4.9; 128 -5.0; 141 -4.9; 155 -4.8; 170 -4.8; 187 -4.9; 206 -4.9; 227 -4.7; 249 -4.6; 274 -4.3; 302 -4.2; 332 -3.9; 365 -3.6; 402 -3.3; 442 -3.0; 486 -2.6; 535 -2.0; 588 -1.2; 647 -1.0; 712 -1.9; 783 -3.7; 861 -4.0; 947 -1.5; 1042 -3.3; 1146 -4.0; 1261 -4.6; 1387 -5.2; 1526 -5.8; 1678 -6.3; 1846 -6.2; 2031 -6.0; 2234 -6.0; 2457 -4.7; 2703 -1.2; 2973 -1.0; 3270 -1.7; 3597 -2.6; 3957 -4.2; 4353 -5.4; 4788 -5.5; 5267 -4.1; 5793 -2.4; 6373 -4.8; 7010 -6.7; 7711 -6.9; 8482 -6.3; 9330 -6.9; 10263 -4.0; 11289 -2.7; 12418 -3.4; 13660 -4.8; 15026 -2.7; 16529 -2.7; 18182 -2.9; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D5000 (balanced) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 (balanced) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 2.92 | 2.6 dB  |
| Peaking | 135 Hz   | 0.65 | -2.3 dB |
| Peaking | 1751 Hz  | 2.36 | -4.0 dB |
| Peaking | 8042 Hz  | 1.79 | -4.4 dB |
| Peaking | 19872 Hz | 2.02 | -4.4 dB |
| Peaking | 608 Hz   | 2.96 | 2.7 dB  |
| Peaking | 1154 Hz  | 0.18 | -0.5 dB |
| Peaking | 2985 Hz  | 4.29 | 3.4 dB  |
| Peaking | 4570 Hz  | 4.08 | -2.3 dB |
| Peaking | 5815 Hz  | 7.76 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D5000%20(balanced)/Denon%20AH-D5000%20(balanced).png)