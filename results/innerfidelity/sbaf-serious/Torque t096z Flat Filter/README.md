# Torque t096z Flat Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.3; 25 -4.6; 28 -5.1; 31 -5.5; 34 -5.8; 37 -6.0; 41 -6.3; 45 -6.6; 49 -6.9; 54 -7.2; 60 -7.6; 66 -8.0; 72 -8.4; 79 -8.8; 87 -9.4; 96 -9.8; 106 -10.1; 116 -10.4; 128 -10.8; 141 -11.1; 155 -11.4; 170 -11.5; 187 -11.6; 206 -11.6; 227 -11.5; 249 -11.4; 274 -11.3; 302 -10.9; 332 -10.6; 365 -10.1; 402 -9.6; 442 -8.9; 486 -8.4; 535 -7.7; 588 -6.9; 647 -6.4; 712 -6.1; 783 -5.8; 861 -5.9; 947 -6.2; 1042 -6.7; 1146 -7.3; 1261 -8.0; 1387 -9.1; 1526 -10.6; 1678 -11.9; 1846 -13.0; 2031 -12.9; 2234 -11.9; 2457 -8.5; 2703 -5.5; 2973 -2.2; 3270 -0.5; 3597 -0.5; 3957 -2.9; 4353 -7.5; 4788 -6.6; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Flat Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Flat Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.19 | 2.8 dB  |
| Peaking | 183 Hz  | 0.64 | -5.5 dB |
| Peaking | 1959 Hz | 2.28 | -7.8 dB |
| Peaking | 3275 Hz | 3.36 | 7.7 dB  |
| Peaking | 5949 Hz | 4.14 | 6.7 dB  |
| Peaking | 362 Hz  | 2.21 | -1.1 dB |
| Peaking | 784 Hz  | 1.58 | 1.8 dB  |
| Peaking | 1497 Hz | 4.05 | -1.2 dB |
| Peaking | 4486 Hz | 2.49 | 3.1 dB  |
| Peaking | 4538 Hz | 6.42 | -7.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Flat%20Filter/Torque%20t096z%20Flat%20Filter.png)