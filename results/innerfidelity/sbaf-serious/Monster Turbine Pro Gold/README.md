# Monster Turbine Pro Gold
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -13.9; 25 -13.9; 28 -13.9; 31 -13.8; 34 -13.8; 37 -13.8; 41 -13.8; 45 -13.7; 49 -13.7; 54 -13.7; 60 -13.7; 66 -13.7; 72 -13.8; 79 -13.8; 87 -13.8; 96 -13.9; 106 -13.6; 116 -13.4; 128 -13.3; 141 -13.0; 155 -12.7; 170 -12.3; 187 -11.9; 206 -11.4; 227 -10.8; 249 -10.3; 274 -9.7; 302 -9.2; 332 -8.6; 365 -8.0; 402 -7.4; 442 -6.7; 486 -6.2; 535 -5.7; 588 -4.9; 647 -4.6; 712 -4.4; 783 -4.0; 861 -4.2; 947 -4.6; 1042 -5.1; 1146 -5.5; 1261 -5.9; 1387 -6.6; 1526 -7.5; 1678 -8.3; 1846 -8.9; 2031 -9.1; 2234 -9.3; 2457 -8.7; 2703 -7.9; 2973 -5.5; 3270 -3.3; 3597 -2.7; 3957 -3.9; 4353 -7.0; 4788 -7.7; 5267 -5.7; 5793 -2.8; 6373 -0.5; 7010 -2.4; 7711 -4.6; 8482 -4.9; 9330 -6.3; 10263 -5.0; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Turbine Pro Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine Pro Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 53 Hz   | 0.22 | -9.6 dB |
| Peaking | 2182 Hz | 1.89 | -5.0 dB |
| Peaking | 3573 Hz | 3.32 | 4.5 dB  |
| Peaking | 4634 Hz | 3.27 | -4.0 dB |
| Peaking | 6355 Hz | 4.8  | 5.5 dB  |
| Peaking | 17 Hz   | 2.48 | -1.0 dB |
| Peaking | 197 Hz  | 1.31 | -1.0 dB |
| Peaking | 729 Hz  | 1.36 | 2.1 dB  |
| Peaking | 1592 Hz | 3.93 | -1.3 dB |
| Peaking | 9360 Hz | 7.01 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.1 dB |
| Peaking | 62 Hz    | 1.41 | -6.4 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Turbine%20Pro%20Gold/Monster%20Turbine%20Pro%20Gold.png)