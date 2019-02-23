# Grado SR325
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.1; 60 -2.1; 66 -2.7; 72 -3.3; 79 -3.8; 87 -4.2; 96 -4.6; 106 -4.6; 116 -4.7; 128 -4.7; 141 -4.7; 155 -4.6; 170 -4.4; 187 -4.3; 206 -4.4; 227 -4.2; 249 -4.1; 274 -4.0; 302 -3.8; 332 -3.5; 365 -3.2; 402 -3.9; 442 -3.8; 486 -3.8; 535 -4.0; 588 -3.7; 647 -3.7; 712 -3.8; 783 -3.7; 861 -3.9; 947 -4.3; 1042 -4.5; 1146 -4.7; 1261 -5.4; 1387 -6.6; 1526 -7.9; 1678 -8.6; 1846 -9.8; 2031 -13.7; 2234 -11.8; 2457 -9.8; 2703 -8.5; 2973 -6.4; 3270 -5.4; 3597 -2.1; 3957 -8.0; 4353 -11.9; 4788 -13.1; 5267 -10.0; 5793 -8.0; 6373 -7.3; 7010 -10.1; 7711 -10.2; 8482 -13.2; 9330 -15.3; 10263 -12.5; 11289 -8.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.6  | 6.5 dB  |
| Peaking | 519 Hz   | 0.43 | 3.0 dB  |
| Peaking | 2062 Hz  | 3.06 | -7.6 dB |
| Peaking | 9082 Hz  | 2.23 | -8.6 dB |
| Peaking | 22050 Hz | 2.23 | -6.1 dB |
| Peaking | 16 Hz    | 1.99 | 1.2 dB  |
| Peaking | 2482 Hz  | 6.83 | -0.7 dB |
| Peaking | 3685 Hz  | 7.54 | 7.5 dB  |
| Peaking | 4566 Hz  | 3.35 | -7.5 dB |
| Peaking | 8345 Hz  | 0.29 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR325/Grado%20SR325.png)