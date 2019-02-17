# Stax SR-40 Electret SR4 Adapter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.2; 106 -2.9; 116 -4.5; 128 -6.1; 141 -7.1; 155 -7.7; 170 -7.8; 187 -7.8; 206 -7.5; 227 -7.3; 249 -7.1; 274 -6.8; 302 -6.6; 332 -6.4; 365 -6.2; 402 -6.1; 442 -6.0; 486 -6.1; 535 -6.4; 588 -6.2; 647 -5.9; 712 -6.0; 783 -6.0; 861 -6.5; 947 -6.4; 1042 -6.3; 1146 -6.5; 1261 -7.6; 1387 -9.0; 1526 -10.5; 1678 -11.2; 1846 -9.9; 2031 -6.9; 2234 -5.8; 2457 -3.8; 2703 -2.4; 2973 -2.4; 3270 -2.5; 3597 -3.9; 3957 -4.5; 4353 -4.7; 4788 -5.3; 5267 -5.0; 5793 -4.7; 6373 -5.2; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-40 Electret SR4 Adapter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-40 Electret SR4 Adapter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 0.28 | 7.4 dB  |
| Peaking | 167 Hz  | 1.06 | -6.5 dB |
| Peaking | 1676 Hz | 2.81 | -6.2 dB |
| Peaking | 2890 Hz | 1.54 | 4.7 dB  |
| Peaking | 6627 Hz | 3.82 | 1.6 dB  |
| Peaking | 17 Hz   | 1.24 | 1.8 dB  |
| Peaking | 44 Hz   | 1.16 | -1.0 dB |
| Peaking | 90 Hz   | 3.78 | 1.6 dB  |
| Peaking | 127 Hz  | 5.14 | -0.9 dB |
| Peaking | 1095 Hz | 7.79 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 6.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-40%20Electret%20SR4%20Adapter/Stax%20SR-40%20Electret%20SR4%20Adapter.png)