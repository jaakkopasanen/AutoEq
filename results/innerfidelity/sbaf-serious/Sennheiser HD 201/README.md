# Sennheiser HD 201
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.7; 155 -1.3; 170 -1.6; 187 -2.0; 206 -2.1; 227 -2.4; 249 -3.1; 274 -3.4; 302 -3.9; 332 -4.4; 365 -4.9; 402 -5.4; 442 -5.8; 486 -6.2; 535 -6.1; 588 -5.8; 647 -5.7; 712 -6.1; 783 -6.7; 861 -7.2; 947 -6.9; 1042 -6.2; 1146 -6.6; 1261 -6.3; 1387 -6.5; 1526 -6.2; 1678 -5.8; 1846 -6.4; 2031 -6.0; 2234 -5.2; 2457 -3.8; 2703 -3.1; 2973 -2.8; 3270 -2.3; 3597 -3.7; 3957 -3.4; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.1; 9330 -10.3; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 201 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 201 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  0.16 | 6.0 dB  |
| Peaking | 149 Hz  |  0.74 | 3.2 dB  |
| Peaking | 2870 Hz |  3.23 | 2.6 dB  |
| Peaking | 5431 Hz |  1.4  | 6.8 dB  |
| Peaking | 8847 Hz |  3.64 | -6.5 dB |
| Peaking | 267 Hz  |  3.12 | 0.4 dB  |
| Peaking | 471 Hz  |  4.7  | -0.7 dB |
| Peaking | 872 Hz  |  4.74 | -1.2 dB |
| Peaking | 4384 Hz | 12.55 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 5.0 dB  |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20201/Sennheiser%20HD%20201.png)