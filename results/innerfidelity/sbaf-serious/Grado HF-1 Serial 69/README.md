# Grado HF-1 Serial 69
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -1.1; 41 -2.3; 45 -3.6; 49 -4.7; 54 -5.8; 60 -7.0; 66 -7.8; 72 -8.2; 79 -8.7; 87 -9.2; 96 -9.6; 106 -9.5; 116 -9.3; 128 -9.2; 141 -9.0; 155 -8.8; 170 -8.5; 187 -8.3; 206 -8.0; 227 -7.6; 249 -7.3; 274 -7.2; 302 -7.0; 332 -6.6; 365 -6.8; 402 -6.7; 442 -6.4; 486 -6.4; 535 -6.4; 588 -6.1; 647 -6.0; 712 -6.1; 783 -6.0; 861 -6.2; 947 -6.5; 1042 -6.7; 1146 -6.9; 1261 -7.5; 1387 -8.6; 1526 -9.8; 1678 -10.5; 1846 -11.2; 2031 -12.2; 2234 -12.1; 2457 -12.4; 2703 -12.0; 2973 -10.0; 3270 -8.1; 3597 -7.2; 3957 -9.2; 4353 -10.2; 4788 -9.5; 5267 -8.2; 5793 -5.9; 6373 -5.9; 7010 -10.2; 7711 -11.4; 8482 -14.8; 9330 -15.9; 10263 -8.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado HF-1 Serial 69 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado HF-1 Serial 69 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.73 | 7.3 dB   |
| Peaking | 89 Hz    | 0.74 | -4.4 dB  |
| Peaking | 1764 Hz  | 2.89 | -2.4 dB  |
| Peaking | 2422 Hz  | 1.82 | -5.4 dB  |
| Peaking | 8859 Hz  | 3.78 | -10.4 dB |
| Peaking | 748 Hz   | 1.12 | 0.9 dB   |
| Peaking | 3486 Hz  | 4.01 | 3.5 dB   |
| Peaking | 5140 Hz  | 1.13 | -4.3 dB  |
| Peaking | 5907 Hz  | 3.73 | 6.0 dB   |
| Peaking | 11079 Hz | 3.9  | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20HF-1%20Serial%2069/Grado%20HF-1%20Serial%2069.png)