# Grado SR225i G Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.9; 54 -2.0; 60 -3.4; 66 -4.4; 72 -5.0; 79 -5.7; 87 -6.1; 96 -6.7; 106 -6.9; 116 -7.0; 128 -7.0; 141 -6.9; 155 -6.8; 170 -6.5; 187 -6.2; 206 -6.0; 227 -5.6; 249 -5.3; 274 -4.9; 302 -4.8; 332 -4.5; 365 -4.4; 402 -4.4; 442 -4.1; 486 -4.1; 535 -4.1; 588 -3.8; 647 -3.7; 712 -3.7; 783 -3.4; 861 -3.7; 947 -3.8; 1042 -3.8; 1146 -4.1; 1261 -4.5; 1387 -5.1; 1526 -5.3; 1678 -5.6; 1846 -5.3; 2031 -5.5; 2234 -5.0; 2457 -5.5; 2703 -5.8; 2973 -6.7; 3270 -6.5; 3597 -8.5; 3957 -8.0; 4353 -6.8; 4788 -8.2; 5267 -11.7; 5793 -13.1; 6373 -14.1; 7010 -12.4; 7711 -11.2; 8482 -12.6; 9330 -13.9; 10263 -10.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i G Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i G Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 1.01 | 7.0 dB  |
| Peaking | 747 Hz   | 0.6  | 3.0 dB  |
| Peaking | 6152 Hz  | 2.59 | -7.3 dB |
| Peaking | 9343 Hz  | 2.77 | -7.8 dB |
| Peaking | 11037 Hz | 2.46 | 2.8 dB  |
| Peaking | 50 Hz    | 4.03 | 1.9 dB  |
| Peaking | 112 Hz   | 1.56 | -1.5 dB |
| Peaking | 2357 Hz  | 3.7  | 0.9 dB  |
| Peaking | 4200 Hz  | 2.36 | -1.9 dB |
| Peaking | 4457 Hz  | 6.59 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -7.3 dB |
| Peaking | 16000 Hz | 1.41 | 1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20G%20Pads/Grado%20SR225i%20G%20Pads.png)