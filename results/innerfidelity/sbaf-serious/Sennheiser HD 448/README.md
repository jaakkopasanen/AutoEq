# Sennheiser HD 448
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.0; 60 -1.7; 66 -2.1; 72 -2.7; 79 -3.5; 87 -4.7; 96 -4.6; 106 -3.6; 116 -4.0; 128 -5.7; 141 -7.4; 155 -8.1; 170 -8.1; 187 -8.6; 206 -8.3; 227 -8.0; 249 -7.4; 274 -6.8; 302 -6.0; 332 -5.4; 365 -5.5; 402 -5.7; 442 -5.7; 486 -6.0; 535 -6.3; 588 -6.3; 647 -6.6; 712 -7.0; 783 -6.8; 861 -6.7; 947 -6.5; 1042 -6.8; 1146 -7.1; 1261 -8.0; 1387 -8.9; 1526 -9.9; 1678 -10.7; 1846 -10.5; 2031 -9.3; 2234 -7.6; 2457 -4.5; 2703 -5.1; 2973 -4.3; 3270 -4.1; 3597 -3.2; 3957 -1.4; 4353 -0.5; 4788 -0.5; 5267 -3.3; 5793 -1.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 448 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 448 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 25 Hz   |  0.92 | 5.6 dB  |
| Peaking | 53 Hz   |  1.36 | 4.2 dB  |
| Peaking | 1709 Hz |  2.66 | -5.0 dB |
| Peaking | 4308 Hz |  1.8  | 6.0 dB  |
| Peaking | 6253 Hz |  6.09 | 4.3 dB  |
| Peaking | 112 Hz  |  3.88 | 3.0 dB  |
| Peaking | 182 Hz  |  1.2  | -2.8 dB |
| Peaking | 346 Hz  |  1.89 | 1.8 dB  |
| Peaking | 2485 Hz | 10.42 | 2.0 dB  |
| Peaking | 8347 Hz |  3.39 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20448/Sennheiser%20HD%20448.png)