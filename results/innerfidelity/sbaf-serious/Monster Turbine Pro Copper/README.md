# Monster Turbine Pro Copper
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.4; 25 -11.4; 28 -11.4; 31 -11.4; 34 -11.2; 37 -11.1; 41 -11.0; 45 -11.0; 49 -11.0; 54 -10.9; 60 -10.9; 66 -11.0; 72 -11.0; 79 -11.0; 87 -11.0; 96 -11.1; 106 -11.0; 116 -10.9; 128 -10.8; 141 -10.8; 155 -10.6; 170 -10.4; 187 -10.2; 206 -9.9; 227 -9.6; 249 -9.3; 274 -8.9; 302 -8.5; 332 -8.1; 365 -7.7; 402 -7.3; 442 -6.8; 486 -6.5; 535 -6.0; 588 -5.3; 647 -4.9; 712 -4.7; 783 -4.3; 861 -4.4; 947 -4.5; 1042 -4.8; 1146 -5.2; 1261 -5.1; 1387 -5.7; 1526 -6.4; 1678 -7.0; 1846 -7.2; 2031 -7.5; 2234 -7.3; 2457 -6.3; 2703 -7.0; 2973 -5.0; 3270 -2.9; 3597 -1.6; 3957 -2.6; 4353 -5.4; 4788 -6.4; 5267 -4.3; 5793 -1.2; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Turbine Pro Copper GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine Pro Copper ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.09 | -5.3 dB |
| Peaking | 803 Hz   | 0.72 | 3.4 dB  |
| Peaking | 3127 Hz  | 0.53 | -3.4 dB |
| Peaking | 3529 Hz  | 2.91 | 7.4 dB  |
| Peaking | 6208 Hz  | 3.7  | 7.5 dB  |
| Peaking | 519 Hz   | 3.39 | -0.2 dB |
| Peaking | 11490 Hz | 1.97 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Turbine%20Pro%20Copper/Monster%20Turbine%20Pro%20Copper.png)