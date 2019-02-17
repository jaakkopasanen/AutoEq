# Sennheiser HD 660 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.3; 49 -1.8; 54 -2.3; 60 -2.8; 66 -3.3; 72 -3.2; 79 -3.2; 87 -4.6; 96 -5.4; 106 -5.9; 116 -6.2; 128 -6.6; 141 -7.1; 155 -7.3; 170 -7.2; 187 -7.5; 206 -7.5; 227 -7.5; 249 -7.4; 274 -7.4; 302 -7.3; 332 -7.1; 365 -7.0; 402 -6.9; 442 -6.7; 486 -6.7; 535 -6.5; 588 -6.1; 647 -6.0; 712 -5.9; 783 -5.6; 861 -5.7; 947 -6.2; 1042 -6.7; 1146 -6.9; 1261 -7.0; 1387 -7.2; 1526 -7.2; 1678 -7.5; 1846 -7.1; 2031 -6.3; 2234 -5.7; 2457 -5.0; 2703 -4.6; 2973 -4.8; 3270 -5.3; 3597 -5.2; 3957 -4.7; 4353 -4.5; 4788 -3.4; 5267 -3.4; 5793 -2.5; 6373 -2.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 660 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 660 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 30 Hz   |  0.28 | 6.5 dB  |
| Peaking | 144 Hz  |  0.54 | -3.0 dB |
| Peaking | 1567 Hz |  1.13 | -5.2 dB |
| Peaking | 1709 Hz |  0.57 | 4.2 dB  |
| Peaking | 5843 Hz |  2.66 | 3.6 dB  |
| Peaking | 2612 Hz |  4.75 | 1.2 dB  |
| Peaking | 2661 Hz |  2.28 | -0.6 dB |
| Peaking | 6724 Hz | 10.95 | 2.2 dB  |
| Peaking | 7988 Hz |  2.24 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20660%20S/Sennheiser%20HD%20660%20S.png)