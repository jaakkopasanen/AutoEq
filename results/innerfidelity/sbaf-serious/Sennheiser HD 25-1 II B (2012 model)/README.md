# Sennheiser HD 25-1 II B (2012 model)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.8; 25 -5.3; 28 -5.8; 31 -6.3; 34 -6.7; 37 -6.9; 41 -7.2; 45 -7.4; 49 -7.4; 54 -7.5; 60 -7.6; 66 -7.8; 72 -8.2; 79 -8.6; 87 -8.5; 96 -8.3; 106 -8.0; 116 -8.3; 128 -9.6; 141 -10.2; 155 -9.7; 170 -9.3; 187 -9.2; 206 -8.4; 227 -7.5; 249 -6.8; 274 -6.1; 302 -5.9; 332 -5.7; 365 -5.5; 402 -5.4; 442 -5.5; 486 -5.8; 535 -5.9; 588 -5.6; 647 -5.8; 712 -5.9; 783 -5.8; 861 -6.1; 947 -6.3; 1042 -6.5; 1146 -6.6; 1261 -6.8; 1387 -7.5; 1526 -8.0; 1678 -8.5; 1846 -8.7; 2031 -8.7; 2234 -7.8; 2457 -6.0; 2703 -4.5; 2973 -3.3; 3270 -3.8; 3597 -3.6; 3957 -3.1; 4353 -2.0; 4788 -1.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.3; 9330 -10.5; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-1 II B (2012 model) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 II B (2012 model) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 3.16 | 2.1 dB  |
| Peaking | 140 Hz  | 1.5  | -3.5 dB |
| Peaking | 3089 Hz | 5.06 | 2.2 dB  |
| Peaking | 5543 Hz | 1.76 | 6.7 dB  |
| Peaking | 8957 Hz | 4.26 | -5.9 dB |
| Peaking | 116 Hz  | 2.15 | 3.1 dB  |
| Peaking | 117 Hz  | 0.68 | -2.7 dB |
| Peaking | 345 Hz  | 0.64 | 1.8 dB  |
| Peaking | 1984 Hz | 1.69 | -4.4 dB |
| Peaking | 2558 Hz | 1.45 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025-1%20II%20B%20(2012%20model)/Sennheiser%20HD%2025-1%20II%20B%20(2012%20model).png)