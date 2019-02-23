# Ultrasone PRO 900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.7; 25 -8.6; 28 -9.6; 31 -10.5; 34 -11.1; 37 -11.7; 41 -12.3; 45 -12.6; 49 -12.8; 54 -13.0; 60 -11.9; 66 -10.1; 72 -10.7; 79 -12.4; 87 -13.4; 96 -13.0; 106 -12.6; 116 -12.9; 128 -12.9; 141 -12.0; 155 -11.9; 170 -10.9; 187 -10.4; 206 -8.6; 227 -6.0; 249 -2.8; 274 -0.5; 302 -1.7; 332 -3.6; 365 -4.7; 402 -5.6; 442 -5.8; 486 -5.8; 535 -2.2; 588 -2.1; 647 -4.6; 712 -4.8; 783 -4.7; 861 -5.1; 947 -5.1; 1042 -4.6; 1146 -3.8; 1261 -3.7; 1387 -4.8; 1526 -6.0; 1678 -6.2; 1846 -5.3; 2031 -4.0; 2234 -4.2; 2457 -6.3; 2703 -10.6; 2973 -9.3; 3270 -9.2; 3597 -9.5; 3957 -9.4; 4353 -9.6; 4788 -4.8; 5267 -1.5; 5793 -6.7; 6373 -13.9; 7010 -11.1; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -10.8; 15026 -14.2; 16529 -13.7; 18182 -11.3; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 125 Hz   | 0.33 | -10.8 dB |
| Peaking | 254 Hz   | 0.91 | -14.2 dB |
| Peaking | 267 Hz   | 1    | 28.2 dB  |
| Peaking | 6528 Hz  | 9.49 | -8.7 dB  |
| Peaking | 16326 Hz | 1.3  | -8.4 dB  |
| Peaking | 21 Hz    | 3.09 | 1.7 dB   |
| Peaking | 2306 Hz  | 3.29 | 4.9 dB   |
| Peaking | 2699 Hz  | 3.68 | -6.2 dB  |
| Peaking | 4192 Hz  | 2.3  | -4.2 dB  |
| Peaking | 5129 Hz  | 6.48 | 8.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | 3.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -8.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%20900/Ultrasone%20PRO%20900.png)