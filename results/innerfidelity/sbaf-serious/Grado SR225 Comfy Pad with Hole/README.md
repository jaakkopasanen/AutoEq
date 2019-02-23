# Grado SR225 Comfy Pad with Hole
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.9; 41 -1.9; 45 -2.8; 49 -3.5; 54 -4.2; 60 -4.9; 66 -5.6; 72 -6.2; 79 -6.6; 87 -7.0; 96 -7.4; 106 -7.5; 116 -7.6; 128 -7.7; 141 -7.6; 155 -7.5; 170 -7.3; 187 -7.2; 206 -7.0; 227 -6.6; 249 -6.3; 274 -6.0; 302 -6.1; 332 -6.0; 365 -5.7; 402 -5.6; 442 -5.4; 486 -5.3; 535 -5.2; 588 -4.9; 647 -4.8; 712 -4.9; 783 -4.7; 861 -4.9; 947 -5.1; 1042 -5.3; 1146 -5.4; 1261 -5.9; 1387 -6.7; 1526 -7.9; 1678 -8.6; 1846 -10.2; 2031 -13.9; 2234 -14.4; 2457 -11.2; 2703 -8.5; 2973 -6.8; 3270 -5.2; 3597 -6.5; 3957 -4.8; 4353 -2.7; 4788 -3.1; 5267 -4.4; 5793 -1.9; 6373 -1.3; 7010 -4.3; 7711 -6.8; 8482 -8.9; 9330 -9.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225 Comfy Pad with Hole GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225 Comfy Pad with Hole ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 28 Hz   |  1.31 | 7.1 dB   |
| Peaking | 2151 Hz |  1.95 | -12.2 dB |
| Peaking | 2605 Hz |  0.33 | 4.3 dB   |
| Peaking | 6261 Hz |  4.54 | 4.0 dB   |
| Peaking | 8751 Hz |  2.79 | -4.9 dB  |
| Peaking | 20 Hz   |  3.05 | 2.2 dB   |
| Peaking | 45 Hz   |  2.51 | 1.3 dB   |
| Peaking | 120 Hz  |  1.16 | -1.7 dB  |
| Peaking | 3678 Hz | 11.74 | -1.8 dB  |
| Peaking | 4473 Hz |  9.87 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225%20Comfy%20Pad%20with%20Hole/Grado%20SR225%20Comfy%20Pad%20with%20Hole.png)