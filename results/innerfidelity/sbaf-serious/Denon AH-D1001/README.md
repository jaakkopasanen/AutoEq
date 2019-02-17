# Denon AH-D1001
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.1; 54 -1.5; 60 -1.7; 66 -2.0; 72 -2.5; 79 -3.1; 87 -3.8; 96 -4.4; 106 -4.7; 116 -4.9; 128 -5.3; 141 -5.4; 155 -5.5; 170 -5.4; 187 -5.3; 206 -5.1; 227 -4.8; 249 -4.4; 274 -4.0; 302 -3.6; 332 -3.2; 365 -2.9; 402 -2.6; 442 -2.3; 486 -2.4; 535 -2.6; 588 -3.0; 647 -4.1; 712 -5.4; 783 -6.0; 861 -6.6; 947 -6.5; 1042 -6.3; 1146 -5.8; 1261 -5.2; 1387 -5.1; 1526 -4.9; 1678 -4.4; 1846 -3.4; 2031 -2.4; 2234 -2.3; 2457 -2.9; 2703 -4.3; 2973 -2.5; 3270 -1.9; 3597 -4.8; 3957 -5.6; 4353 -7.0; 4788 -6.0; 5267 -3.1; 5793 -1.7; 6373 -3.0; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -8.5; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D1001 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.52 | 6.4 dB  |
| Peaking | 431 Hz  | 1.34 | 4.3 dB  |
| Peaking | 2127 Hz | 2.59 | 4.2 dB  |
| Peaking | 3144 Hz | 5.85 | 4.0 dB  |
| Peaking | 5947 Hz | 4.13 | 4.9 dB  |
| Peaking | 591 Hz  | 5.72 | 1.1 dB  |
| Peaking | 858 Hz  | 3.46 | -1.3 dB |
| Peaking | 4425 Hz | 6.09 | -2.4 dB |
| Peaking | 5500 Hz | 0.97 | 0.7 dB  |
| Peaking | 9585 Hz | 4.46 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 4.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D1001/Denon%20AH-D1001.png)