# Sennheiser Urbanite XL
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -5.1; 25 -5.7; 28 -6.3; 31 -6.8; 34 -7.3; 37 -7.7; 41 -8.2; 45 -8.6; 49 -8.9; 54 -9.3; 60 -9.7; 66 -10.0; 72 -10.3; 79 -10.7; 87 -11.2; 96 -11.6; 106 -11.6; 116 -11.3; 128 -11.2; 141 -11.7; 155 -12.2; 170 -11.0; 187 -11.3; 206 -11.1; 227 -10.3; 249 -9.9; 274 -10.0; 302 -10.5; 332 -10.6; 365 -10.1; 402 -9.1; 442 -8.3; 486 -8.2; 535 -7.4; 588 -6.5; 647 -6.3; 712 -6.3; 783 -5.8; 861 -5.7; 947 -5.3; 1042 -4.9; 1146 -5.2; 1261 -5.5; 1387 -6.0; 1526 -6.6; 1678 -7.0; 1846 -7.3; 2031 -7.3; 2234 -6.2; 2457 -4.7; 2703 -4.1; 2973 -2.7; 3270 -2.5; 3597 -1.4; 3957 -0.5; 4353 -0.5; 4788 -4.1; 5267 -5.3; 5793 -1.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Urbanite XL GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Urbanite XL ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 88 Hz   | 0.91 | -4.0 dB |
| Peaking | 173 Hz  | 1.28 | -3.5 dB |
| Peaking | 336 Hz  | 2.59 | -3.1 dB |
| Peaking | 3811 Hz | 2.2  | 6.1 dB  |
| Peaking | 6209 Hz | 5.77 | 5.5 dB  |
| Peaking | 22 Hz   | 2.41 | 2.5 dB  |
| Peaking | 1049 Hz | 1.36 | 2.0 dB  |
| Peaking | 1990 Hz | 1.85 | -2.2 dB |
| Peaking | 2135 Hz | 0.13 | -0.3 dB |
| Peaking | 2599 Hz | 2.46 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Urbanite%20XL/Sennheiser%20Urbanite%20XL.png)