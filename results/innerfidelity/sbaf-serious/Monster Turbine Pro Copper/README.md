# Monster Turbine Pro Copper
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.3; 23 -12.4; 25 -12.4; 28 -12.4; 31 -12.3; 34 -12.2; 37 -12.1; 41 -12.0; 45 -12.0; 49 -12.0; 54 -11.9; 60 -11.9; 66 -12.0; 72 -12.0; 79 -12.0; 87 -12.0; 96 -12.1; 106 -12.0; 116 -11.8; 128 -11.8; 141 -11.7; 155 -11.6; 170 -11.4; 187 -11.2; 206 -10.9; 227 -10.6; 249 -10.3; 274 -9.9; 302 -9.5; 332 -9.1; 365 -8.7; 402 -8.3; 442 -7.8; 486 -7.5; 535 -7.0; 588 -6.3; 647 -5.9; 712 -5.7; 783 -5.3; 861 -5.3; 947 -5.5; 1042 -5.8; 1146 -6.2; 1261 -6.1; 1387 -6.7; 1526 -7.4; 1678 -8.0; 1846 -8.2; 2031 -8.5; 2234 -8.3; 2457 -7.3; 2703 -7.9; 2973 -5.9; 3270 -3.9; 3597 -2.6; 3957 -3.6; 4353 -6.4; 4788 -7.4; 5267 -5.3; 5793 -2.2; 6373 -0.5; 7010 -3.1; 7711 -5.4; 8482 -5.6; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Turbine Pro Copper GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine Pro Copper ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.17 | -6.8 dB |
| Peaking | 2148 Hz | 1.91 | -3.1 dB |
| Peaking | 3686 Hz | 3.67 | 4.7 dB  |
| Peaking | 4668 Hz | 3.15 | -3.2 dB |
| Peaking | 6262 Hz | 4.18 | 5.9 dB  |
| Peaking | 20 Hz   | 0.75 | -0.9 dB |
| Peaking | 48 Hz   | 0.74 | 0.9 dB  |
| Peaking | 229 Hz  | 0.58 | -0.7 dB |
| Peaking | 758 Hz  | 1.42 | 1.5 dB  |
| Peaking | 1612 Hz | 5.04 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Turbine%20Pro%20Copper/Monster%20Turbine%20Pro%20Copper.png)