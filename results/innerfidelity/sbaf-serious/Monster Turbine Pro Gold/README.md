# Monster Turbine Pro Gold
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.7; 23 -12.7; 25 -12.7; 28 -12.6; 31 -12.6; 34 -12.6; 37 -12.6; 41 -12.5; 45 -12.5; 49 -12.5; 54 -12.5; 60 -12.5; 66 -12.5; 72 -12.5; 79 -12.6; 87 -12.6; 96 -12.6; 106 -12.4; 116 -12.2; 128 -12.1; 141 -11.8; 155 -11.5; 170 -11.1; 187 -10.7; 206 -10.2; 227 -9.6; 249 -9.1; 274 -8.5; 302 -7.9; 332 -7.4; 365 -6.7; 402 -6.2; 442 -5.4; 486 -5.0; 535 -4.5; 588 -3.7; 647 -3.4; 712 -3.1; 783 -2.8; 861 -3.0; 947 -3.4; 1042 -3.8; 1146 -4.2; 1261 -4.6; 1387 -5.4; 1526 -6.3; 1678 -7.1; 1846 -7.6; 2031 -7.9; 2234 -8.1; 2457 -7.5; 2703 -6.7; 2973 -4.3; 3270 -2.0; 3597 -1.4; 3957 -2.7; 4353 -5.8; 4788 -6.5; 5267 -4.5; 5793 -1.6; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Turbine Pro Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine Pro Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 54 Hz    | 0.14 | -6.9 dB |
| Peaking | 807 Hz   | 0.52 | 5.9 dB  |
| Peaking | 2584 Hz  | 0.55 | -5.9 dB |
| Peaking | 3463 Hz  | 2.53 | 9.0 dB  |
| Peaking | 6203 Hz  | 3.78 | 7.5 dB  |
| Peaking | 11231 Hz | 1.96 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Turbine%20Pro%20Gold/Monster%20Turbine%20Pro%20Gold.png)