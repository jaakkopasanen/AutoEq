# Fujisan Telos
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.3; 31 -1.9; 34 -2.5; 37 -3.1; 41 -3.7; 45 -4.2; 49 -4.7; 54 -5.3; 60 -5.9; 66 -6.5; 72 -7.1; 79 -7.7; 87 -8.3; 96 -8.9; 106 -9.4; 116 -9.7; 128 -10.2; 141 -10.6; 155 -10.9; 170 -11.0; 187 -11.2; 206 -11.3; 227 -11.2; 249 -11.2; 274 -11.0; 302 -10.7; 332 -10.3; 365 -9.8; 402 -9.2; 442 -8.6; 486 -8.1; 535 -7.5; 588 -6.6; 647 -6.2; 712 -5.8; 783 -5.6; 861 -5.8; 947 -6.3; 1042 -6.7; 1146 -6.9; 1261 -7.4; 1387 -8.2; 1526 -8.9; 1678 -9.7; 1846 -10.0; 2031 -10.3; 2234 -10.3; 2457 -8.7; 2703 -6.5; 2973 -3.5; 3270 -0.7; 3597 -0.5; 3957 -0.7; 4353 -3.2; 4788 -5.9; 5267 -8.4; 5793 -10.0; 6373 -6.3; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fujisan Telos GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fujisan Telos ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.81 | 6.2 dB  |
| Peaking | 188 Hz  | 0.7  | -5.2 dB |
| Peaking | 2242 Hz | 1.54 | -8.9 dB |
| Peaking | 3441 Hz | 1.05 | 9.5 dB  |
| Peaking | 5423 Hz | 3.37 | -6.9 dB |
| Peaking | 356 Hz  | 2.27 | -1.0 dB |
| Peaking | 746 Hz  | 1.85 | 1.8 dB  |
| Peaking | 1539 Hz | 4.25 | -1.1 dB |
| Peaking | 6844 Hz | 8.99 | 3.3 dB  |
| Peaking | 8021 Hz | 1.25 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fujisan%20Telos/Fujisan%20Telos.png)