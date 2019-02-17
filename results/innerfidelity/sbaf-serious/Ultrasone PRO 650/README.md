# Ultrasone PRO 650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.1; 37 -1.8; 41 -2.5; 45 -2.8; 49 -3.0; 54 -3.2; 60 -2.9; 66 -3.5; 72 -4.6; 79 -5.3; 87 -5.7; 96 -5.6; 106 -5.7; 116 -5.8; 128 -5.8; 141 -5.6; 155 -5.3; 170 -4.8; 187 -4.7; 206 -4.3; 227 -3.9; 249 -3.5; 274 -3.3; 302 -3.7; 332 -4.1; 365 -5.1; 402 -6.4; 442 -6.9; 486 -5.2; 535 -4.7; 588 -4.8; 647 -4.5; 712 -4.9; 783 -5.2; 861 -6.0; 947 -6.4; 1042 -6.7; 1146 -6.7; 1261 -6.8; 1387 -7.4; 1526 -8.1; 1678 -8.3; 1846 -6.7; 2031 -3.8; 2234 -1.9; 2457 -1.5; 2703 -6.4; 2973 -5.4; 3270 -6.5; 3597 -7.1; 3957 -7.3; 4353 -5.4; 4788 -1.0; 5267 -3.5; 5793 -4.2; 6373 -5.7; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -11.4; 16529 -10.9; 18182 -7.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.65 | 6.2 dB  |
| Peaking | 267 Hz   | 1.45 | 3.0 dB  |
| Peaking | 2336 Hz  | 7.54 | 6.3 dB  |
| Peaking | 4952 Hz  | 5.56 | 5.6 dB  |
| Peaking | 15872 Hz | 2.65 | -6.1 dB |
| Peaking | 429 Hz   | 5.23 | -2.2 dB |
| Peaking | 602 Hz   | 2.03 | 1.8 dB  |
| Peaking | 1571 Hz  | 3.92 | -2.5 dB |
| Peaking | 3887 Hz  | 2.87 | -2.5 dB |
| Peaking | 4409 Hz  | 0.68 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%20650/Ultrasone%20PRO%20650.png)