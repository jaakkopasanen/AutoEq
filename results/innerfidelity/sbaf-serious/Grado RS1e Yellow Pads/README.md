# Grado RS1e Yellow Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.5; 41 -2.7; 45 -3.7; 49 -4.6; 54 -5.5; 60 -6.5; 66 -7.5; 72 -8.2; 79 -8.9; 87 -9.6; 96 -10.2; 106 -10.6; 116 -10.8; 128 -11.0; 141 -11.2; 155 -11.1; 170 -11.1; 187 -10.8; 206 -10.7; 227 -10.1; 249 -9.9; 274 -9.6; 302 -10.1; 332 -9.7; 365 -9.3; 402 -9.0; 442 -8.6; 486 -8.5; 535 -8.3; 588 -7.9; 647 -7.8; 712 -7.8; 783 -7.5; 861 -7.7; 947 -7.9; 1042 -8.0; 1146 -8.0; 1261 -8.1; 1387 -8.3; 1526 -7.5; 1678 -9.4; 1846 -15.4; 2031 -14.7; 2234 -11.8; 2457 -8.2; 2703 -5.4; 2973 -3.0; 3270 -1.8; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -1.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1e Yellow Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e Yellow Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 30 Hz   |  0.6  | 8.0 dB   |
| Peaking | 112 Hz  |  0.54 | -3.7 dB  |
| Peaking | 149 Hz  |  0.22 | -2.1 dB  |
| Peaking | 1986 Hz |  3.3  | -11.0 dB |
| Peaking | 4198 Hz |  1.05 | 7.1 dB   |
| Peaking | 1594 Hz | 12.19 | 2.5 dB   |
| Peaking | 3925 Hz |  0.16 | -0.2 dB  |
| Peaking | 6314 Hz |  3.48 | 4.2 dB   |
| Peaking | 7510 Hz |  2.51 | -1.7 dB  |
| Peaking | 7578 Hz |  1.06 | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.9 dB |
| Peaking | 4000 Hz  | 1.41 | 9.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20Yellow%20Pads/Grado%20RS1e%20Yellow%20Pads.png)