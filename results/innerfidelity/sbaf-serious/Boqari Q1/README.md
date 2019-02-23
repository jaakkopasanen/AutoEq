# Boqari Q1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.9; 49 -1.4; 54 -1.9; 60 -2.5; 66 -3.0; 72 -3.6; 79 -4.2; 87 -4.8; 96 -5.5; 106 -5.9; 116 -6.4; 128 -6.9; 141 -7.5; 155 -8.0; 170 -8.4; 187 -8.8; 206 -9.3; 227 -9.5; 249 -10.0; 274 -10.3; 302 -10.6; 332 -10.9; 365 -11.1; 402 -11.3; 442 -11.1; 486 -10.8; 535 -10.6; 588 -10.0; 647 -9.7; 712 -9.3; 783 -8.8; 861 -8.2; 947 -7.9; 1042 -8.1; 1146 -8.3; 1261 -8.5; 1387 -8.9; 1526 -9.0; 1678 -8.8; 1846 -8.0; 2031 -6.8; 2234 -5.6; 2457 -4.1; 2703 -2.7; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -2.2; 4353 -6.2; 4788 -9.9; 5267 -9.5; 5793 -4.7; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Boqari Q1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Boqari Q1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.37 | 6.5 dB  |
| Peaking | 356 Hz  | 0.33 | -4.5 dB |
| Peaking | 3399 Hz | 2.06 | 7.8 dB  |
| Peaking | 4978 Hz | 3.75 | -7.0 dB |
| Peaking | 6304 Hz | 5.06 | 6.3 dB  |
| Peaking | 409 Hz  | 2.95 | -0.8 dB |
| Peaking | 908 Hz  | 1.97 | 1.5 dB  |
| Peaking | 1607 Hz | 2.14 | -1.9 dB |
| Peaking | 2575 Hz | 4.13 | 1.1 dB  |
| Peaking | 8205 Hz | 5.06 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.8 dB |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Boqari%20Q1/Boqari%20Q1.png)