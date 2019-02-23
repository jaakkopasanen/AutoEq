# Accidentally Extraordinary 51st Studios
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -3.0; 25 -3.7; 28 -4.7; 31 -5.5; 34 -6.2; 37 -6.8; 41 -7.4; 45 -8.0; 49 -8.5; 54 -9.0; 60 -9.5; 66 -9.8; 72 -10.0; 79 -10.3; 87 -10.7; 96 -11.2; 106 -11.2; 116 -11.4; 128 -12.0; 141 -12.4; 155 -12.5; 170 -12.1; 187 -12.2; 206 -11.9; 227 -11.5; 249 -11.0; 274 -10.1; 302 -9.2; 332 -8.2; 365 -7.0; 402 -6.3; 442 -6.0; 486 -6.2; 535 -5.9; 588 -5.6; 647 -6.0; 712 -6.9; 783 -7.3; 861 -8.0; 947 -8.3; 1042 -8.4; 1146 -8.1; 1261 -9.0; 1387 -9.3; 1526 -9.3; 1678 -9.0; 1846 -8.1; 2031 -6.9; 2234 -5.7; 2457 -4.1; 2703 -2.8; 2973 -1.8; 3270 -1.5; 3597 -1.7; 3957 -2.2; 4353 -4.6; 4788 -3.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Accidentally Extraordinary 51st Studios GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Accidentally Extraordinary 51st Studios ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.47 | 4.9 dB  |
| Peaking | 95 Hz   | 0.66 | -4.0 dB |
| Peaking | 191 Hz  | 1.39 | -4.0 dB |
| Peaking | 3264 Hz | 2.98 | 5.4 dB  |
| Peaking | 5761 Hz | 3.12 | 6.4 dB  |
| Peaking | 280 Hz  | 3.29 | -1.3 dB |
| Peaking | 484 Hz  | 1.21 | 1.9 dB  |
| Peaking | 1486 Hz | 0.98 | -3.4 dB |
| Peaking | 2521 Hz | 2.33 | 2.5 dB  |
| Peaking | 8213 Hz | 5.38 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Accidentally%20Extraordinary%2051st%20Studios/Accidentally%20Extraordinary%2051st%20Studios.png)