# Accidentally Extraordinary 51st Studios
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -2.0; 28 -3.0; 31 -3.8; 34 -4.5; 37 -5.1; 41 -5.7; 45 -6.3; 49 -6.8; 54 -7.3; 60 -7.8; 66 -8.1; 72 -8.3; 79 -8.6; 87 -9.1; 96 -9.5; 106 -9.5; 116 -9.7; 128 -10.3; 141 -10.8; 155 -10.8; 170 -10.4; 187 -10.5; 206 -10.2; 227 -9.8; 249 -9.3; 274 -8.4; 302 -7.5; 332 -6.5; 365 -5.3; 402 -4.7; 442 -4.3; 486 -4.5; 535 -4.2; 588 -3.9; 647 -4.3; 712 -5.2; 783 -5.6; 861 -6.3; 947 -6.6; 1042 -6.7; 1146 -6.4; 1261 -7.3; 1387 -7.6; 1526 -7.6; 1678 -7.3; 1846 -6.4; 2031 -5.2; 2234 -4.0; 2457 -2.5; 2703 -1.1; 2973 -0.7; 3270 -0.7; 3597 -0.7; 3957 -0.8; 4353 -2.9; 4788 -1.8; 5267 -0.7; 5793 -0.7; 6373 -1.2; 7010 -4.2; 7711 -6.4; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Accidentally Extraordinary 51st Studios GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Accidentally Extraordinary 51st Studios ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.66 | 8.4 dB  |
| Peaking | 422 Hz  | 0.22 | -8.6 dB |
| Peaking | 521 Hz  | 0.62 | 11.2 dB |
| Peaking | 3075 Hz | 1.29 | 7.8 dB  |
| Peaking | 5732 Hz | 2.99 | 5.4 dB  |
| Peaking | 100 Hz  | 1.5  | 0.8 dB  |
| Peaking | 222 Hz  | 0.28 | -0.5 dB |
| Peaking | 363 Hz  | 3.23 | 1.2 dB  |
| Peaking | 1126 Hz | 6.95 | 1.1 dB  |
| Peaking | 8263 Hz | 4.37 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Accidentally%20Extraordinary%2051st%20Studios/Accidentally%20Extraordinary%2051st%20Studios.png)