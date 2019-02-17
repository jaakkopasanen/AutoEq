# Sennheiser HD 800 S sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.5; 28 -2.1; 31 -2.6; 34 -3.0; 37 -3.3; 41 -3.6; 45 -3.7; 49 -3.9; 54 -4.1; 60 -4.4; 66 -4.4; 72 -4.7; 79 -5.3; 87 -5.9; 96 -6.7; 106 -7.1; 116 -7.4; 128 -7.7; 141 -8.0; 155 -8.1; 170 -8.1; 187 -8.4; 206 -8.4; 227 -8.4; 249 -8.4; 274 -8.2; 302 -8.1; 332 -8.0; 365 -7.8; 402 -7.6; 442 -7.3; 486 -7.2; 535 -7.1; 588 -6.6; 647 -6.4; 712 -6.3; 783 -5.8; 861 -5.6; 947 -5.2; 1042 -4.7; 1146 -4.5; 1261 -3.9; 1387 -3.4; 1526 -2.9; 1678 -3.0; 1846 -3.3; 2031 -2.9; 2234 -3.1; 2457 -2.9; 2703 -2.7; 2973 -3.1; 3270 -3.2; 3597 -3.5; 3957 -4.3; 4353 -4.9; 4788 -4.9; 5267 -6.1; 5793 -6.1; 6373 -9.1; 7010 -8.9; 7711 -7.5; 8482 -6.3; 9330 -5.2; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.1; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.95 | 2.1 dB  |
| Peaking | 18 Hz   | 0.2  | 2.9 dB  |
| Peaking | 202 Hz  | 0.36 | -4.0 dB |
| Peaking | 2094 Hz | 0.69 | 2.5 dB  |
| Peaking | 6773 Hz | 2.97 | -4.9 dB |
| Peaking | 17 Hz   | 2.04 | 1.0 dB  |
| Peaking | 70 Hz   | 5.1  | 0.7 dB  |
| Peaking | 2820 Hz | 6.45 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20800%20S%20sample%201/Sennheiser%20HD%20800%20S%20sample%201.png)