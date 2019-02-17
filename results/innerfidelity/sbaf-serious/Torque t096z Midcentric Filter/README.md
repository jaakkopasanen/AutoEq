# Torque t096z Midcentric Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.2; 28 -1.6; 31 -2.0; 34 -2.3; 37 -2.6; 41 -2.9; 45 -3.2; 49 -3.4; 54 -3.8; 60 -4.2; 66 -4.6; 72 -5.0; 79 -5.5; 87 -5.9; 96 -6.4; 106 -6.7; 116 -7.0; 128 -7.4; 141 -7.8; 155 -8.0; 170 -8.2; 187 -8.3; 206 -8.5; 227 -8.3; 249 -8.5; 274 -8.3; 302 -8.2; 332 -8.0; 365 -7.8; 402 -7.5; 442 -7.1; 486 -7.0; 535 -6.7; 588 -6.2; 647 -6.0; 712 -5.9; 783 -5.7; 861 -6.0; 947 -6.3; 1042 -6.7; 1146 -7.0; 1261 -7.3; 1387 -8.0; 1526 -8.4; 1678 -8.8; 1846 -8.4; 2031 -8.0; 2234 -7.5; 2457 -6.2; 2703 -5.7; 2973 -4.6; 3270 -4.1; 3597 -5.7; 3957 -8.3; 4353 -10.8; 4788 -9.5; 5267 -5.6; 5793 -2.4; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.8; 10263 -8.4; 11289 -7.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Midcentric Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Midcentric Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.37 | 5.8 dB   |
| Peaking | 47 Hz    | 1.98 | 2.5 dB   |
| Peaking | 3299 Hz  | 1.75 | 11.0 dB  |
| Peaking | 4411 Hz  | 0.87 | -13.9 dB |
| Peaking | 6010 Hz  | 1.93 | 13.0 dB  |
| Peaking | 232 Hz   | 0.92 | -2.2 dB  |
| Peaking | 776 Hz   | 1.58 | 1.5 dB   |
| Peaking | 1642 Hz  | 3.35 | -1.3 dB  |
| Peaking | 10688 Hz | 4.22 | -2.3 dB  |
| Peaking | 11657 Hz | 1.13 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Midcentric%20Filter/Torque%20t096z%20Midcentric%20Filter.png)