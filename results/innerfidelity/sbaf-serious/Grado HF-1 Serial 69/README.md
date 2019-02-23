# Grado HF-1 Serial 69
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.4; 49 -2.5; 54 -3.7; 60 -4.8; 66 -5.6; 72 -6.1; 79 -6.5; 87 -7.0; 96 -7.4; 106 -7.4; 116 -7.2; 128 -7.1; 141 -6.9; 155 -6.6; 170 -6.4; 187 -6.2; 206 -5.9; 227 -5.5; 249 -5.2; 274 -5.1; 302 -4.8; 332 -4.4; 365 -4.6; 402 -4.5; 442 -4.3; 486 -4.3; 535 -4.3; 588 -4.0; 647 -3.9; 712 -4.0; 783 -3.9; 861 -4.1; 947 -4.4; 1042 -4.5; 1146 -4.8; 1261 -5.4; 1387 -6.5; 1526 -7.7; 1678 -8.4; 1846 -9.1; 2031 -10.1; 2234 -9.9; 2457 -10.3; 2703 -9.9; 2973 -7.9; 3270 -6.0; 3597 -5.1; 3957 -7.1; 4353 -8.0; 4788 -7.4; 5267 -6.0; 5793 -3.8; 6373 -3.7; 7010 -8.1; 7711 -9.3; 8482 -12.6; 9330 -13.8; 10263 -7.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado HF-1 Serial 69 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado HF-1 Serial 69 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 1.21 | 7.1 dB  |
| Peaking | 711 Hz   | 0.64 | 2.9 dB  |
| Peaking | 2123 Hz  | 1.81 | -4.7 dB |
| Peaking | 6107 Hz  | 6.44 | 4.4 dB  |
| Peaking | 8924 Hz  | 4.2  | -8.3 dB |
| Peaking | 102 Hz   | 2.04 | -1.7 dB |
| Peaking | 2688 Hz  | 6.74 | -1.6 dB |
| Peaking | 3579 Hz  | 3.92 | 3.0 dB  |
| Peaking | 4251 Hz  | 4.68 | -2.5 dB |
| Peaking | 10708 Hz | 7.49 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20HF-1%20Serial%2069/Grado%20HF-1%20Serial%2069.png)