# Grado SR225i Small Flat Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.3; 49 -2.4; 54 -3.6; 60 -4.8; 66 -5.7; 72 -6.4; 79 -7.0; 87 -7.4; 96 -7.8; 106 -7.9; 116 -8.1; 128 -8.4; 141 -8.4; 155 -8.5; 170 -8.5; 187 -8.5; 206 -8.4; 227 -8.2; 249 -8.1; 274 -7.7; 302 -7.8; 332 -7.8; 365 -7.5; 402 -7.4; 442 -7.2; 486 -7.2; 535 -7.0; 588 -6.6; 647 -6.5; 712 -6.5; 783 -6.3; 861 -6.4; 947 -6.4; 1042 -6.4; 1146 -6.4; 1261 -6.6; 1387 -7.2; 1526 -7.7; 1678 -7.8; 1846 -8.4; 2031 -11.8; 2234 -11.2; 2457 -7.6; 2703 -4.9; 2973 -3.6; 3270 -2.4; 3597 -3.4; 3957 -1.8; 4353 -0.5; 4788 -0.6; 5267 -1.6; 5793 -0.6; 6373 -2.2; 7010 -6.0; 7711 -7.3; 8482 -7.9; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i Small Flat Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i Small Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.57 | 9.3 dB  |
| Peaking | 81 Hz    | 0.38 | -4.7 dB |
| Peaking | 2107 Hz  | 3.69 | -7.6 dB |
| Peaking | 5417 Hz  | 0.8  | 8.2 dB  |
| Peaking | 8002 Hz  | 1.5  | -6.4 dB |
| Peaking | 1498 Hz  | 7.75 | -1.1 dB |
| Peaking | 3266 Hz  | 4.12 | 1.3 dB  |
| Peaking | 3615 Hz  | 7.97 | -1.9 dB |
| Peaking | 14060 Hz | 2.17 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20Small%20Flat%20Pads/Grado%20SR225i%20Small%20Flat%20Pads.png)