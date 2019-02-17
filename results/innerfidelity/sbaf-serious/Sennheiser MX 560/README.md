# Sennheiser MX 560
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.6; 96 -1.5; 106 -2.1; 116 -2.6; 128 -3.0; 141 -3.3; 155 -3.5; 170 -3.8; 187 -3.8; 206 -4.0; 227 -4.0; 249 -4.3; 274 -4.2; 302 -4.2; 332 -4.0; 365 -5.2; 402 -4.9; 442 -4.8; 486 -4.4; 535 -4.5; 588 -4.5; 647 -4.9; 712 -5.3; 783 -5.3; 861 -5.7; 947 -6.2; 1042 -6.7; 1146 -7.1; 1261 -7.9; 1387 -9.2; 1526 -10.9; 1678 -12.7; 1846 -14.8; 2031 -16.6; 2234 -18.2; 2457 -18.6; 2703 -18.8; 2973 -17.1; 3270 -14.6; 3597 -12.9; 3957 -12.8; 4353 -14.7; 4788 -15.9; 5267 -16.6; 5793 -17.1; 6373 -15.4; 7010 -13.8; 7711 -14.1; 8482 -13.5; 9330 -9.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.5; 15026 -10.1; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MX 560 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MX 560 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 40 Hz    |  0.3  | 6.4 dB   |
| Peaking | 732 Hz   |  0.55 | 2.2 dB   |
| Peaking | 2356 Hz  |  1.34 | -12.4 dB |
| Peaking | 5937 Hz  |  1.38 | -9.2 dB  |
| Peaking | 14635 Hz |  5.72 | -4.0 dB  |
| Peaking | 2860 Hz  | 10.23 | -1.2 dB  |
| Peaking | 3670 Hz  |  5.9  | 2.1 dB   |
| Peaking | 8433 Hz  |  3.62 | -7.1 dB  |
| Peaking | 8576 Hz  |  0.49 | -2.6 dB  |
| Peaking | 9106 Hz  |  1.07 | 6.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB   |
| Peaking | 62 Hz    | 1.41 | 5.2 dB   |
| Peaking | 125 Hz   | 1.41 | 2.5 dB   |
| Peaking | 250 Hz   | 1.41 | 1.5 dB   |
| Peaking | 500 Hz   | 1.41 | 1.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.0 dB |
| Peaking | 4000 Hz  | 1.41 | -7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20MX%20560/Sennheiser%20MX%20560.png)