# Boqari Q1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.0; 66 -1.5; 72 -2.1; 79 -2.7; 87 -3.3; 96 -3.9; 106 -4.4; 116 -4.9; 128 -5.4; 141 -6.0; 155 -6.5; 170 -6.9; 187 -7.3; 206 -7.7; 227 -8.0; 249 -8.5; 274 -8.8; 302 -9.1; 332 -9.4; 365 -9.6; 402 -9.8; 442 -9.6; 486 -9.3; 535 -9.1; 588 -8.5; 647 -8.2; 712 -7.8; 783 -7.3; 861 -6.7; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.0; 1387 -7.4; 1526 -7.5; 1678 -7.2; 1846 -6.5; 2031 -5.3; 2234 -4.1; 2457 -2.6; 2703 -1.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.9; 4353 -4.7; 4788 -8.4; 5267 -8.0; 5793 -3.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Boqari Q1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Boqari Q1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.41 | 6.5 dB  |
| Peaking | 347 Hz  | 0.63 | -3.4 dB |
| Peaking | 3339 Hz | 1.69 | 7.2 dB  |
| Peaking | 4967 Hz | 4.75 | -6.0 dB |
| Peaking | 6206 Hz | 5.35 | 6.0 dB  |
| Peaking | 922 Hz  | 3.62 | 1.1 dB  |
| Peaking | 1598 Hz | 2.62 | -1.6 dB |
| Peaking | 2558 Hz | 5.2  | 1.3 dB  |
| Peaking | 6815 Hz | 8.54 | 1.4 dB  |
| Peaking | 7773 Hz | 2.28 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Boqari%20Q1/Boqari%20Q1.png)