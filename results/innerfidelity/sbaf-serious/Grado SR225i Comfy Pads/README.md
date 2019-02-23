# Grado SR225i Comfy Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.3; 45 -2.2; 49 -3.0; 54 -3.8; 60 -4.4; 66 -5.1; 72 -5.6; 79 -6.1; 87 -6.6; 96 -7.0; 106 -7.1; 116 -7.2; 128 -7.3; 141 -7.2; 155 -7.2; 170 -7.1; 187 -6.9; 206 -6.8; 227 -6.5; 249 -6.3; 274 -5.9; 302 -6.1; 332 -5.9; 365 -5.7; 402 -5.6; 442 -5.4; 486 -5.3; 535 -5.3; 588 -5.0; 647 -4.8; 712 -5.0; 783 -4.8; 861 -5.0; 947 -5.2; 1042 -5.3; 1146 -5.5; 1261 -5.9; 1387 -6.8; 1526 -8.0; 1678 -8.8; 1846 -10.1; 2031 -14.1; 2234 -14.5; 2457 -11.1; 2703 -8.7; 2973 -6.9; 3270 -5.4; 3597 -6.6; 3957 -5.1; 4353 -3.1; 4788 -3.6; 5267 -4.9; 5793 -2.2; 6373 -2.4; 7010 -5.2; 7711 -6.6; 8482 -7.7; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i Comfy Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i Comfy Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.13 | 6.9 dB  |
| Peaking | 762 Hz  | 1    | 1.9 dB  |
| Peaking | 2143 Hz | 3.45 | -9.2 dB |
| Peaking | 4424 Hz | 3.96 | 3.6 dB  |
| Peaking | 6094 Hz | 5.9  | 4.9 dB  |
| Peaking | 47 Hz   | 2.4  | 1.1 dB  |
| Peaking | 120 Hz  | 1.31 | -1.3 dB |
| Peaking | 3299 Hz | 6.89 | 2.0 dB  |
| Peaking | 3569 Hz | 6.3  | -1.2 dB |
| Peaking | 8837 Hz | 6.03 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20Comfy%20Pads/Grado%20SR225i%20Comfy%20Pads.png)