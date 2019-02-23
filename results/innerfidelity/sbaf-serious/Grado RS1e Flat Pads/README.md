# Grado RS1e Flat Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.0; 60 -3.1; 66 -4.9; 72 -6.6; 79 -8.2; 87 -9.5; 96 -10.5; 106 -10.8; 116 -10.8; 128 -10.8; 141 -10.6; 155 -10.3; 170 -10.1; 187 -9.8; 206 -9.5; 227 -9.0; 249 -8.9; 274 -8.8; 302 -9.0; 332 -8.6; 365 -8.4; 402 -8.3; 442 -8.0; 486 -8.1; 535 -8.0; 588 -7.8; 647 -7.8; 712 -8.0; 783 -7.9; 861 -8.4; 947 -8.7; 1042 -9.0; 1146 -9.2; 1261 -9.5; 1387 -9.7; 1526 -8.2; 1678 -8.9; 1846 -15.2; 2031 -14.5; 2234 -11.1; 2457 -7.2; 2703 -4.3; 2973 -2.0; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1e Flat Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 57 Hz   |  0.25 | 25.4 dB  |
| Peaking | 91 Hz   |  0.32 | -25.9 dB |
| Peaking | 1980 Hz |  3.18 | -10.3 dB |
| Peaking | 3512 Hz |  1.48 | 7.0 dB   |
| Peaking | 5775 Hz |  3.12 | 4.8 dB   |
| Peaking | 589 Hz  |  1.42 | 0.6 dB   |
| Peaking | 1234 Hz |  1.78 | -1.7 dB  |
| Peaking | 1609 Hz | 10.59 | 3.9 dB   |
| Peaking | 6574 Hz |  7.79 | 1.9 dB   |
| Peaking | 7901 Hz |  2.48 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB |
| Peaking | 4000 Hz  | 1.41 | 9.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20Flat%20Pads/Grado%20RS1e%20Flat%20Pads.png)