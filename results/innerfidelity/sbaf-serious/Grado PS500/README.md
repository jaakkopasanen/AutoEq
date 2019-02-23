# Grado PS500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.6; 41 -2.9; 45 -4.0; 49 -5.1; 54 -6.3; 60 -7.5; 66 -8.6; 72 -9.5; 79 -10.2; 87 -11.0; 96 -11.4; 106 -11.5; 116 -11.2; 128 -11.0; 141 -10.6; 155 -10.2; 170 -9.6; 187 -9.0; 206 -9.1; 227 -8.5; 249 -8.0; 274 -7.6; 302 -7.2; 332 -6.8; 365 -6.4; 402 -6.1; 442 -5.8; 486 -5.9; 535 -5.6; 588 -5.2; 647 -5.3; 712 -5.5; 783 -5.3; 861 -5.6; 947 -5.8; 1042 -6.2; 1146 -6.6; 1261 -7.0; 1387 -8.0; 1526 -9.1; 1678 -9.8; 1846 -10.5; 2031 -12.3; 2234 -11.7; 2457 -8.1; 2703 -5.2; 2973 -2.6; 3270 -1.8; 3597 -3.9; 3957 -4.8; 4353 -3.2; 4788 -2.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.5; 9330 -10.2; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado PS500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.82 | 7.1 dB  |
| Peaking | 100 Hz  | 0.89 | -6.1 dB |
| Peaking | 2082 Hz | 2.6  | -7.0 dB |
| Peaking | 3085 Hz | 3    | 5.6 dB  |
| Peaking | 5596 Hz | 2.94 | 6.8 dB  |
| Peaking | 671 Hz  | 1.18 | 1.6 dB  |
| Peaking | 1521 Hz | 5.47 | -1.4 dB |
| Peaking | 6535 Hz | 8.59 | 1.9 dB  |
| Peaking | 9228 Hz | 5.26 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20PS500/Grado%20PS500.png)