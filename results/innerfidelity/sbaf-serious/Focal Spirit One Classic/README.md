# Focal Spirit One Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.8; 25 -9.8; 28 -9.8; 31 -9.7; 34 -9.7; 37 -9.6; 41 -9.5; 45 -9.4; 49 -9.3; 54 -9.2; 60 -9.2; 66 -9.0; 72 -9.0; 79 -8.9; 87 -9.3; 96 -10.5; 106 -10.9; 116 -10.4; 128 -10.1; 141 -10.7; 155 -10.7; 170 -10.4; 187 -10.6; 206 -10.5; 227 -10.1; 249 -9.8; 274 -9.4; 302 -9.0; 332 -8.4; 365 -8.1; 402 -7.7; 442 -7.7; 486 -7.9; 535 -7.6; 588 -7.0; 647 -6.5; 712 -5.8; 783 -5.8; 861 -6.1; 947 -6.3; 1042 -6.0; 1146 -5.7; 1261 -5.6; 1387 -5.8; 1526 -6.1; 1678 -6.1; 1846 -6.1; 2031 -5.8; 2234 -5.6; 2457 -5.1; 2703 -5.0; 2973 -5.7; 3270 -6.5; 3597 -6.6; 3957 -5.5; 4353 -4.1; 4788 -3.3; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.7; 10263 -7.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.11 | -2.7 dB |
| Peaking | 37 Hz   | 1.3  | -1.5 dB |
| Peaking | 159 Hz  | 0.54 | -4.2 dB |
| Peaking | 1072 Hz | 0.57 | 0.9 dB  |
| Peaking | 5723 Hz | 2.96 | 6.7 dB  |
| Peaking | 28 Hz   | 1.21 | 0.2 dB  |
| Peaking | 366 Hz  | 5.27 | 0.2 dB  |
| Peaking | 3399 Hz | 1.71 | 2.0 dB  |
| Peaking | 3508 Hz | 3.65 | -3.2 dB |
| Peaking | 9725 Hz | 2.64 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20One%20Classic/Focal%20Spirit%20One%20Classic.png)