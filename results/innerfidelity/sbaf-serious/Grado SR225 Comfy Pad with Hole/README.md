# Grado SR225 Comfy Pad with Hole
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.3; 37 -2.2; 41 -3.2; 45 -4.1; 49 -4.8; 54 -5.5; 60 -6.2; 66 -6.9; 72 -7.5; 79 -8.0; 87 -8.3; 96 -8.8; 106 -8.8; 116 -8.9; 128 -9.0; 141 -8.9; 155 -8.8; 170 -8.6; 187 -8.5; 206 -8.3; 227 -7.9; 249 -7.7; 274 -7.3; 302 -7.4; 332 -7.3; 365 -7.0; 402 -6.9; 442 -6.7; 486 -6.6; 535 -6.5; 588 -6.2; 647 -6.1; 712 -6.2; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.7; 1261 -7.2; 1387 -8.1; 1526 -9.2; 1678 -9.9; 1846 -11.5; 2031 -15.3; 2234 -15.7; 2457 -12.5; 2703 -9.8; 2973 -8.1; 3270 -6.5; 3597 -7.8; 3957 -6.1; 4353 -4.0; 4788 -4.4; 5267 -5.7; 5793 -3.2; 6373 -2.6; 7010 -5.6; 7711 -8.1; 8482 -10.2; 9330 -10.6; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225 Comfy Pad with Hole GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225 Comfy Pad with Hole ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.82 | 6.7 dB   |
| Peaking | 109 Hz  | 0.71 | -3.1 dB  |
| Peaking | 2159 Hz | 2.88 | -10.2 dB |
| Peaking | 6596 Hz | 1.12 | 4.8 dB   |
| Peaking | 8549 Hz | 2.52 | -7.4 dB  |
| Peaking | 823 Hz  | 1.25 | 0.8 dB   |
| Peaking | 1522 Hz | 7.54 | -0.9 dB  |
| Peaking | 4542 Hz | 5.56 | 3.3 dB   |
| Peaking | 5201 Hz | 2.19 | -3.0 dB  |
| Peaking | 6077 Hz | 5.68 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225%20Comfy%20Pad%20with%20Hole/Grado%20SR225%20Comfy%20Pad%20with%20Hole.png)