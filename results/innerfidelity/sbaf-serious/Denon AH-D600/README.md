# Denon AH-D600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.4; 25 -10.5; 28 -10.5; 31 -10.6; 34 -10.6; 37 -10.5; 41 -10.4; 45 -10.3; 49 -10.1; 54 -9.7; 60 -9.6; 66 -9.8; 72 -10.6; 79 -11.2; 87 -11.5; 96 -11.8; 106 -11.9; 116 -11.9; 128 -12.0; 141 -12.0; 155 -11.5; 170 -10.5; 187 -10.1; 206 -8.7; 227 -6.4; 249 -4.6; 274 -4.2; 302 -5.2; 332 -6.0; 365 -6.1; 402 -6.2; 442 -5.5; 486 -6.0; 535 -6.5; 588 -6.5; 647 -6.4; 712 -6.6; 783 -6.3; 861 -6.3; 947 -6.3; 1042 -6.4; 1146 -6.6; 1261 -7.1; 1387 -8.0; 1526 -8.9; 1678 -9.4; 1846 -9.5; 2031 -8.7; 2234 -7.8; 2457 -8.1; 2703 -7.6; 2973 -6.5; 3270 -4.8; 3597 -2.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.0; 6373 -5.2; 7010 -4.0; 7711 -6.2; 8482 -7.4; 9330 -11.5; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.9; 18182 -9.6; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.49 | -4.0 dB |
| Peaking | 121 Hz  | 1.54 | -5.2 dB |
| Peaking | 2031 Hz | 1.46 | -3.5 dB |
| Peaking | 4518 Hz | 1.63 | 7.2 dB  |
| Peaking | 9322 Hz | 6.04 | -6.1 dB |
| Peaking | 187 Hz  | 3    | -2.1 dB |
| Peaking | 261 Hz  | 3.07 | 3.8 dB  |
| Peaking | 442 Hz  | 6.18 | 1.0 dB  |
| Peaking | 1046 Hz | 1.65 | 0.7 dB  |
| Peaking | 1557 Hz | 4.54 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D600/Denon%20AH-D600.png)