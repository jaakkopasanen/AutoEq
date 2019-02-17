# Logitech UE 900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.4; 25 -5.4; 28 -5.5; 31 -5.6; 34 -5.8; 37 -5.9; 41 -6.0; 45 -6.1; 49 -6.3; 54 -6.5; 60 -7.0; 66 -7.3; 72 -7.6; 79 -8.0; 87 -8.4; 96 -8.9; 106 -9.2; 116 -9.4; 128 -9.7; 141 -10.1; 155 -10.3; 170 -10.5; 187 -10.7; 206 -10.8; 227 -10.9; 249 -11.0; 274 -11.0; 302 -11.1; 332 -11.2; 365 -11.3; 402 -11.4; 442 -11.4; 486 -11.6; 535 -11.6; 588 -11.2; 647 -10.5; 712 -9.5; 783 -8.1; 861 -7.2; 947 -6.6; 1042 -6.5; 1146 -6.5; 1261 -6.8; 1387 -7.3; 1526 -7.9; 1678 -8.5; 1846 -8.8; 2031 -8.9; 2234 -8.8; 2457 -7.7; 2703 -5.1; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -1.0; 5267 -0.9; 5793 -0.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.7; 9330 -8.0; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech UE 900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.89 | 1.4 dB  |
| Peaking | 288 Hz  | 0.45 | -5.1 dB |
| Peaking | 2261 Hz | 2.15 | -5.9 dB |
| Peaking | 3329 Hz | 1.33 | 7.8 dB  |
| Peaking | 5796 Hz | 3.28 | 4.5 dB  |
| Peaking | 284 Hz  | 2.11 | 0.8 dB  |
| Peaking | 620 Hz  | 1.45 | -3.0 dB |
| Peaking | 879 Hz  | 1.17 | 2.9 dB  |
| Peaking | 1623 Hz | 3.39 | -1.4 dB |
| Peaking | 9224 Hz | 3.83 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -5.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE%20900/Logitech%20UE%20900.png)