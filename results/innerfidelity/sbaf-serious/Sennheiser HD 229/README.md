# Sennheiser HD 229
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.3; 28 -2.2; 31 -3.0; 34 -3.7; 37 -4.3; 41 -5.1; 45 -5.7; 49 -6.3; 54 -6.9; 60 -7.5; 66 -8.1; 72 -8.5; 79 -8.9; 87 -9.5; 96 -9.9; 106 -10.1; 116 -10.1; 128 -9.9; 141 -9.8; 155 -10.3; 170 -9.7; 187 -9.5; 206 -8.8; 227 -8.5; 249 -8.7; 274 -7.9; 302 -6.6; 332 -5.8; 365 -5.4; 402 -5.1; 442 -4.7; 486 -5.1; 535 -5.0; 588 -4.8; 647 -4.8; 712 -5.3; 783 -5.3; 861 -5.5; 947 -5.8; 1042 -6.1; 1146 -6.1; 1261 -5.9; 1387 -5.7; 1526 -5.1; 1678 -7.3; 1846 -7.2; 2031 -6.6; 2234 -5.9; 2457 -5.3; 2703 -5.8; 2973 -5.7; 3270 -5.6; 3597 -5.2; 3957 -5.9; 4353 -7.3; 4788 -7.0; 5267 -4.1; 5793 -2.2; 6373 -1.2; 7010 -3.9; 7711 -6.1; 8482 -8.8; 9330 -9.9; 10263 -6.5; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 229 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 229 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.6  | 6.7 dB  |
| Peaking | 143 Hz  | 0.38 | -4.8 dB |
| Peaking | 421 Hz  | 0.75 | 3.9 dB  |
| Peaking | 6256 Hz | 3.88 | 5.8 dB  |
| Peaking | 8991 Hz | 5.26 | -4.5 dB |
| Peaking | 257 Hz  | 9.68 | -0.9 dB |
| Peaking | 1542 Hz | 6.81 | 2.1 dB  |
| Peaking | 1712 Hz | 4.35 | -2.2 dB |
| Peaking | 3664 Hz | 1.1  | 1.1 dB  |
| Peaking | 4506 Hz | 5.82 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20229/Sennheiser%20HD%20229.png)