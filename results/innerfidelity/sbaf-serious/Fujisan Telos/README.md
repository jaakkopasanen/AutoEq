# Fujisan Telos
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.0; 34 -1.6; 37 -2.1; 41 -2.7; 45 -3.3; 49 -3.8; 54 -4.3; 60 -5.0; 66 -5.6; 72 -6.1; 79 -6.7; 87 -7.4; 96 -7.9; 106 -8.4; 116 -8.7; 128 -9.3; 141 -9.7; 155 -9.9; 170 -10.1; 187 -10.3; 206 -10.3; 227 -10.3; 249 -10.2; 274 -10.0; 302 -9.7; 332 -9.3; 365 -8.8; 402 -8.3; 442 -7.6; 486 -7.2; 535 -6.5; 588 -5.7; 647 -5.2; 712 -4.9; 783 -4.6; 861 -4.8; 947 -5.3; 1042 -5.8; 1146 -6.0; 1261 -6.5; 1387 -7.3; 1526 -8.0; 1678 -8.7; 1846 -9.1; 2031 -9.4; 2234 -9.4; 2457 -7.8; 2703 -5.6; 2973 -2.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.2; 4788 -5.0; 5267 -7.5; 5793 -9.0; 6373 -5.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fujisan Telos GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fujisan Telos ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.51 | 6.4 dB  |
| Peaking | 209 Hz  | 0.45 | -4.5 dB |
| Peaking | 734 Hz  | 0.97 | 3.5 dB  |
| Peaking | 2100 Hz | 1.39 | -4.6 dB |
| Peaking | 3449 Hz | 2.25 | 8.3 dB  |
| Peaking | 3583 Hz | 8.81 | -1.9 dB |
| Peaking | 4124 Hz | 3.43 | 2.2 dB  |
| Peaking | 5710 Hz | 3.79 | -4.4 dB |
| Peaking | 6730 Hz | 5.86 | 4.4 dB  |
| Peaking | 7745 Hz | 2.81 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fujisan%20Telos/Fujisan%20Telos.png)