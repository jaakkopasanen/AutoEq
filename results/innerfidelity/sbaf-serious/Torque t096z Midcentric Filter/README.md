# Torque t096z Midcentric Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.9; 28 -1.3; 31 -1.6; 34 -2.0; 37 -2.2; 41 -2.5; 45 -2.8; 49 -3.1; 54 -3.4; 60 -3.9; 66 -4.2; 72 -4.7; 79 -5.1; 87 -5.5; 96 -6.1; 106 -6.4; 116 -6.6; 128 -7.0; 141 -7.5; 155 -7.6; 170 -7.8; 187 -8.0; 206 -8.2; 227 -8.0; 249 -8.1; 274 -7.9; 302 -7.8; 332 -7.7; 365 -7.5; 402 -7.2; 442 -6.8; 486 -6.7; 535 -6.4; 588 -5.9; 647 -5.7; 712 -5.6; 783 -5.4; 861 -5.6; 947 -5.9; 1042 -6.3; 1146 -6.7; 1261 -7.0; 1387 -7.6; 1526 -8.1; 1678 -8.5; 1846 -8.1; 2031 -7.7; 2234 -7.2; 2457 -5.8; 2703 -5.3; 2973 -4.3; 3270 -3.8; 3597 -5.4; 3957 -8.0; 4353 -10.5; 4788 -9.2; 5267 -5.3; 5793 -2.1; 6373 -1.1; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.6; 10263 -8.1; 11289 -7.6; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Midcentric Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Midcentric Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 1.27 | 5.9 dB   |
| Peaking | 50 Hz   | 1.92 | 2.5 dB   |
| Peaking | 3334 Hz | 1.81 | 10.5 dB  |
| Peaking | 4379 Hz | 0.92 | -12.9 dB |
| Peaking | 5987 Hz | 2.05 | 12.6 dB  |
| Peaking | 78 Hz   | 1.66 | 0.9 dB   |
| Peaking | 223 Hz  | 0.67 | -1.9 dB  |
| Peaking | 757 Hz  | 1.24 | 1.7 dB   |
| Peaking | 1639 Hz | 2.77 | -1.3 dB  |
| Peaking | 2510 Hz | 7.55 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Midcentric%20Filter/Torque%20t096z%20Midcentric%20Filter.png)