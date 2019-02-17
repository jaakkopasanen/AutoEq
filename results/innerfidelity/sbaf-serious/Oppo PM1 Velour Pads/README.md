# Oppo PM1 Velour Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.2; 25 -3.5; 28 -3.9; 31 -4.1; 34 -4.2; 37 -4.2; 41 -4.4; 45 -4.6; 49 -4.3; 54 -4.3; 60 -5.4; 66 -6.3; 72 -6.6; 79 -7.0; 87 -7.5; 96 -7.9; 106 -8.1; 116 -8.4; 128 -8.7; 141 -9.0; 155 -9.1; 170 -9.2; 187 -9.5; 206 -9.4; 227 -9.4; 249 -9.3; 274 -9.6; 302 -9.8; 332 -9.8; 365 -9.3; 402 -7.2; 442 -7.3; 486 -8.3; 535 -8.7; 588 -8.5; 647 -8.7; 712 -9.1; 783 -9.0; 861 -9.5; 947 -8.0; 1042 -6.3; 1146 -6.5; 1261 -6.5; 1387 -6.9; 1526 -7.1; 1678 -7.0; 1846 -6.4; 2031 -5.7; 2234 -5.0; 2457 -4.4; 2703 -4.0; 2973 -3.5; 3270 -3.4; 3597 -3.5; 3957 -3.1; 4353 -3.2; 4788 -2.2; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -8.2; 9330 -9.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM1 Velour Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 Velour Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.24 | 3.5 dB  |
| Peaking | 177 Hz  | 0.45 | -3.6 dB |
| Peaking | 791 Hz  | 2.81 | -2.4 dB |
| Peaking | 6348 Hz | 0.86 | 8.4 dB  |
| Peaking | 8529 Hz | 1.61 | -8.0 dB |
| Peaking | 414 Hz  | 1.92 | -2.4 dB |
| Peaking | 418 Hz  | 4.68 | 4.0 dB  |
| Peaking | 1668 Hz | 2.12 | -2.5 dB |
| Peaking | 1912 Hz | 0.74 | 1.6 dB  |
| Peaking | 4426 Hz | 4.98 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM1%20Velour%20Pads/Oppo%20PM1%20Velour%20Pads.png)