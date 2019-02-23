# Grado SR225i TTVJ Flat Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.2; 45 -2.4; 49 -3.5; 54 -4.7; 60 -5.7; 66 -6.6; 72 -7.1; 79 -7.5; 87 -8.0; 96 -8.4; 106 -8.7; 116 -8.7; 128 -8.9; 141 -9.0; 155 -8.9; 170 -8.8; 187 -8.8; 206 -8.8; 227 -8.4; 249 -8.1; 274 -7.8; 302 -7.8; 332 -8.0; 365 -7.8; 402 -7.7; 442 -7.3; 486 -7.3; 535 -7.2; 588 -6.7; 647 -6.6; 712 -6.5; 783 -6.3; 861 -6.6; 947 -6.3; 1042 -6.4; 1146 -6.5; 1261 -6.6; 1387 -7.1; 1526 -7.6; 1678 -7.5; 1846 -7.8; 2031 -11.2; 2234 -10.5; 2457 -6.6; 2703 -4.4; 2973 -3.0; 3270 -2.0; 3597 -3.0; 3957 -1.4; 4353 -0.5; 4788 -0.5; 5267 -1.4; 5793 -0.5; 6373 -1.5; 7010 -5.5; 7711 -7.6; 8482 -8.3; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i TTVJ Flat Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i TTVJ Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.62 | 9.1 dB  |
| Peaking | 82 Hz    | 0.37 | -4.5 dB |
| Peaking | 2104 Hz  | 4.06 | -7.1 dB |
| Peaking | 5368 Hz  | 0.77 | 7.9 dB  |
| Peaking | 8151 Hz  | 1.68 | -6.7 dB |
| Peaking | 1497 Hz  | 6.7  | -1.3 dB |
| Peaking | 2939 Hz  | 5.46 | 1.1 dB  |
| Peaking | 5860 Hz  | 2.44 | -1.5 dB |
| Peaking | 6097 Hz  | 6.06 | 2.8 dB  |
| Peaking | 14043 Hz | 2.07 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20TTVJ%20Flat%20Pads/Grado%20SR225i%20TTVJ%20Flat%20Pads.png)