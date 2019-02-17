# Sennheiser Urbanite XL
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.6; 25 -7.1; 28 -7.8; 31 -8.3; 34 -8.7; 37 -9.2; 41 -9.6; 45 -10.0; 49 -10.4; 54 -10.7; 60 -11.1; 66 -11.5; 72 -11.8; 79 -12.2; 87 -12.7; 96 -13.0; 106 -13.1; 116 -12.8; 128 -12.7; 141 -13.2; 155 -13.7; 170 -12.5; 187 -12.8; 206 -12.5; 227 -11.8; 249 -11.4; 274 -11.5; 302 -11.9; 332 -12.0; 365 -11.6; 402 -10.5; 442 -9.8; 486 -9.7; 535 -8.9; 588 -8.0; 647 -7.7; 712 -7.8; 783 -7.3; 861 -7.1; 947 -6.8; 1042 -6.4; 1146 -6.7; 1261 -7.0; 1387 -7.5; 1526 -8.0; 1678 -8.5; 1846 -8.8; 2031 -8.7; 2234 -7.7; 2457 -6.2; 2703 -5.6; 2973 -4.2; 3270 -3.9; 3597 -2.9; 3957 -1.1; 4353 -0.5; 4788 -5.5; 5267 -6.8; 5793 -2.5; 6373 -1.6; 7010 -4.1; 7711 -6.3; 8482 -6.6; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.6; 16529 -6.6; 18182 -6.6; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Urbanite XL GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Urbanite XL ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 74 Hz    |  0.68 | -2.0 dB |
| Peaking | 155 Hz   |  0.45 | -5.4 dB |
| Peaking | 349 Hz   |  2.91 | -1.9 dB |
| Peaking | 4073 Hz  |  2.6  | 5.8 dB  |
| Peaking | 21465 Hz |  2.52 | 1.9 dB  |
| Peaking | 21 Hz    |  2.48 | 1.8 dB  |
| Peaking | 1872 Hz  |  1.73 | -5.1 dB |
| Peaking | 1907 Hz  |  0.81 | 2.5 dB  |
| Peaking | 5052 Hz  | 10.35 | -5.6 dB |
| Peaking | 6240 Hz  |  5.06 | 4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Urbanite%20XL/Sennheiser%20Urbanite%20XL.png)