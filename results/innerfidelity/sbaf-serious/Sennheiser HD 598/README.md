# Sennheiser HD 598
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.3; 34 -2.1; 37 -2.7; 41 -3.5; 45 -4.1; 49 -4.6; 54 -5.2; 60 -5.7; 66 -5.8; 72 -6.3; 79 -7.0; 87 -7.5; 96 -8.6; 106 -9.1; 116 -9.5; 128 -10.0; 141 -10.3; 155 -10.4; 170 -10.3; 187 -10.3; 206 -10.3; 227 -10.1; 249 -10.0; 274 -9.8; 302 -9.7; 332 -9.4; 365 -9.1; 402 -8.9; 442 -8.4; 486 -8.5; 535 -8.3; 588 -6.7; 647 -7.2; 712 -7.1; 783 -6.9; 861 -6.9; 947 -6.8; 1042 -6.6; 1146 -6.3; 1261 -6.1; 1387 -5.8; 1526 -5.3; 1678 -4.4; 1846 -4.1; 2031 -5.1; 2234 -6.0; 2457 -6.3; 2703 -6.6; 2973 -6.0; 3270 -7.2; 3597 -7.4; 3957 -7.4; 4353 -9.8; 4788 -9.9; 5267 -7.8; 5793 -5.9; 6373 -5.2; 7010 -4.9; 7711 -6.2; 8482 -8.4; 9330 -9.6; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.5; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.54 | 6.4 dB  |
| Peaking | 175 Hz   | 0.54 | -4.4 dB |
| Peaking | 1754 Hz  | 2.81 | 2.6 dB  |
| Peaking | 4555 Hz  | 5.29 | -4.1 dB |
| Peaking | 19536 Hz | 1.26 | -1.8 dB |
| Peaking | 208 Hz   | 4.56 | 0.2 dB  |
| Peaking | 548 Hz   | 4.01 | -1.0 dB |
| Peaking | 602 Hz   | 7.81 | 1.8 dB  |
| Peaking | 6786 Hz  | 4.11 | 2.2 dB  |
| Peaking | 9086 Hz  | 6.12 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)