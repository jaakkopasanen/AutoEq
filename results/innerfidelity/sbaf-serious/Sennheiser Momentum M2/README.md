# Sennheiser Momentum M2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.9; 25 -1.2; 28 -1.8; 31 -2.3; 34 -2.7; 37 -3.0; 41 -3.3; 45 -3.7; 49 -3.9; 54 -4.2; 60 -4.5; 66 -4.8; 72 -5.1; 79 -5.2; 87 -5.6; 96 -5.8; 106 -5.8; 116 -5.8; 128 -5.7; 141 -5.5; 155 -5.8; 170 -5.3; 187 -5.2; 206 -5.1; 227 -5.1; 249 -4.3; 274 -4.8; 302 -5.3; 332 -5.1; 365 -5.3; 402 -5.4; 442 -5.4; 486 -5.9; 535 -6.3; 588 -6.1; 647 -6.2; 712 -6.5; 783 -6.5; 861 -6.5; 947 -6.7; 1042 -6.6; 1146 -6.4; 1261 -7.1; 1387 -6.8; 1526 -8.1; 1678 -8.4; 1846 -8.8; 2031 -8.2; 2234 -6.9; 2457 -5.2; 2703 -4.0; 2973 -1.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -4.0; 5267 -2.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum M2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.5  | 6.0 dB  |
| Peaking | 270 Hz  | 1.12 | 1.7 dB  |
| Peaking | 1882 Hz | 2.1  | -3.5 dB |
| Peaking | 3557 Hz | 1.63 | 6.8 dB  |
| Peaking | 6064 Hz | 4.7  | 5.1 dB  |
| Peaking | 6693 Hz | 9.76 | 1.6 dB  |
| Peaking | 7932 Hz | 2.32 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2/Sennheiser%20Momentum%20M2.png)