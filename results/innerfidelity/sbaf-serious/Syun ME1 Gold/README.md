# Syun ME1 Gold
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.5; 34 -2.1; 37 -2.6; 41 -3.1; 45 -3.6; 49 -4.0; 54 -4.5; 60 -5.1; 66 -5.7; 72 -6.2; 79 -6.7; 87 -7.3; 96 -7.9; 106 -8.3; 116 -8.6; 128 -9.1; 141 -9.5; 155 -9.9; 170 -10.1; 187 -10.3; 206 -10.5; 227 -10.5; 249 -10.5; 274 -10.4; 302 -10.3; 332 -10.1; 365 -9.7; 402 -9.3; 442 -8.7; 486 -8.3; 535 -7.8; 588 -7.0; 647 -6.5; 712 -6.2; 783 -5.8; 861 -5.2; 947 -4.8; 1042 -5.1; 1146 -5.3; 1261 -5.7; 1387 -6.2; 1526 -6.8; 1678 -7.1; 1846 -7.0; 2031 -6.7; 2234 -6.4; 2457 -5.5; 2703 -4.7; 2973 -3.3; 3270 -2.1; 3597 -2.2; 3957 -4.0; 4353 -7.8; 4788 -10.4; 5267 -7.8; 5793 -3.0; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Syun ME1 Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Syun ME1 Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.74 | 6.2 dB  |
| Peaking | 209 Hz  | 0.74 | -4.5 dB |
| Peaking | 3513 Hz | 2.47 | 5.7 dB  |
| Peaking | 4788 Hz | 3.37 | -6.4 dB |
| Peaking | 6200 Hz | 4.47 | 6.8 dB  |
| Peaking | 219 Hz  | 1.39 | 1.6 dB  |
| Peaking | 341 Hz  | 0.57 | -1.8 dB |
| Peaking | 983 Hz  | 0.8  | 2.8 dB  |
| Peaking | 1678 Hz | 1.64 | -2.1 dB |
| Peaking | 8072 Hz | 5.25 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Syun%20ME1%20Gold/Syun%20ME1%20Gold.png)