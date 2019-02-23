# Denon AH-D400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.7; 25 -3.3; 28 -4.1; 31 -4.8; 34 -5.4; 37 -5.8; 41 -6.3; 45 -6.7; 49 -7.0; 54 -7.3; 60 -7.6; 66 -7.9; 72 -8.2; 79 -8.5; 87 -8.8; 96 -9.3; 106 -9.8; 116 -10.2; 128 -10.6; 141 -10.9; 155 -11.2; 170 -11.2; 187 -11.3; 206 -11.4; 227 -11.4; 249 -11.3; 274 -11.4; 302 -10.9; 332 -10.3; 365 -9.1; 402 -7.8; 442 -6.2; 486 -5.2; 535 -4.4; 588 -4.1; 647 -4.9; 712 -6.4; 783 -7.3; 861 -8.5; 947 -9.3; 1042 -10.0; 1146 -10.1; 1261 -9.5; 1387 -9.7; 1526 -9.1; 1678 -9.4; 1846 -9.8; 2031 -8.8; 2234 -8.3; 2457 -8.0; 2703 -7.8; 2973 -7.3; 3270 -6.1; 3597 -0.8; 3957 -4.3; 4353 -4.2; 4788 -3.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.8  | 4.7 dB  |
| Peaking | 174 Hz  | 0.85 | -5.4 dB |
| Peaking | 1574 Hz | 1.16 | -3.5 dB |
| Peaking | 3641 Hz | 8.87 | 5.7 dB  |
| Peaking | 5649 Hz | 2.74 | 7.0 dB  |
| Peaking | 179 Hz  | 3.22 | 1.1 dB  |
| Peaking | 311 Hz  | 1.61 | -2.4 dB |
| Peaking | 550 Hz  | 1.76 | 4.2 dB  |
| Peaking | 979 Hz  | 2.93 | -2.3 dB |
| Peaking | 8181 Hz | 5.02 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.8 dB |
| Peaking | 500 Hz   | 1.41 | 3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D400/Denon%20AH-D400.png)