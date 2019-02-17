# Syun ME1 Gold
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.5; 28 -2.2; 31 -2.9; 34 -3.6; 37 -4.1; 41 -4.6; 45 -5.1; 49 -5.5; 54 -6.0; 60 -6.6; 66 -7.1; 72 -7.7; 79 -8.2; 87 -8.8; 96 -9.4; 106 -9.8; 116 -10.1; 128 -10.5; 141 -11.0; 155 -11.3; 170 -11.6; 187 -11.8; 206 -11.9; 227 -12.0; 249 -12.0; 274 -11.9; 302 -11.8; 332 -11.5; 365 -11.2; 402 -10.8; 442 -10.1; 486 -9.8; 535 -9.3; 588 -8.4; 647 -8.0; 712 -7.7; 783 -7.3; 861 -6.7; 947 -6.2; 1042 -6.5; 1146 -6.8; 1261 -7.1; 1387 -7.7; 1526 -8.2; 1678 -8.5; 1846 -8.5; 2031 -8.2; 2234 -7.8; 2457 -7.0; 2703 -6.2; 2973 -4.8; 3270 -3.6; 3597 -3.7; 3957 -5.5; 4353 -9.3; 4788 -11.9; 5267 -9.3; 5793 -4.5; 6373 -1.7; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Syun ME1 Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Syun ME1 Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.68 | 6.4 dB  |
| Peaking | 216 Hz  | 0.51 | -5.8 dB |
| Peaking | 3571 Hz | 3.6  | 5.2 dB  |
| Peaking | 4823 Hz | 2.51 | -7.0 dB |
| Peaking | 6252 Hz | 3.92 | 7.0 dB  |
| Peaking | 390 Hz  | 2.82 | -0.6 dB |
| Peaking | 957 Hz  | 1.63 | 1.6 dB  |
| Peaking | 1778 Hz | 1.56 | -2.1 dB |
| Peaking | 2994 Hz | 4.56 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Syun%20ME1%20Gold/Syun%20ME1%20Gold.png)