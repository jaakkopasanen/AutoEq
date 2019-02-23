# Sennheiser MX 560
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.8; 141 -1.2; 155 -1.3; 170 -1.5; 187 -1.8; 206 -2.1; 227 -2.0; 249 -2.0; 274 -2.2; 302 -2.4; 332 -2.6; 365 -3.0; 402 -3.3; 442 -3.1; 486 -2.2; 535 -2.6; 588 -3.0; 647 -3.4; 712 -3.7; 783 -4.0; 861 -4.3; 947 -4.8; 1042 -5.2; 1146 -5.5; 1261 -6.1; 1387 -7.2; 1526 -8.7; 1678 -10.2; 1846 -12.1; 2031 -14.4; 2234 -16.4; 2457 -17.6; 2703 -17.0; 2973 -14.4; 3270 -10.5; 3597 -8.4; 3957 -8.2; 4353 -9.8; 4788 -11.0; 5267 -11.3; 5793 -11.5; 6373 -10.5; 7010 -9.0; 7711 -7.9; 8482 -9.9; 9330 -11.5; 10263 -9.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.3; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MX 560 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MX 560 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 108 Hz   | 0.38 | 4.9 dB   |
| Peaking | 640 Hz   | 0.68 | 2.7 dB   |
| Peaking | 2388 Hz  | 2.02 | -11.7 dB |
| Peaking | 6629 Hz  | 0.95 | -3.4 dB  |
| Peaking | 17 Hz    | 0.55 | 3.8 dB   |
| Peaking | 32 Hz    | 0.43 | 1.3 dB   |
| Peaking | 3737 Hz  | 3.77 | 5.4 dB   |
| Peaking | 3849 Hz  | 1.5  | -2.7 dB  |
| Peaking | 11958 Hz | 4.9  | 1.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 4.6 dB  |
| Peaking | 250 Hz   | 1.41 | 3.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.2 dB |
| Peaking | 4000 Hz  | 1.41 | -2.4 dB |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20MX%20560/Sennheiser%20MX%20560.png)