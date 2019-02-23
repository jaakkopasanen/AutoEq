# Ultrasone Edition 10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.6; 34 -2.5; 37 -3.3; 41 -4.1; 45 -4.6; 49 -4.9; 54 -5.4; 60 -6.2; 66 -6.6; 72 -7.1; 79 -7.3; 87 -7.5; 96 -8.0; 106 -8.2; 116 -8.2; 128 -8.3; 141 -8.3; 155 -8.2; 170 -7.9; 187 -7.8; 206 -7.5; 227 -7.2; 249 -7.0; 274 -6.7; 302 -6.6; 332 -6.3; 365 -6.0; 402 -5.9; 442 -5.7; 486 -5.7; 535 -5.8; 588 -5.7; 647 -5.8; 712 -6.0; 783 -6.0; 861 -6.6; 947 -7.1; 1042 -7.7; 1146 -8.3; 1261 -8.7; 1387 -8.4; 1526 -7.4; 1678 -5.8; 1846 -0.9; 2031 -0.5; 2234 -1.4; 2457 -1.0; 2703 -0.7; 2973 -3.1; 3270 -6.7; 3597 -9.5; 3957 -11.5; 4353 -10.9; 4788 -5.9; 5267 -6.5; 5793 -12.5; 6373 -17.3; 7010 -9.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.9; 15026 -15.6; 16529 -13.7; 18182 -8.4; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Edition 10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 1.7  | 6.8 dB   |
| Peaking | 2400 Hz  | 2.27 | 6.9 dB   |
| Peaking | 3932 Hz  | 4.72 | -6.5 dB  |
| Peaking | 6282 Hz  | 7.94 | -12.0 dB |
| Peaking | 15599 Hz | 2.17 | -10.3 dB |
| Peaking | 134 Hz   | 0.98 | -2.2 dB  |
| Peaking | 1053 Hz  | 0.46 | 2.6 dB   |
| Peaking | 1360 Hz  | 1.02 | -5.5 dB  |
| Peaking | 1888 Hz  | 6.24 | 5.1 dB   |
| Peaking | 10577 Hz | 1.54 | 1.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB |
| Peaking | 2000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -8.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Edition%2010/Ultrasone%20Edition%2010.png)