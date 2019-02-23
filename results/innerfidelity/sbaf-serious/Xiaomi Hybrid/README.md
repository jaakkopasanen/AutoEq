# Xiaomi Hybrid
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -11.2; 25 -11.5; 28 -11.8; 31 -12.1; 34 -12.2; 37 -12.4; 41 -12.6; 45 -12.7; 49 -12.8; 54 -13.0; 60 -13.1; 66 -13.2; 72 -13.3; 79 -13.3; 87 -13.5; 96 -13.7; 106 -13.4; 116 -13.3; 128 -13.2; 141 -13.0; 155 -12.7; 170 -12.4; 187 -12.0; 206 -11.6; 227 -11.1; 249 -10.6; 274 -9.9; 302 -9.3; 332 -8.8; 365 -8.2; 402 -7.7; 442 -7.0; 486 -6.6; 535 -6.0; 588 -5.3; 647 -5.0; 712 -4.8; 783 -4.6; 861 -4.8; 947 -5.1; 1042 -5.6; 1146 -6.1; 1261 -6.6; 1387 -7.7; 1526 -8.9; 1678 -10.1; 1846 -11.0; 2031 -11.4; 2234 -11.4; 2457 -9.5; 2703 -7.2; 2973 -5.1; 3270 -4.0; 3597 -5.0; 3957 -6.7; 4353 -5.5; 4788 -2.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.4; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Xiaomi Hybrid GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Hybrid ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.47 | -5.6 dB |
| Peaking | 114 Hz  | 1.01 | -4.2 dB |
| Peaking | 213 Hz  | 1.72 | -2.9 dB |
| Peaking | 2018 Hz | 3.07 | -5.9 dB |
| Peaking | 5607 Hz | 2.54 | 6.8 dB  |
| Peaking | 785 Hz  | 1.67 | 2.4 dB  |
| Peaking | 1593 Hz | 4.41 | -1.6 dB |
| Peaking | 3254 Hz | 5.62 | 2.8 dB  |
| Peaking | 4080 Hz | 8.18 | -2.3 dB |
| Peaking | 8194 Hz | 4.62 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.2 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Hybrid/Xiaomi%20Hybrid.png)