# Koss ESP950
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.2; 96 -2.2; 106 -3.1; 116 -3.7; 128 -3.7; 141 -3.8; 155 -3.8; 170 -4.1; 187 -4.2; 206 -4.3; 227 -4.3; 249 -4.4; 274 -4.3; 302 -4.4; 332 -4.4; 365 -4.4; 402 -4.5; 442 -4.5; 486 -4.8; 535 -4.9; 588 -4.9; 647 -5.1; 712 -5.3; 783 -5.4; 861 -5.9; 947 -6.2; 1042 -6.5; 1146 -6.9; 1261 -7.5; 1387 -8.0; 1526 -8.1; 1678 -7.4; 1846 -5.4; 2031 -3.4; 2234 -1.9; 2457 -1.4; 2703 -3.4; 2973 -4.4; 3270 -4.0; 3597 -2.2; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -1.0; 6373 -2.1; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss ESP950 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.09 | 6.1 dB  |
| Peaking | 1489 Hz | 3.35 | -2.8 dB |
| Peaking | 2298 Hz | 4.1  | 4.3 dB  |
| Peaking | 5026 Hz | 1.14 | 6.6 dB  |
| Peaking | 8642 Hz | 2.22 | -3.0 dB |
| Peaking | 83 Hz   | 1.47 | 2.7 dB  |
| Peaking | 106 Hz  | 1.19 | -2.7 dB |
| Peaking | 452 Hz  | 1.1  | 1.3 dB  |
| Peaking | 3108 Hz | 6.72 | -1.4 dB |
| Peaking | 3902 Hz | 7.89 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.7 dB  |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20ESP950/Koss%20ESP950.png)