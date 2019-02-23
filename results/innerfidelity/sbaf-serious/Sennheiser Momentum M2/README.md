# Sennheiser Momentum M2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.3; 25 -3.8; 28 -4.4; 31 -4.9; 34 -5.2; 37 -5.6; 41 -5.9; 45 -6.2; 49 -6.5; 54 -6.7; 60 -7.0; 66 -7.3; 72 -7.6; 79 -7.8; 87 -8.1; 96 -8.4; 106 -8.4; 116 -8.4; 128 -8.3; 141 -8.0; 155 -8.4; 170 -7.8; 187 -7.8; 206 -7.7; 227 -7.6; 249 -6.9; 274 -7.4; 302 -7.9; 332 -7.7; 365 -7.8; 402 -8.0; 442 -7.9; 486 -8.5; 535 -8.8; 588 -8.6; 647 -8.8; 712 -9.1; 783 -9.1; 861 -9.1; 947 -9.3; 1042 -9.2; 1146 -8.9; 1261 -9.6; 1387 -9.3; 1526 -10.7; 1678 -11.0; 1846 -11.4; 2031 -10.8; 2234 -9.5; 2457 -7.8; 2703 -6.6; 2973 -4.3; 3270 -1.8; 3597 -1.4; 3957 -0.5; 4353 -0.5; 4788 -6.5; 5267 -5.3; 5793 -1.4; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum M2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.88 | 5.0 dB  |
| Peaking | 243 Hz   | 0    | -1.6 dB |
| Peaking | 1890 Hz  | 1.21 | -5.1 dB |
| Peaking | 3568 Hz  | 2.29 | 4.4 dB  |
| Peaking | 4652 Hz  | 0.61 | 4.5 dB  |
| Peaking | 255 Hz   | 5.93 | 1.3 dB  |
| Peaking | 5037 Hz  | 7.81 | -7.3 dB |
| Peaking | 6367 Hz  | 1.74 | 6.2 dB  |
| Peaking | 7528 Hz  | 2.02 | -4.9 dB |
| Peaking | 17512 Hz | 0.5  | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2/Sennheiser%20Momentum%20M2.png)