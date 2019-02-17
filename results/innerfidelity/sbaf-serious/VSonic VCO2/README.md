# VSonic VCO2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.3; 25 -2.3; 28 -2.4; 31 -2.4; 34 -2.5; 37 -2.6; 41 -2.7; 45 -2.8; 49 -3.0; 54 -3.2; 60 -3.5; 66 -3.7; 72 -4.0; 79 -4.4; 87 -4.8; 96 -5.0; 106 -5.3; 116 -5.6; 128 -5.8; 141 -6.2; 155 -6.4; 170 -6.5; 187 -6.5; 206 -6.7; 227 -6.6; 249 -6.7; 274 -6.6; 302 -6.6; 332 -6.5; 365 -6.4; 402 -6.4; 442 -6.0; 486 -6.1; 535 -6.0; 588 -5.6; 647 -5.5; 712 -5.5; 783 -5.5; 861 -5.8; 947 -6.3; 1042 -6.7; 1146 -7.1; 1261 -7.7; 1387 -8.3; 1526 -8.8; 1678 -9.0; 1846 -8.4; 2031 -6.4; 2234 -5.2; 2457 -3.6; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -3.5; 5267 -3.7; 5793 -5.0; 6373 -8.3; 7010 -10.5; 7711 -8.8; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VCO2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VCO2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.74 | 4.1 dB  |
| Peaking | 58 Hz    | 1.25 | 1.9 dB  |
| Peaking | 1774 Hz  | 1.27 | -9.0 dB |
| Peaking | 2815 Hz  | 0.61 | 9.2 dB  |
| Peaking | 6958 Hz  | 2.74 | -6.8 dB |
| Peaking | 239 Hz   | 1.41 | -0.5 dB |
| Peaking | 728 Hz   | 1.64 | 0.8 dB  |
| Peaking | 1113 Hz  | 2.49 | -0.6 dB |
| Peaking | 10907 Hz | 3.95 | -0.4 dB |
| Peaking | 13533 Hz | 1.97 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VCO2/VSonic%20VCO2.png)