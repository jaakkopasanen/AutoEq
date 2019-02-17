# Fostex T20RP Mk3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -2.2; 49 -3.6; 54 -5.2; 60 -6.8; 66 -8.3; 72 -9.5; 79 -10.6; 87 -11.4; 96 -12.0; 106 -12.0; 116 -11.9; 128 -11.6; 141 -11.2; 155 -10.8; 170 -10.2; 187 -9.7; 206 -9.1; 227 -8.8; 249 -8.6; 274 -8.2; 302 -8.5; 332 -8.0; 365 -6.7; 402 -6.3; 442 -6.1; 486 -4.1; 535 -4.4; 588 -4.1; 647 -3.5; 712 -3.8; 783 -3.6; 861 -5.1; 947 -5.7; 1042 -6.4; 1146 -6.8; 1261 -5.6; 1387 -6.8; 1526 -5.0; 1678 -4.8; 1846 -4.8; 2031 -3.7; 2234 -4.1; 2457 -3.8; 2703 -3.8; 2973 -4.3; 3270 -4.7; 3597 -5.5; 3957 -7.3; 4353 -8.0; 4788 -6.0; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.1; 9330 -12.7; 10263 -10.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T20RP Mk3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T20RP Mk3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 39 Hz   | 0.5  | 11.3 dB  |
| Peaking | 85 Hz   | 0.56 | -11.2 dB |
| Peaking | 627 Hz  | 1.18 | 3.4 dB   |
| Peaking | 5989 Hz | 2.99 | 7.0 dB   |
| Peaking | 9287 Hz | 3.93 | -7.4 dB  |
| Peaking | 315 Hz  | 7.36 | -1.1 dB  |
| Peaking | 1165 Hz | 1.95 | -1.9 dB  |
| Peaking | 2754 Hz | 0.74 | 3.3 dB   |
| Peaking | 4454 Hz | 2.14 | -5.3 dB  |
| Peaking | 5179 Hz | 7.96 | 3.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T20RP%20Mk3/Fostex%20T20RP%20Mk3.png)