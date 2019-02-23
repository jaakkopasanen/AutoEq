# Denon AH-D1100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -9.2; 25 -9.8; 28 -10.5; 31 -11.1; 34 -11.6; 37 -12.1; 41 -12.7; 45 -13.2; 49 -13.6; 54 -14.0; 60 -14.4; 66 -14.8; 72 -15.1; 79 -15.3; 87 -15.6; 96 -15.7; 106 -15.5; 116 -15.1; 128 -15.5; 141 -15.8; 155 -16.2; 170 -14.6; 187 -15.1; 206 -15.7; 227 -15.4; 249 -14.6; 274 -13.2; 302 -11.3; 332 -9.1; 365 -6.5; 402 -3.8; 442 -1.7; 486 -1.5; 535 -2.2; 588 -3.2; 647 -4.3; 712 -5.1; 783 -5.1; 861 -5.1; 947 -4.6; 1042 -4.0; 1146 -3.4; 1261 -3.0; 1387 -3.2; 1526 -3.8; 1678 -4.1; 1846 -4.1; 2031 -4.5; 2234 -7.1; 2457 -6.3; 2703 -4.3; 2973 -1.7; 3270 -2.9; 3597 -2.7; 3957 -0.5; 4353 -0.8; 4788 -2.4; 5267 -1.0; 5793 -2.0; 6373 -2.4; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -7.7; 10263 -7.8; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D1100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 83 Hz   |  0.4  | -8.1 dB  |
| Peaking | 263 Hz  |  0.79 | -11.7 dB |
| Peaking | 486 Hz  |  0.75 | 18.0 dB  |
| Peaking | 635 Hz  |  1.16 | -8.0 dB  |
| Peaking | 4567 Hz |  1.44 | 5.4 dB   |
| Peaking | 1323 Hz |  4.11 | 1.1 dB   |
| Peaking | 2322 Hz |  5.43 | -2.9 dB  |
| Peaking | 3014 Hz | 10    | 2.8 dB   |
| Peaking | 6297 Hz |  5.49 | 2.3 dB   |
| Peaking | 9393 Hz |  2    | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.4 dB |
| Peaking | 250 Hz   | 1.41 | -7.9 dB |
| Peaking | 500 Hz   | 1.41 | 6.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D1100/Denon%20AH-D1100.png)