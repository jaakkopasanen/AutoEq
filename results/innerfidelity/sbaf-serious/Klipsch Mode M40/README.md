# Klipsch Mode M40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -7.3; 25 -7.9; 28 -8.7; 31 -9.3; 34 -9.7; 37 -10.0; 41 -10.3; 45 -10.6; 49 -10.7; 54 -10.8; 60 -10.8; 66 -10.8; 72 -10.8; 79 -10.8; 87 -10.9; 96 -10.9; 106 -10.9; 116 -10.8; 128 -10.8; 141 -10.9; 155 -10.9; 170 -10.8; 187 -10.7; 206 -10.6; 227 -10.4; 249 -10.0; 274 -10.2; 302 -9.9; 332 -9.4; 365 -9.6; 402 -9.6; 442 -9.5; 486 -9.5; 535 -9.4; 588 -9.1; 647 -9.2; 712 -9.3; 783 -9.3; 861 -9.7; 947 -10.2; 1042 -10.7; 1146 -11.5; 1261 -12.6; 1387 -14.3; 1526 -15.8; 1678 -15.3; 1846 -13.6; 2031 -10.2; 2234 -7.3; 2457 -5.1; 2703 -4.1; 2973 -2.6; 3270 -2.5; 3597 -2.3; 3957 -1.3; 4353 -2.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Mode M40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Mode M40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 74 Hz   |  0.39 | -3.8 dB  |
| Peaking | 408 Hz  |  0.3  | -2.2 dB  |
| Peaking | 1587 Hz |  1.93 | -10.2 dB |
| Peaking | 4045 Hz |  0.84 | 6.6 dB   |
| Peaking | 18 Hz   |  2.87 | 1.9 dB   |
| Peaking | 2571 Hz |  5.36 | 1.1 dB   |
| Peaking | 4243 Hz | 10.15 | -2.3 dB  |
| Peaking | 6267 Hz |  2.18 | 6.0 dB   |
| Peaking | 7220 Hz |  1.41 | -4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -4.2 dB |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Mode%20M40/Klipsch%20Mode%20M40.png)