# Sennheiser HD 219
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.6; 25 -3.2; 28 -4.1; 31 -4.8; 34 -5.5; 37 -6.2; 41 -6.9; 45 -7.5; 49 -8.0; 54 -8.5; 60 -9.1; 66 -9.6; 72 -10.0; 79 -10.2; 87 -10.5; 96 -10.8; 106 -10.9; 116 -10.9; 128 -10.5; 141 -10.1; 155 -9.8; 170 -9.7; 187 -9.5; 206 -8.6; 227 -7.9; 249 -7.8; 274 -7.2; 302 -5.9; 332 -4.8; 365 -4.1; 402 -3.9; 442 -3.6; 486 -3.9; 535 -4.2; 588 -4.3; 647 -4.5; 712 -4.2; 783 -4.1; 861 -4.9; 947 -5.5; 1042 -5.9; 1146 -5.9; 1261 -5.7; 1387 -5.5; 1526 -5.0; 1678 -6.3; 1846 -7.0; 2031 -6.5; 2234 -6.0; 2457 -5.3; 2703 -5.3; 2973 -5.2; 3270 -5.3; 3597 -5.3; 3957 -5.7; 4353 -7.4; 4788 -6.5; 5267 -3.0; 5793 -0.8; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -7.5; 9330 -6.2; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 219 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 219 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.96 | 5.0 dB  |
| Peaking | 86 Hz   | 0.65 | -2.6 dB |
| Peaking | 214 Hz  | 0.36 | -4.2 dB |
| Peaking | 421 Hz  | 0.79 | 5.7 dB  |
| Peaking | 6116 Hz | 4.79 | 6.4 dB  |
| Peaking | 775 Hz  | 8.8  | 1.0 dB  |
| Peaking | 1878 Hz | 6.22 | -1.5 dB |
| Peaking | 4441 Hz | 4.74 | -4.1 dB |
| Peaking | 4508 Hz | 1.28 | 1.8 dB  |
| Peaking | 8596 Hz | 5.56 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20219/Sennheiser%20HD%20219.png)