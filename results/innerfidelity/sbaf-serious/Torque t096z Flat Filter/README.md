# Torque t096z Flat Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.1; 25 -4.5; 28 -4.9; 31 -5.3; 34 -5.6; 37 -5.8; 41 -6.1; 45 -6.4; 49 -6.7; 54 -7.0; 60 -7.4; 66 -7.9; 72 -8.3; 79 -8.7; 87 -9.2; 96 -9.7; 106 -9.9; 116 -10.2; 128 -10.6; 141 -10.9; 155 -11.2; 170 -11.3; 187 -11.4; 206 -11.5; 227 -11.3; 249 -11.2; 274 -11.1; 302 -10.8; 332 -10.4; 365 -9.9; 402 -9.4; 442 -8.7; 486 -8.2; 535 -7.6; 588 -6.7; 647 -6.2; 712 -6.0; 783 -5.6; 861 -5.7; 947 -6.0; 1042 -6.5; 1146 -7.1; 1261 -7.8; 1387 -9.0; 1526 -10.4; 1678 -11.7; 1846 -12.8; 2031 -12.8; 2234 -11.7; 2457 -8.4; 2703 -5.4; 2973 -2.1; 3270 -0.5; 3597 -0.5; 3957 -2.8; 4353 -7.4; 4788 -6.4; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Flat Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Flat Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  1.1  | 2.9 dB  |
| Peaking | 183 Hz  |  0.66 | -5.3 dB |
| Peaking | 1964 Hz |  2.35 | -7.7 dB |
| Peaking | 3270 Hz |  3.26 | 7.7 dB  |
| Peaking | 5939 Hz |  4.08 | 6.7 dB  |
| Peaking | 363 Hz  |  2.18 | -1.1 dB |
| Peaking | 785 Hz  |  1.46 | 1.9 dB  |
| Peaking | 1504 Hz |  4.41 | -1.3 dB |
| Peaking | 3799 Hz | 10.39 | 2.2 dB  |
| Peaking | 4481 Hz |  9.65 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Flat%20Filter/Torque%20t096z%20Flat%20Filter.png)