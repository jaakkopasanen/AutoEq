# Klipsch Mode M40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -3.3; 25 -3.9; 28 -4.7; 31 -5.2; 34 -5.7; 37 -6.0; 41 -6.3; 45 -6.5; 49 -6.7; 54 -6.7; 60 -6.8; 66 -6.7; 72 -6.7; 79 -6.8; 87 -6.8; 96 -6.9; 106 -6.9; 116 -6.7; 128 -6.8; 141 -6.9; 155 -6.9; 170 -6.7; 187 -6.7; 206 -6.6; 227 -6.4; 249 -6.0; 274 -6.1; 302 -5.9; 332 -5.4; 365 -5.5; 402 -5.5; 442 -5.5; 486 -5.4; 535 -5.4; 588 -5.1; 647 -5.2; 712 -5.3; 783 -5.3; 861 -5.7; 947 -6.2; 1042 -6.7; 1146 -7.4; 1261 -8.5; 1387 -10.3; 1526 -11.8; 1678 -11.3; 1846 -9.5; 2031 -6.1; 2234 -3.3; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Mode M40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Mode M40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.31 | 4.9 dB  |
| Peaking | 103 Hz  | 0.24 | -0.7 dB |
| Peaking | 513 Hz  | 0.61 | 1.5 dB  |
| Peaking | 1603 Hz | 2.03 | -9.6 dB |
| Peaking | 3230 Hz | 0.69 | 7.7 dB  |
| Peaking | 17 Hz   | 0.9  | -0.4 dB |
| Peaking | 2544 Hz | 4.74 | 1.8 dB  |
| Peaking | 3230 Hz | 1.5  | -1.2 dB |
| Peaking | 6195 Hz | 2.04 | 5.5 dB  |
| Peaking | 7521 Hz | 1.46 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Mode%20M40/Klipsch%20Mode%20M40.png)