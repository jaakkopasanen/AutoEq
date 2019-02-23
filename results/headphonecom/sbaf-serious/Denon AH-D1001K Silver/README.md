# Denon AH-D1001K Silver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.4; 37 -2.2; 41 -3.1; 45 -3.8; 49 -4.3; 54 -4.6; 60 -5.0; 66 -5.5; 72 -6.1; 79 -6.7; 87 -7.2; 96 -7.5; 106 -7.8; 116 -7.9; 128 -7.9; 141 -7.6; 155 -7.5; 170 -7.6; 187 -7.2; 206 -6.8; 227 -6.8; 249 -6.8; 274 -6.5; 302 -6.3; 332 -5.9; 365 -5.6; 402 -5.2; 442 -5.1; 486 -5.0; 535 -5.0; 588 -5.2; 647 -5.9; 712 -7.0; 783 -8.2; 861 -8.8; 947 -9.1; 1042 -9.0; 1146 -8.3; 1261 -8.2; 1387 -8.0; 1526 -7.9; 1678 -7.6; 1846 -6.9; 2031 -5.9; 2234 -4.9; 2457 -4.3; 2703 -4.7; 2973 -5.7; 3270 -6.7; 3597 -4.5; 3957 -5.9; 4353 -9.3; 4788 -8.9; 5267 -5.2; 5793 -1.0; 6373 -3.1; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -11.2; 10263 -11.7; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -6.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D1001K Silver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1001K Silver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.33 | 6.8 dB  |
| Peaking | 1011 Hz  | 2.68 | -2.9 dB |
| Peaking | 6116 Hz  | 4.5  | 5.3 dB  |
| Peaking | 9390 Hz  | 6.86 | -3.8 dB |
| Peaking | 10171 Hz | 6.62 | -4.7 dB |
| Peaking | 55 Hz    | 1.21 | 1.2 dB  |
| Peaking | 109 Hz   | 0.94 | -1.9 dB |
| Peaking | 470 Hz   | 2.12 | 2.0 dB  |
| Peaking | 2509 Hz  | 4    | 2.4 dB  |
| Peaking | 4565 Hz  | 7.66 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D1001K%20Silver/Denon%20AH-D1001K%20Silver.png)