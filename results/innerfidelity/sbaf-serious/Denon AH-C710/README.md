# Denon AH-C710
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.6; 25 -11.6; 28 -11.6; 31 -11.6; 34 -11.6; 37 -11.5; 41 -11.5; 45 -11.5; 49 -11.4; 54 -11.4; 60 -11.4; 66 -11.4; 72 -11.4; 79 -11.4; 87 -11.4; 96 -11.4; 106 -11.2; 116 -11.0; 128 -10.8; 141 -10.6; 155 -10.2; 170 -9.8; 187 -9.4; 206 -8.9; 227 -8.2; 249 -7.6; 274 -7.1; 302 -6.4; 332 -5.8; 365 -5.0; 402 -4.5; 442 -3.6; 486 -3.2; 535 -2.5; 588 -1.8; 647 -1.2; 712 -0.9; 783 -0.5; 861 -0.6; 947 -0.6; 1042 -0.8; 1146 -0.9; 1261 -0.6; 1387 -1.5; 1526 -2.2; 1678 -2.8; 1846 -3.0; 2031 -3.3; 2234 -4.0; 2457 -5.0; 2703 -6.0; 2973 -5.5; 3270 -3.5; 3597 -2.1; 3957 -2.7; 4353 -5.4; 4788 -8.1; 5267 -11.6; 5793 -10.6; 6373 -5.2; 7010 -3.1; 7711 -4.9; 8482 -7.6; 9330 -7.5; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C710 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C710 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 0.17 | -6.6 dB |
| Peaking | 793 Hz   | 0.66 | 5.6 dB  |
| Peaking | 3726 Hz  | 6.38 | 3.4 dB  |
| Peaking | 5374 Hz  | 5.45 | -8.2 dB |
| Peaking | 21147 Hz | 1.92 | -0.6 dB |
| Peaking | 1285 Hz  | 5.68 | 0.9 dB  |
| Peaking | 2737 Hz  | 6.43 | -2.3 dB |
| Peaking | 6908 Hz  | 7.32 | 3.2 dB  |
| Peaking | 8861 Hz  | 7.51 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-C710/Denon%20AH-C710.png)