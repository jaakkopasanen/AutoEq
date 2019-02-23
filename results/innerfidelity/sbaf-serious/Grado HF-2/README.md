# Grado HF-2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -1.0; 54 -2.0; 60 -3.4; 66 -4.6; 72 -5.5; 79 -6.3; 87 -7.0; 96 -7.4; 106 -7.5; 116 -7.3; 128 -7.2; 141 -7.0; 155 -6.7; 170 -6.5; 187 -6.3; 206 -6.0; 227 -5.5; 249 -5.3; 274 -5.3; 302 -5.1; 332 -4.9; 365 -4.8; 402 -4.6; 442 -4.3; 486 -4.3; 535 -4.3; 588 -4.0; 647 -3.9; 712 -4.0; 783 -3.9; 861 -4.2; 947 -4.4; 1042 -4.7; 1146 -4.9; 1261 -5.6; 1387 -6.7; 1526 -8.2; 1678 -8.9; 1846 -9.9; 2031 -13.0; 2234 -12.3; 2457 -10.5; 2703 -9.5; 2973 -8.0; 3270 -7.0; 3597 -5.9; 3957 -3.5; 4353 -2.4; 4788 -3.3; 5267 -7.5; 5793 -5.1; 6373 -5.5; 7010 -7.2; 7711 -8.1; 8482 -11.8; 9330 -13.1; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado HF-2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado HF-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 32 Hz    |  1.09 | 7.1 dB  |
| Peaking | 722 Hz   |  0.7  | 2.9 dB  |
| Peaking | 2126 Hz  |  2.12 | -7.0 dB |
| Peaking | 4322 Hz  |  3.87 | 5.1 dB  |
| Peaking | 8976 Hz  |  5.11 | -7.7 dB |
| Peaking | 50 Hz    |  3.21 | 2.2 dB  |
| Peaking | 101 Hz   |  1.66 | -2.0 dB |
| Peaking | 5319 Hz  | 11.8  | -2.7 dB |
| Peaking | 5948 Hz  |  5.59 | 1.6 dB  |
| Peaking | 10630 Hz |  8.51 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20HF-2/Grado%20HF-2.png)