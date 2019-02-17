# Denon AH-D400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.4; 34 -2.0; 37 -2.5; 41 -3.0; 45 -3.3; 49 -3.6; 54 -3.9; 60 -4.3; 66 -4.5; 72 -4.8; 79 -5.1; 87 -5.4; 96 -6.0; 106 -6.5; 116 -6.8; 128 -7.2; 141 -7.6; 155 -7.8; 170 -7.9; 187 -7.9; 206 -8.1; 227 -8.0; 249 -8.0; 274 -8.0; 302 -7.6; 332 -7.0; 365 -5.8; 402 -4.4; 442 -2.9; 486 -1.9; 535 -1.0; 588 -0.7; 647 -1.5; 712 -3.0; 783 -3.9; 861 -5.1; 947 -6.0; 1042 -6.7; 1146 -6.7; 1261 -6.2; 1387 -6.4; 1526 -5.8; 1678 -6.0; 1846 -6.4; 2031 -5.5; 2234 -5.0; 2457 -4.7; 2703 -4.5; 2973 -4.0; 3270 -2.7; 3597 -0.5; 3957 -1.2; 4353 -0.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.7  | 6.1 dB  |
| Peaking | 73 Hz   | 1.11 | 1.2 dB  |
| Peaking | 400 Hz  | 0.36 | -3.9 dB |
| Peaking | 552 Hz  | 1.28 | 9.5 dB  |
| Peaking | 4551 Hz | 1.18 | 6.7 dB  |
| Peaking | 1039 Hz | 7.57 | -0.7 dB |
| Peaking | 3615 Hz | 7.05 | 1.9 dB  |
| Peaking | 4153 Hz | 7.13 | -1.7 dB |
| Peaking | 6315 Hz | 3.19 | 4.4 dB  |
| Peaking | 7379 Hz | 1.57 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 6.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D400/Denon%20AH-D400.png)