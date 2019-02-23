# Fostex T50RP Mk3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.2; 49 -2.1; 54 -3.3; 60 -4.6; 66 -5.6; 72 -6.5; 79 -7.2; 87 -7.8; 96 -8.2; 106 -8.4; 116 -8.5; 128 -8.6; 141 -8.6; 155 -8.4; 170 -8.0; 187 -7.6; 206 -7.4; 227 -7.1; 249 -6.8; 274 -6.8; 302 -6.7; 332 -6.3; 365 -6.0; 402 -5.6; 442 -5.1; 486 -5.5; 535 -5.3; 588 -5.6; 647 -5.8; 712 -6.3; 783 -6.7; 861 -7.3; 947 -8.0; 1042 -7.6; 1146 -7.2; 1261 -6.7; 1387 -6.6; 1526 -6.2; 1678 -6.2; 1846 -5.8; 2031 -5.6; 2234 -5.3; 2457 -5.5; 2703 -5.4; 2973 -6.0; 3270 -6.4; 3597 -7.4; 3957 -8.2; 4353 -9.2; 4788 -7.8; 5267 -3.2; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.4; 9330 -11.9; 10263 -9.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T50RP Mk3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP Mk3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 52 Hz   | 0.22 | 9.7 dB   |
| Peaking | 104 Hz  | 0.56 | -10.8 dB |
| Peaking | 4554 Hz | 2.28 | -10.6 dB |
| Peaking | 5503 Hz | 1.34 | 11.0 dB  |
| Peaking | 9144 Hz | 2.8  | -7.8 dB  |
| Peaking | 43 Hz   | 3.4  | 1.0 dB   |
| Peaking | 63 Hz   | 3.16 | -0.6 dB  |
| Peaking | 514 Hz  | 2.29 | 1.1 dB   |
| Peaking | 972 Hz  | 2.74 | -1.8 dB  |
| Peaking | 2247 Hz | 2.98 | 0.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50RP%20Mk3/Fostex%20T50RP%20Mk3.png)