# Grado HF-1 Prototype
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.4; 60 -2.4; 66 -3.2; 72 -4.2; 79 -5.2; 87 -5.9; 96 -6.3; 106 -6.5; 116 -6.5; 128 -6.5; 141 -6.3; 155 -5.9; 170 -5.6; 187 -5.1; 206 -5.1; 227 -4.8; 249 -4.6; 274 -4.3; 302 -3.8; 332 -4.0; 365 -3.7; 402 -3.7; 442 -3.7; 486 -3.8; 535 -3.6; 588 -3.4; 647 -3.4; 712 -3.6; 783 -3.5; 861 -3.8; 947 -4.0; 1042 -4.2; 1146 -4.5; 1261 -5.1; 1387 -6.2; 1526 -7.4; 1678 -8.0; 1846 -8.7; 2031 -9.4; 2234 -9.2; 2457 -8.0; 2703 -7.7; 2973 -6.0; 3270 -4.9; 3597 -5.4; 3957 -5.7; 4353 -10.6; 4788 -13.0; 5267 -9.1; 5793 -7.3; 6373 -8.1; 7010 -10.5; 7711 -11.5; 8482 -14.1; 9330 -15.3; 10263 -10.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado HF-1 Prototype GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado HF-1 Prototype ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.88 | 7.0 dB  |
| Peaking | 617 Hz   | 0.56 | 3.3 dB  |
| Peaking | 1968 Hz  | 2.19 | -3.8 dB |
| Peaking | 8824 Hz  | 2.44 | -8.8 dB |
| Peaking | 22050 Hz | 2.45 | -5.7 dB |
| Peaking | 54 Hz    | 3.07 | 1.7 dB  |
| Peaking | 103 Hz   | 2    | -1.6 dB |
| Peaking | 3627 Hz  | 3.21 | 2.8 dB  |
| Peaking | 4627 Hz  | 5.96 | -7.3 dB |
| Peaking | 11331 Hz | 4.7  | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20HF-1%20Prototype/Grado%20HF-1%20Prototype.png)