# Sennheiser HD 250 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.4; 25 -5.0; 28 -5.6; 31 -6.1; 34 -6.6; 37 -6.9; 41 -7.1; 45 -7.2; 49 -7.4; 54 -7.4; 60 -7.1; 66 -6.7; 72 -6.4; 79 -5.6; 87 -5.3; 96 -6.6; 106 -8.6; 116 -9.2; 128 -8.3; 141 -8.0; 155 -7.3; 170 -6.4; 187 -5.7; 206 -4.6; 227 -4.5; 249 -4.3; 274 -3.8; 302 -3.5; 332 -3.0; 365 -2.6; 402 -2.6; 442 -2.7; 486 -2.8; 535 -2.9; 588 -2.7; 647 -2.9; 712 -3.1; 783 -3.0; 861 -3.4; 947 -3.6; 1042 -3.8; 1146 -4.0; 1261 -3.3; 1387 -4.1; 1526 -4.8; 1678 -4.7; 1846 -4.1; 2031 -4.4; 2234 -4.8; 2457 -4.1; 2703 -3.4; 2973 -2.3; 3270 -1.9; 3597 -1.6; 3957 -1.8; 4353 -3.6; 4788 -4.1; 5267 -3.0; 5793 -0.5; 6373 -2.1; 7010 -4.5; 7711 -4.6; 8482 -6.5; 9330 -7.0; 10263 -4.3; 11289 -4.2; 12418 -4.7; 13660 -4.2; 15026 -4.2; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 250 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 250 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 1.38 | -3.3 dB |
| Peaking | 123 Hz  | 2.34 | -4.8 dB |
| Peaking | 3504 Hz | 3.35 | 2.9 dB  |
| Peaking | 5940 Hz | 7.67 | 4.4 dB  |
| Peaking | 8902 Hz | 4.86 | -3.4 dB |
| Peaking | 132 Hz  | 7.53 | 2.0 dB  |
| Peaking | 144 Hz  | 2.58 | -1.5 dB |
| Peaking | 374 Hz  | 2.66 | 0.9 dB  |
| Peaking | 578 Hz  | 0.77 | 1.3 dB  |
| Peaking | 1761 Hz | 1.72 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20250%20II/Sennheiser%20HD%20250%20II.png)