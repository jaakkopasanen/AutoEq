# Grado SR325
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.5; 49 -2.4; 54 -3.3; 60 -4.2; 66 -4.9; 72 -5.5; 79 -5.9; 87 -6.4; 96 -6.8; 106 -6.8; 116 -6.8; 128 -6.8; 141 -6.8; 155 -6.8; 170 -6.6; 187 -6.4; 206 -6.5; 227 -6.4; 249 -6.3; 274 -6.2; 302 -6.0; 332 -5.6; 365 -5.4; 402 -6.1; 442 -6.0; 486 -6.0; 535 -6.2; 588 -5.8; 647 -5.9; 712 -6.0; 783 -5.9; 861 -6.1; 947 -6.5; 1042 -6.6; 1146 -6.8; 1261 -7.6; 1387 -8.8; 1526 -10.1; 1678 -10.8; 1846 -11.9; 2031 -15.9; 2234 -14.0; 2457 -12.0; 2703 -10.6; 2973 -8.6; 3270 -7.6; 3597 -4.3; 3957 -10.2; 4353 -14.0; 4788 -15.3; 5267 -12.2; 5793 -10.2; 6373 -9.5; 7010 -12.3; 7711 -12.4; 8482 -15.4; 9330 -17.5; 10263 -14.6; 11289 -10.1; 12418 -6.9; 13660 -6.5; 15026 -6.5; 16529 -6.9; 18182 -7.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 1.02 | 6.9 dB   |
| Peaking | 2059 Hz  | 3.16 | -8.2 dB  |
| Peaking | 9881 Hz  | 0.95 | -20.9 dB |
| Peaking | 11486 Hz | 0.87 | 13.3 dB  |
| Peaking | 21311 Hz | 2.43 | -7.7 dB  |
| Peaking | 114 Hz   | 1.6  | -1.1 dB  |
| Peaking | 538 Hz   | 0.75 | 0.9 dB   |
| Peaking | 3670 Hz  | 5.87 | 9.3 dB   |
| Peaking | 4492 Hz  | 2.29 | -7.2 dB  |
| Peaking | 6097 Hz  | 3.58 | 4.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.7 dB |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -8.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR325/Grado%20SR325.png)