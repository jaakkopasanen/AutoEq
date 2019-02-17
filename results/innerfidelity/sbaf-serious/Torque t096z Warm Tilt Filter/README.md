# Torque t096z Warm Tilt Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.7; 25 -11.0; 28 -11.3; 31 -11.6; 34 -11.7; 37 -11.9; 41 -12.1; 45 -12.2; 49 -12.4; 54 -12.6; 60 -12.8; 66 -13.0; 72 -13.2; 79 -13.5; 87 -13.7; 96 -13.9; 106 -13.9; 116 -13.9; 128 -13.9; 141 -13.8; 155 -13.6; 170 -13.4; 187 -13.1; 206 -12.7; 227 -12.3; 249 -11.8; 274 -11.3; 302 -10.7; 332 -10.1; 365 -9.5; 402 -8.9; 442 -8.1; 486 -7.7; 535 -7.2; 588 -6.3; 647 -5.9; 712 -5.6; 783 -5.3; 861 -5.4; 947 -5.7; 1042 -6.2; 1146 -6.7; 1261 -7.3; 1387 -8.2; 1526 -9.4; 1678 -10.4; 1846 -11.4; 2031 -12.3; 2234 -13.2; 2457 -12.4; 2703 -10.2; 2973 -6.6; 3270 -4.6; 3597 -4.0; 3957 -6.1; 4353 -10.9; 4788 -11.4; 5267 -6.3; 5793 -1.0; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.2; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Warm Tilt Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Warm Tilt Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 55 Hz   | 0.33 | -6.2 dB |
| Peaking | 179 Hz  | 0.77 | -4.4 dB |
| Peaking | 2124 Hz | 2.53 | -7.7 dB |
| Peaking | 4679 Hz | 6.88 | -7.6 dB |
| Peaking | 6120 Hz | 4    | 6.9 dB  |
| Peaking | 787 Hz  | 2.26 | 1.7 dB  |
| Peaking | 1554 Hz | 4.71 | -1.6 dB |
| Peaking | 2590 Hz | 6.26 | -2.6 dB |
| Peaking | 3503 Hz | 2.95 | 4.0 dB  |
| Peaking | 4267 Hz | 5.43 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Warm%20Tilt%20Filter/Torque%20t096z%20Warm%20Tilt%20Filter.png)