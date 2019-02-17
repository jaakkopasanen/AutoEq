# Koss ESP950 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.4; 96 -2.7; 106 -3.4; 116 -3.8; 128 -3.8; 141 -3.8; 155 -3.8; 170 -4.1; 187 -4.2; 206 -4.3; 227 -4.2; 249 -4.3; 274 -4.2; 302 -4.4; 332 -4.4; 365 -4.3; 402 -4.4; 442 -4.3; 486 -4.5; 535 -4.7; 588 -4.7; 647 -4.9; 712 -5.1; 783 -5.2; 861 -5.7; 947 -6.1; 1042 -6.4; 1146 -6.7; 1261 -7.4; 1387 -7.8; 1526 -8.0; 1678 -7.4; 1846 -5.5; 2031 -3.4; 2234 -1.9; 2457 -1.0; 2703 -3.4; 2973 -4.8; 3270 -4.4; 3597 -2.5; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -0.9; 5793 -1.1; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss ESP950 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.31 | 6.1 dB  |
| Peaking | 75 Hz   | 2.95 | 1.8 dB  |
| Peaking | 375 Hz  | 0.94 | 2.0 dB  |
| Peaking | 2365 Hz | 5.57 | 5.3 dB  |
| Peaking | 4764 Hz | 1.68 | 6.6 dB  |
| Peaking | 1468 Hz | 2.13 | -4.5 dB |
| Peaking | 1568 Hz | 1.12 | 2.2 dB  |
| Peaking | 4912 Hz | 6.92 | -1.4 dB |
| Peaking | 6493 Hz | 2.54 | 3.0 dB  |
| Peaking | 7876 Hz | 1.86 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20ESP950%20sample%201/Koss%20ESP950%20sample%201.png)