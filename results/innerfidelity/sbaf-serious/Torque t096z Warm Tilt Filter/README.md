# Torque t096z Warm Tilt Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.8; 25 -9.0; 28 -9.4; 31 -9.6; 34 -9.8; 37 -9.9; 41 -10.1; 45 -10.3; 49 -10.4; 54 -10.6; 60 -10.8; 66 -11.1; 72 -11.3; 79 -11.5; 87 -11.7; 96 -12.0; 106 -12.0; 116 -11.9; 128 -11.9; 141 -11.8; 155 -11.7; 170 -11.5; 187 -11.2; 206 -10.8; 227 -10.3; 249 -9.9; 274 -9.3; 302 -8.8; 332 -8.2; 365 -7.5; 402 -6.9; 442 -6.2; 486 -5.7; 535 -5.2; 588 -4.4; 647 -4.0; 712 -3.7; 783 -3.3; 861 -3.5; 947 -3.8; 1042 -4.2; 1146 -4.7; 1261 -5.3; 1387 -6.3; 1526 -7.4; 1678 -8.4; 1846 -9.5; 2031 -10.4; 2234 -11.3; 2457 -10.4; 2703 -8.3; 2973 -4.7; 3270 -2.6; 3597 -2.1; 3957 -4.2; 4353 -8.9; 4788 -9.4; 5267 -4.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Warm Tilt Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Warm Tilt Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.54 | -4.4 dB |
| Peaking | 161 Hz  | 1.21 | -3.8 dB |
| Peaking | 2241 Hz | 3.25 | -5.6 dB |
| Peaking | 3388 Hz | 5.26 | 5.6 dB  |
| Peaking | 6115 Hz | 5.45 | 6.9 dB  |
| Peaking | 290 Hz  | 1.85 | -1.4 dB |
| Peaking | 803 Hz  | 1.01 | 3.5 dB  |
| Peaking | 1720 Hz | 2.71 | -2.0 dB |
| Peaking | 4606 Hz | 5.62 | -8.1 dB |
| Peaking | 4700 Hz | 2.06 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Warm%20Tilt%20Filter/Torque%20t096z%20Warm%20Tilt%20Filter.png)