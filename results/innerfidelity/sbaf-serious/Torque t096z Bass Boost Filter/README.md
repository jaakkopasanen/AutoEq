# Torque t096z Bass Boost Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.1; 23 -17.1; 25 -17.1; 28 -17.0; 31 -16.9; 34 -16.8; 37 -16.7; 41 -16.5; 45 -16.3; 49 -16.2; 54 -16.0; 60 -15.9; 66 -15.7; 72 -15.6; 79 -15.5; 87 -15.4; 96 -15.3; 106 -15.0; 116 -14.6; 128 -14.3; 141 -14.0; 155 -13.6; 170 -13.2; 187 -12.7; 206 -12.2; 227 -11.6; 249 -11.0; 274 -10.3; 302 -9.7; 332 -9.1; 365 -8.4; 402 -7.8; 442 -7.1; 486 -6.7; 535 -6.1; 588 -5.4; 647 -5.1; 712 -5.0; 783 -4.6; 861 -4.9; 947 -5.3; 1042 -5.8; 1146 -6.4; 1261 -7.2; 1387 -8.4; 1526 -9.8; 1678 -11.3; 1846 -12.6; 2031 -13.1; 2234 -12.0; 2457 -8.7; 2703 -5.7; 2973 -2.4; 3270 -0.9; 3597 -1.2; 3957 -4.2; 4353 -7.3; 4788 -4.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Bass Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.28 | -10.4 dB |
| Peaking | 147 Hz   | 0.88 | -4.0 dB  |
| Peaking | 1998 Hz  | 2.73 | -7.9 dB  |
| Peaking | 3251 Hz  | 3.67 | 7.0 dB   |
| Peaking | 5816 Hz  | 3.47 | 6.8 dB   |
| Peaking | 281 Hz   | 1.82 | -1.1 dB  |
| Peaking | 760 Hz   | 1.19 | 2.6 dB   |
| Peaking | 1382 Hz  | 1.96 | -0.3 dB  |
| Peaking | 1551 Hz  | 4.11 | -1.5 dB  |
| Peaking | 20704 Hz | 1.73 | -0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.0 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB  |
| Peaking | 125 Hz   | 1.41 | -6.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -7.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Bass%20Boost%20Filter/Torque%20t096z%20Bass%20Boost%20Filter.png)