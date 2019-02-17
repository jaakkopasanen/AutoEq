# Sennheiser HD 201
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -1.2; 861 -3.2; 947 -5.3; 1042 -7.1; 1146 -7.7; 1261 -8.0; 1387 -7.7; 1526 -7.5; 1678 -2.8; 1846 -5.2; 2031 -5.3; 2234 -5.2; 2457 -5.1; 2703 -3.8; 2973 -2.3; 3270 -1.8; 3597 -2.4; 3957 -2.2; 4353 -0.5; 4788 -0.5; 5267 -7.7; 5793 -2.5; 6373 -3.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.7; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 201 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 201 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 85 Hz   |  0.05 | 6.1 dB  |
| Peaking | 731 Hz  |  1.65 | 2.8 dB  |
| Peaking | 1142 Hz |  1.62 | -6.7 dB |
| Peaking | 3132 Hz |  4.92 | 2.4 dB  |
| Peaking | 4393 Hz |  2.23 | 4.9 dB  |
| Peaking | 1553 Hz |  5.35 | -3.0 dB |
| Peaking | 1646 Hz |  9.57 | 5.1 dB  |
| Peaking | 5256 Hz | 11.1  | -7.8 dB |
| Peaking | 5741 Hz |  1.64 | 6.5 dB  |
| Peaking | 5923 Hz |  0.75 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 4.6 dB  |
| Peaking | 250 Hz   | 1.41 | 4.1 dB  |
| Peaking | 500 Hz   | 1.41 | 6.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20201/Sennheiser%20HD%20201.png)