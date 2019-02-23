# Denon AH-D1001
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.1; 37 -1.6; 41 -2.2; 45 -2.8; 49 -3.2; 54 -3.6; 60 -3.8; 66 -4.1; 72 -4.6; 79 -5.2; 87 -5.9; 96 -6.5; 106 -6.8; 116 -7.0; 128 -7.4; 141 -7.5; 155 -7.6; 170 -7.5; 187 -7.4; 206 -7.2; 227 -6.9; 249 -6.5; 274 -6.1; 302 -5.7; 332 -5.4; 365 -5.0; 402 -4.7; 442 -4.4; 486 -4.5; 535 -4.7; 588 -5.1; 647 -6.2; 712 -7.5; 783 -8.1; 861 -8.7; 947 -8.6; 1042 -8.4; 1146 -7.9; 1261 -7.3; 1387 -7.2; 1526 -7.0; 1678 -6.5; 1846 -5.5; 2031 -4.5; 2234 -4.4; 2457 -5.0; 2703 -6.4; 2973 -4.6; 3270 -4.0; 3597 -6.9; 3957 -7.7; 4353 -9.2; 4788 -8.1; 5267 -5.2; 5793 -3.8; 6373 -5.1; 7010 -4.7; 7711 -6.3; 8482 -8.4; 9330 -10.6; 10263 -10.1; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D1001 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.9  | 6.5 dB  |
| Peaking | 995 Hz  | 2.5  | -2.8 dB |
| Peaking | 4381 Hz | 2.78 | -7.0 dB |
| Peaking | 5105 Hz | 0.6  | 4.5 dB  |
| Peaking | 9404 Hz | 2.5  | -6.6 dB |
| Peaking | 66 Hz   | 2.24 | 1.3 dB  |
| Peaking | 149 Hz  | 0.94 | -1.6 dB |
| Peaking | 464 Hz  | 1.19 | 3.6 dB  |
| Peaking | 687 Hz  | 0.7  | -1.5 dB |
| Peaking | 2102 Hz | 7.04 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D1001/Denon%20AH-D1001.png)