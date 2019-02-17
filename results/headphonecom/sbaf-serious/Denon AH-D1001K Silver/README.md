# Denon AH-D1001K Silver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.3; 49 -1.8; 54 -2.1; 60 -2.5; 66 -3.0; 72 -3.6; 79 -4.2; 87 -4.7; 96 -5.0; 106 -5.3; 116 -5.3; 128 -5.4; 141 -5.1; 155 -5.0; 170 -5.1; 187 -4.7; 206 -4.3; 227 -4.3; 249 -4.3; 274 -4.0; 302 -3.8; 332 -3.4; 365 -3.1; 402 -2.7; 442 -2.6; 486 -2.5; 535 -2.4; 588 -2.7; 647 -3.4; 712 -4.5; 783 -5.7; 861 -6.3; 947 -6.6; 1042 -6.4; 1146 -5.8; 1261 -5.6; 1387 -5.5; 1526 -5.4; 1678 -5.1; 1846 -4.4; 2031 -3.4; 2234 -2.4; 2457 -1.8; 2703 -2.2; 2973 -3.2; 3270 -4.2; 3597 -2.0; 3957 -3.4; 4353 -6.8; 4788 -6.4; 5267 -2.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.7; 10263 -9.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D1001K Silver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1001K Silver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.58 | 6.4 dB  |
| Peaking | 432 Hz  | 1.06 | 4.1 dB  |
| Peaking | 2449 Hz | 2.49 | 4.7 dB  |
| Peaking | 3704 Hz | 8.46 | 4.0 dB  |
| Peaking | 6000 Hz | 4.69 | 6.7 dB  |
| Peaking | 210 Hz  | 4.92 | 0.8 dB  |
| Peaking | 612 Hz  | 4.49 | 1.2 dB  |
| Peaking | 898 Hz  | 2.77 | -1.4 dB |
| Peaking | 1794 Hz | 2.46 | 0.3 dB  |
| Peaking | 9880 Hz | 6.15 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 4.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D1001K%20Silver/Denon%20AH-D1001K%20Silver.png)