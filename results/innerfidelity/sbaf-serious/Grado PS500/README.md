# Grado PS500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.1; 37 -2.1; 41 -3.3; 45 -4.5; 49 -5.5; 54 -6.7; 60 -8.0; 66 -9.1; 72 -10.0; 79 -10.7; 87 -11.4; 96 -11.8; 106 -11.9; 116 -11.7; 128 -11.5; 141 -11.1; 155 -10.6; 170 -10.0; 187 -9.4; 206 -9.5; 227 -8.9; 249 -8.5; 274 -8.0; 302 -7.6; 332 -7.3; 365 -6.9; 402 -6.5; 442 -6.3; 486 -6.3; 535 -6.1; 588 -5.7; 647 -5.7; 712 -5.9; 783 -5.7; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -7.0; 1261 -7.5; 1387 -8.5; 1526 -9.6; 1678 -10.2; 1846 -11.0; 2031 -12.8; 2234 -12.1; 2457 -8.5; 2703 -5.7; 2973 -3.1; 3270 -2.2; 3597 -4.3; 3957 -5.2; 4353 -3.6; 4788 -2.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.8; 9330 -10.7; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 27 Hz   | 0.81 | 7.3 dB  |
| Peaking | 99 Hz   | 0.78 | -6.5 dB |
| Peaking | 2075 Hz | 2.28 | -7.3 dB |
| Peaking | 3069 Hz | 3.08 | 5.5 dB  |
| Peaking | 5642 Hz | 3.11 | 6.9 dB  |
| Peaking | 671 Hz  | 1.34 | 1.2 dB  |
| Peaking | 1509 Hz | 5.92 | -1.2 dB |
| Peaking | 6575 Hz | 8.03 | 1.9 dB  |
| Peaking | 9241 Hz | 5.22 | -5.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20PS500/Grado%20PS500.png)