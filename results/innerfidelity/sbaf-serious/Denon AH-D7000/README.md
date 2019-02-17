# Denon AH-D7000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.4; 34 -2.4; 37 -3.3; 41 -4.0; 45 -4.3; 49 -4.5; 54 -4.9; 60 -4.9; 66 -4.9; 72 -5.1; 79 -5.1; 87 -5.2; 96 -5.2; 106 -5.0; 116 -4.9; 128 -4.9; 141 -4.9; 155 -4.9; 170 -4.5; 187 -4.4; 206 -4.2; 227 -3.7; 249 -3.3; 274 -2.8; 302 -2.3; 332 -1.9; 365 -1.5; 402 -1.9; 442 -2.3; 486 -3.8; 535 -5.2; 588 -6.0; 647 -6.5; 712 -7.2; 783 -7.1; 861 -6.0; 947 -6.1; 1042 -6.6; 1146 -6.0; 1261 -5.5; 1387 -5.4; 1526 -5.2; 1678 -4.8; 1846 -4.2; 2031 -3.9; 2234 -3.6; 2457 -2.7; 2703 -2.0; 2973 -1.7; 3270 -2.1; 3597 -3.0; 3957 -4.1; 4353 -6.9; 4788 -5.8; 5267 -4.7; 5793 -5.7; 6373 -6.5; 7010 -6.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -8.1; 11289 -7.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.77 | 6.2 dB  |
| Peaking | 232 Hz   | 1.03 | 2.3 dB  |
| Peaking | 376 Hz   | 2.46 | 4.1 dB  |
| Peaking | 2019 Hz  | 2.09 | 1.6 dB  |
| Peaking | 3011 Hz  | 2.22 | 4.7 dB  |
| Peaking | 455 Hz   | 7.73 | 1.0 dB  |
| Peaking | 704 Hz   | 3.64 | -1.5 dB |
| Peaking | 4452 Hz  | 6.66 | -3.8 dB |
| Peaking | 4557 Hz  | 2.73 | 2.0 dB  |
| Peaking | 10728 Hz | 6.07 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 3.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D7000/Denon%20AH-D7000.png)