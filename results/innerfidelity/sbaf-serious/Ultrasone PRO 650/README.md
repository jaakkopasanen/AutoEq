# Ultrasone PRO 650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.2; 31 -2.1; 34 -3.0; 37 -3.7; 41 -4.4; 45 -4.7; 49 -4.9; 54 -5.1; 60 -4.8; 66 -5.4; 72 -6.5; 79 -7.2; 87 -7.6; 96 -7.5; 106 -7.6; 116 -7.7; 128 -7.7; 141 -7.5; 155 -7.2; 170 -6.7; 187 -6.6; 206 -6.2; 227 -5.8; 249 -5.4; 274 -5.2; 302 -5.6; 332 -6.0; 365 -7.0; 402 -8.3; 442 -8.8; 486 -7.1; 535 -6.6; 588 -6.7; 647 -6.4; 712 -6.8; 783 -7.1; 861 -7.9; 947 -8.3; 1042 -8.6; 1146 -8.6; 1261 -8.7; 1387 -9.3; 1526 -10.0; 1678 -10.2; 1846 -8.6; 2031 -5.7; 2234 -3.6; 2457 -2.9; 2703 -8.3; 2973 -7.3; 3270 -8.4; 3597 -9.0; 3957 -9.2; 4353 -7.3; 4788 -2.9; 5267 -5.4; 5793 -6.1; 6373 -7.6; 7010 -5.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.6; 15026 -13.3; 16529 -12.8; 18182 -8.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.44 | 6.4 dB  |
| Peaking | 1485 Hz  | 1.38 | -3.4 dB |
| Peaking | 2339 Hz  | 8.54 | 7.3 dB  |
| Peaking | 3588 Hz  | 5.17 | -2.6 dB |
| Peaking | 15994 Hz | 2.22 | -8.2 dB |
| Peaking | 119 Hz   | 1.51 | -1.7 dB |
| Peaking | 315 Hz   | 1.05 | 1.7 dB  |
| Peaking | 418 Hz   | 3.72 | -3.4 dB |
| Peaking | 4171 Hz  | 6.36 | -2.5 dB |
| Peaking | 4791 Hz  | 6.11 | 4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -6.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%20650/Ultrasone%20PRO%20650.png)