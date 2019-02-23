# Teknmotion London Underground
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -2.0; 28 -3.0; 31 -3.9; 34 -4.7; 37 -5.5; 41 -6.3; 45 -7.0; 49 -7.6; 54 -8.3; 60 -9.0; 66 -9.5; 72 -9.8; 79 -10.1; 87 -10.2; 96 -10.4; 106 -10.5; 116 -10.4; 128 -10.2; 141 -10.1; 155 -9.9; 170 -9.5; 187 -9.1; 206 -8.7; 227 -8.2; 249 -7.8; 274 -7.4; 302 -6.7; 332 -6.1; 365 -5.4; 402 -4.9; 442 -4.5; 486 -4.8; 535 -5.6; 588 -6.4; 647 -8.0; 712 -9.6; 783 -10.2; 861 -10.8; 947 -10.9; 1042 -11.3; 1146 -10.7; 1261 -10.7; 1387 -11.8; 1526 -11.3; 1678 -10.2; 1846 -8.5; 2031 -6.4; 2234 -5.0; 2457 -3.1; 2703 -2.0; 2973 -1.5; 3270 -1.6; 3597 -1.1; 3957 -0.7; 4353 -1.4; 4788 -1.5; 5267 -1.2; 5793 -1.0; 6373 -1.2; 7010 -4.2; 7711 -6.4; 8482 -7.7; 9330 -8.8; 10263 -8.6; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Teknmotion London Underground GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teknmotion London Underground ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.18 | 6.5 dB  |
| Peaking | 80 Hz   | 1.12 | -3.7 dB |
| Peaking | 145 Hz  | 1.92 | -2.5 dB |
| Peaking | 1338 Hz | 1.2  | -6.7 dB |
| Peaking | 3587 Hz | 0.86 | 7.0 dB  |
| Peaking | 478 Hz  | 1.85 | 3.9 dB  |
| Peaking | 792 Hz  | 1.15 | -2.4 dB |
| Peaking | 1214 Hz | 5.61 | 2.5 dB  |
| Peaking | 6201 Hz | 4.22 | 3.7 dB  |
| Peaking | 9148 Hz | 2.08 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Teknmotion%20London%20Underground/Teknmotion%20London%20Underground.png)