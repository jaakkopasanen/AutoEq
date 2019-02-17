# Grado RS1e Flat Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.8; 66 -2.4; 72 -4.1; 79 -5.6; 87 -7.0; 96 -7.9; 106 -8.2; 116 -8.2; 128 -8.2; 141 -8.0; 155 -7.8; 170 -7.6; 187 -7.2; 206 -7.0; 227 -6.4; 249 -6.4; 274 -6.2; 302 -6.4; 332 -6.1; 365 -5.9; 402 -5.8; 442 -5.5; 486 -5.5; 535 -5.5; 588 -5.2; 647 -5.2; 712 -5.4; 783 -5.4; 861 -5.8; 947 -6.2; 1042 -6.4; 1146 -6.7; 1261 -6.9; 1387 -7.2; 1526 -5.6; 1678 -6.3; 1846 -12.7; 2031 -12.0; 2234 -8.6; 2457 -4.7; 2703 -1.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1e Flat Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.4  | 9.1 dB  |
| Peaking | 104 Hz  | 0.84 | -8.2 dB |
| Peaking | 569 Hz  | 1.82 | 1.1 dB  |
| Peaking | 1976 Hz | 4.23 | -9.7 dB |
| Peaking | 3839 Hz | 0.89 | 7.2 dB  |
| Peaking | 1219 Hz | 3.69 | -1.4 dB |
| Peaking | 2664 Hz | 0.39 | 0.5 dB  |
| Peaking | 3954 Hz | 4.24 | -1.4 dB |
| Peaking | 6254 Hz | 2.75 | 4.6 dB  |
| Peaking | 7487 Hz | 1.45 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 9.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20Flat%20Pads/Grado%20RS1e%20Flat%20Pads.png)