# Sennheiser HD 560 Ovation II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -1.4; 79 -2.2; 87 -3.0; 96 -3.7; 106 -4.3; 116 -4.7; 128 -5.2; 141 -5.6; 155 -6.0; 170 -6.1; 187 -6.2; 206 -6.3; 227 -6.3; 249 -6.2; 274 -6.2; 302 -6.1; 332 -6.2; 365 -5.9; 402 -5.9; 442 -5.7; 486 -5.7; 535 -5.7; 588 -5.3; 647 -5.4; 712 -5.5; 783 -5.3; 861 -5.6; 947 -5.7; 1042 -5.9; 1146 -5.8; 1261 -6.3; 1387 -7.0; 1526 -7.7; 1678 -8.2; 1846 -8.3; 2031 -8.7; 2234 -9.3; 2457 -9.6; 2703 -10.1; 2973 -9.6; 3270 -8.8; 3597 -7.7; 3957 -7.7; 4353 -8.3; 4788 -8.1; 5267 -6.4; 5793 -0.8; 6373 -1.0; 7010 -4.8; 7711 -8.9; 8482 -10.2; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -12.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 560 Ovation II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 560 Ovation II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.54 | 6.8 dB  |
| Peaking | 2585 Hz | 1.81 | -3.7 dB |
| Peaking | 5000 Hz | 2.88 | -5.0 dB |
| Peaking | 5975 Hz | 2.56 | 9.3 dB  |
| Peaking | 8131 Hz | 3.54 | -5.6 dB |
| Peaking | 41 Hz   | 2.52 | -0.9 dB |
| Peaking | 68 Hz   | 2.48 | 1.3 dB  |
| Peaking | 165 Hz  | 1.04 | -0.9 dB |
| Peaking | 803 Hz  | 0.73 | 1.3 dB  |
| Peaking | 1645 Hz | 2.89 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20560%20Ovation%20II/Sennheiser%20HD%20560%20Ovation%20II.png)