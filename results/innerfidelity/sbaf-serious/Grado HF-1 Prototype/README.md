# Grado HF-1 Prototype
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.3; 49 -2.4; 54 -3.7; 60 -4.8; 66 -5.6; 72 -6.6; 79 -7.6; 87 -8.3; 96 -8.7; 106 -8.9; 116 -8.9; 128 -8.8; 141 -8.6; 155 -8.3; 170 -7.9; 187 -7.5; 206 -7.5; 227 -7.2; 249 -7.0; 274 -6.7; 302 -6.1; 332 -6.3; 365 -6.0; 402 -6.0; 442 -6.0; 486 -6.1; 535 -5.9; 588 -5.8; 647 -5.8; 712 -5.9; 783 -5.8; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.5; 1387 -8.5; 1526 -9.7; 1678 -10.4; 1846 -11.0; 2031 -11.8; 2234 -11.6; 2457 -10.3; 2703 -10.0; 2973 -8.3; 3270 -7.2; 3597 -7.8; 3957 -8.0; 4353 -12.9; 4788 -15.4; 5267 -11.5; 5793 -9.6; 6373 -10.5; 7010 -12.9; 7711 -13.8; 8482 -16.4; 9330 -17.6; 10263 -12.4; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado HF-1 Prototype GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado HF-1 Prototype ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.2  | 11.2 dB  |
| Peaking | 107 Hz   | 0.48 | -12.9 dB |
| Peaking | 2008 Hz  | 1.92 | -5.5 dB  |
| Peaking | 4707 Hz  | 5.41 | -8.3 dB  |
| Peaking | 8768 Hz  | 2.5  | -11.5 dB |
| Peaking | 42 Hz    | 4.76 | 0.9 dB   |
| Peaking | 3605 Hz  | 5.93 | 1.3 dB   |
| Peaking | 9883 Hz  | 6.26 | -3.3 dB  |
| Peaking | 11450 Hz | 2.7  | 3.0 dB   |
| Peaking | 18424 Hz | 2.71 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | -9.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20HF-1%20Prototype/Grado%20HF-1%20Prototype.png)