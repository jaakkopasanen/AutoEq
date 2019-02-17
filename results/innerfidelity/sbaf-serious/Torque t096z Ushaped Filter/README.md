# Torque t096z Ushaped Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.7; 23 -16.7; 25 -16.7; 28 -16.6; 31 -16.5; 34 -16.4; 37 -16.3; 41 -16.1; 45 -16.0; 49 -15.8; 54 -15.7; 60 -15.5; 66 -15.4; 72 -15.3; 79 -15.2; 87 -15.1; 96 -15.0; 106 -14.7; 116 -14.3; 128 -14.1; 141 -13.8; 155 -13.3; 170 -12.8; 187 -12.3; 206 -11.8; 227 -11.2; 249 -10.7; 274 -10.0; 302 -9.4; 332 -8.7; 365 -8.0; 402 -7.4; 442 -6.7; 486 -6.3; 535 -5.7; 588 -4.9; 647 -4.5; 712 -4.2; 783 -3.8; 861 -4.0; 947 -4.2; 1042 -4.6; 1146 -5.0; 1261 -5.5; 1387 -6.3; 1526 -7.3; 1678 -8.1; 1846 -8.7; 2031 -9.1; 2234 -10.1; 2457 -11.1; 2703 -11.5; 2973 -10.3; 3270 -8.1; 3597 -7.0; 3957 -8.4; 4353 -12.8; 4788 -15.1; 5267 -9.6; 5793 -3.4; 6373 -0.5; 7010 -2.0; 7711 -4.2; 8482 -4.5; 9330 -4.5; 10263 -7.0; 11289 -8.4; 12418 -4.6; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Ushaped Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Ushaped Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.2  | -12.0 dB |
| Peaking | 165 Hz   | 0.73 | -4.2 dB  |
| Peaking | 2461 Hz  | 1.76 | -6.6 dB  |
| Peaking | 4736 Hz  | 4.42 | -11.1 dB |
| Peaking | 6360 Hz  | 4.41 | 6.3 dB   |
| Peaking | 328 Hz   | 1.72 | -0.9 dB  |
| Peaking | 778 Hz   | 1.57 | 1.6 dB   |
| Peaking | 1620 Hz  | 3.43 | -1.6 dB  |
| Peaking | 2560 Hz  | 0.06 | 0.2 dB   |
| Peaking | 10956 Hz | 5.6  | -5.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.8 dB |
| Peaking | 62 Hz    | 1.41 | -7.6 dB  |
| Peaking | 125 Hz   | 1.41 | -7.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Ushaped%20Filter/Torque%20t096z%20Ushaped%20Filter.png)