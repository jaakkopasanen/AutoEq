# Torque t096z Bass Boost Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.9; 23 -17.9; 25 -17.9; 28 -17.8; 31 -17.7; 34 -17.6; 37 -17.5; 41 -17.3; 45 -17.2; 49 -17.0; 54 -16.8; 60 -16.7; 66 -16.6; 72 -16.4; 79 -16.4; 87 -16.2; 96 -16.1; 106 -15.8; 116 -15.4; 128 -15.2; 141 -14.8; 155 -14.5; 170 -14.0; 187 -13.5; 206 -13.0; 227 -12.4; 249 -11.8; 274 -11.2; 302 -10.5; 332 -9.9; 365 -9.3; 402 -8.7; 442 -7.9; 486 -7.5; 535 -7.0; 588 -6.3; 647 -5.9; 712 -5.8; 783 -5.5; 861 -5.7; 947 -6.1; 1042 -6.7; 1146 -7.3; 1261 -8.1; 1387 -9.2; 1526 -10.7; 1678 -12.1; 1846 -13.5; 2031 -14.0; 2234 -12.9; 2457 -9.6; 2703 -6.5; 2973 -3.2; 3270 -1.8; 3597 -2.0; 3957 -5.1; 4353 -8.2; 4788 -4.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Bass Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.23 | -11.2 dB |
| Peaking | 157 Hz   | 0.8  | -4.0 dB  |
| Peaking | 1986 Hz  | 2.34 | -8.5 dB  |
| Peaking | 3235 Hz  | 3.95 | 6.5 dB   |
| Peaking | 5849 Hz  | 3.65 | 7.0 dB   |
| Peaking | 769 Hz   | 1.88 | 2.0 dB   |
| Peaking | 1513 Hz  | 4.57 | -1.2 dB  |
| Peaking | 4396 Hz  | 6.52 | -6.6 dB  |
| Peaking | 4512 Hz  | 2.61 | 2.9 dB   |
| Peaking | 22050 Hz | 1.76 | 0.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.9 dB |
| Peaking | 62 Hz    | 1.41 | -7.1 dB  |
| Peaking | 125 Hz   | 1.41 | -7.1 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -7.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Bass%20Boost%20Filter/Torque%20t096z%20Bass%20Boost%20Filter.png)