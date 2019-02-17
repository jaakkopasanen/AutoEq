# Sennheiser HD 25-1 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.1; 66 -1.8; 72 -2.6; 79 -3.2; 87 -3.3; 96 -3.4; 106 -4.9; 116 -5.8; 128 -6.9; 141 -8.0; 155 -8.2; 170 -8.3; 187 -8.6; 206 -8.4; 227 -8.2; 249 -8.0; 274 -7.6; 302 -7.6; 332 -7.5; 365 -7.2; 402 -6.8; 442 -6.7; 486 -6.7; 535 -6.6; 588 -6.3; 647 -6.2; 712 -6.3; 783 -6.1; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -7.1; 1387 -7.7; 1526 -8.4; 1678 -9.2; 1846 -9.4; 2031 -9.4; 2234 -9.0; 2457 -7.6; 2703 -5.7; 2973 -4.0; 3270 -4.0; 3597 -4.3; 3957 -3.8; 4353 -4.1; 4788 -2.7; 5267 -1.3; 5793 -1.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.9; 9330 -8.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-1 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.79 | 7.1 dB  |
| Peaking | 2055 Hz | 1.69 | -4.3 dB |
| Peaking | 3039 Hz | 2.08 | 3.3 dB  |
| Peaking | 5837 Hz | 1.95 | 6.0 dB  |
| Peaking | 8756 Hz | 4.26 | -4.6 dB |
| Peaking | 35 Hz   | 0.23 | 4.7 dB  |
| Peaking | 36 Hz   | 1.05 | -5.6 dB |
| Peaking | 166 Hz  | 0.88 | -4.5 dB |
| Peaking | 762 Hz  | 1.58 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025-1%20II/Sennheiser%20HD%2025-1%20II.png)