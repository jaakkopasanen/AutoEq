# Sennheiser HD 414
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -1.2; 79 -2.4; 87 -3.2; 96 -4.1; 106 -4.9; 116 -5.4; 128 -6.1; 141 -6.7; 155 -7.1; 170 -7.5; 187 -7.5; 206 -7.7; 227 -7.7; 249 -7.6; 274 -7.4; 302 -7.2; 332 -7.3; 365 -7.1; 402 -6.9; 442 -6.7; 486 -6.7; 535 -6.6; 588 -6.2; 647 -6.2; 712 -6.3; 783 -6.1; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -7.0; 1387 -7.7; 1526 -8.4; 1678 -8.9; 1846 -8.8; 2031 -8.1; 2234 -8.5; 2457 -10.6; 2703 -12.8; 2973 -10.7; 3270 -8.2; 3597 -7.0; 3957 -5.6; 4353 -3.9; 4788 -1.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 414 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 414 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 0.25 | 7.6 dB  |
| Peaking | 159 Hz  | 0.65 | -6.1 dB |
| Peaking | 1667 Hz | 3.67 | -2.3 dB |
| Peaking | 2739 Hz | 3.51 | -6.7 dB |
| Peaking | 5465 Hz | 2.32 | 7.1 dB  |
| Peaking | 62 Hz   | 1.25 | -0.9 dB |
| Peaking | 67 Hz   | 2.99 | 1.8 dB  |
| Peaking | 760 Hz  | 2.22 | 0.5 dB  |
| Peaking | 6572 Hz | 6.62 | 2.6 dB  |
| Peaking | 7620 Hz | 2.08 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20414/Sennheiser%20HD%20414.png)