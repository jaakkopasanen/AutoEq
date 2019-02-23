# Stax SR-40 Electret SR4 Adapter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.7; 106 -3.5; 116 -5.0; 128 -6.6; 141 -7.7; 155 -8.2; 170 -8.4; 187 -8.3; 206 -8.1; 227 -7.8; 249 -7.6; 274 -7.4; 302 -7.1; 332 -6.9; 365 -6.7; 402 -6.7; 442 -6.5; 486 -6.6; 535 -6.9; 588 -6.8; 647 -6.4; 712 -6.6; 783 -6.5; 861 -7.0; 947 -7.0; 1042 -6.8; 1146 -7.0; 1261 -8.1; 1387 -9.5; 1526 -11.0; 1678 -11.8; 1846 -10.4; 2031 -7.5; 2234 -6.3; 2457 -4.3; 2703 -3.0; 2973 -3.0; 3270 -3.1; 3597 -4.4; 3957 -5.0; 4353 -5.2; 4788 -5.8; 5267 -5.6; 5793 -5.2; 6373 -5.7; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-40 Electret SR4 Adapter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-40 Electret SR4 Adapter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 58 Hz   | 0.32 | 7.6 dB  |
| Peaking | 165 Hz  | 1    | -6.6 dB |
| Peaking | 1668 Hz | 2.55 | -6.4 dB |
| Peaking | 2865 Hz | 1.72 | 4.4 dB  |
| Peaking | 6912 Hz | 6.59 | 1.8 dB  |
| Peaking | 17 Hz   | 1.2  | 2.0 dB  |
| Peaking | 44 Hz   | 1.16 | -1.1 dB |
| Peaking | 89 Hz   | 3.77 | 1.6 dB  |
| Peaking | 128 Hz  | 4.82 | -0.8 dB |
| Peaking | 9317 Hz | 6.78 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.6 dB  |
| Peaking | 62 Hz    | 1.41 | 6.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-40%20Electret%20SR4%20Adapter/Stax%20SR-40%20Electret%20SR4%20Adapter.png)