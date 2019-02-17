# Grado RS1e Bowl Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.9; 72 -3.4; 79 -4.9; 87 -6.4; 96 -7.7; 106 -8.5; 116 -8.8; 128 -9.2; 141 -9.3; 155 -9.1; 170 -8.8; 187 -8.4; 206 -7.9; 227 -7.4; 249 -6.9; 274 -6.8; 302 -7.5; 332 -7.0; 365 -6.6; 402 -6.4; 442 -6.0; 486 -6.0; 535 -5.9; 588 -5.6; 647 -5.6; 712 -5.8; 783 -5.7; 861 -6.0; 947 -6.3; 1042 -6.7; 1146 -7.1; 1261 -7.6; 1387 -8.6; 1526 -9.3; 1678 -11.6; 1846 -17.2; 2031 -17.6; 2234 -14.9; 2457 -10.6; 2703 -7.2; 2973 -4.6; 3270 -3.4; 3597 -2.7; 3957 -0.7; 4353 -0.5; 4788 -3.4; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1e Bowl Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e Bowl Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 77 Hz   | 0.25 | 13.9 dB  |
| Peaking | 123 Hz  | 0.53 | -15.7 dB |
| Peaking | 2003 Hz | 2.98 | -13.3 dB |
| Peaking | 3911 Hz | 1.68 | 6.1 dB   |
| Peaking | 5961 Hz | 3.97 | 5.0 dB   |
| Peaking | 61 Hz   | 4.79 | 1.4 dB   |
| Peaking | 89 Hz   | 4.61 | -0.9 dB  |
| Peaking | 319 Hz  | 4.35 | -1.0 dB  |
| Peaking | 742 Hz  | 1.8  | 0.7 dB   |
| Peaking | 8284 Hz | 4.12 | -1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB   |
| Peaking | 62 Hz    | 1.41 | 4.6 dB   |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.4 dB |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20Bowl%20Pads/Grado%20RS1e%20Bowl%20Pads.png)