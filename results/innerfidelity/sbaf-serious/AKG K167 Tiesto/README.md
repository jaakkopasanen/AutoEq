# AKG K167 Tiesto
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.9; 25 -2.4; 28 -3.0; 31 -3.4; 34 -3.7; 37 -3.8; 41 -3.9; 45 -3.9; 49 -3.8; 54 -3.6; 60 -3.0; 66 -2.4; 72 -2.2; 79 -2.8; 87 -3.3; 96 -3.4; 106 -3.6; 116 -3.7; 128 -4.0; 141 -3.9; 155 -3.8; 170 -3.3; 187 -4.3; 206 -4.3; 227 -4.1; 249 -4.1; 274 -4.1; 302 -4.6; 332 -5.2; 365 -5.6; 402 -5.9; 442 -6.0; 486 -6.3; 535 -6.6; 588 -6.6; 647 -6.8; 712 -7.2; 783 -7.3; 861 -7.8; 947 -8.0; 1042 -8.4; 1146 -8.9; 1261 -9.0; 1387 -9.6; 1526 -10.4; 1678 -11.4; 1846 -11.4; 2031 -9.8; 2234 -7.5; 2457 -6.6; 2703 -5.7; 2973 -4.6; 3270 -4.5; 3597 -4.9; 3957 -5.1; 4353 -5.2; 4788 -3.5; 5267 -0.5; 5793 -4.2; 6373 -5.5; 7010 -4.2; 7711 -5.9; 8482 -9.3; 9330 -11.0; 10263 -8.9; 11289 -7.2; 12418 -6.8; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K167 Tiesto GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K167 Tiesto ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.88 | 3.9 dB  |
| Peaking | 84 Hz   | 0.37 | 2.9 dB  |
| Peaking | 1676 Hz | 1.08 | -6.5 dB |
| Peaking | 4419 Hz | 0.48 | 3.8 dB  |
| Peaking | 9298 Hz | 2.59 | -6.8 dB |
| Peaking | 271 Hz  | 2.23 | 1.3 dB  |
| Peaking | 362 Hz  | 0.67 | -0.6 dB |
| Peaking | 2903 Hz | 2.57 | 1.3 dB  |
| Peaking | 4634 Hz | 1.99 | -2.9 dB |
| Peaking | 5173 Hz | 7.1  | 5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | 1.8 dB  |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K167%20Tiesto/AKG%20K167%20Tiesto.png)