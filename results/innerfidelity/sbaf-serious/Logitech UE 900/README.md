# Logitech UE 900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.6; 25 -4.6; 28 -4.7; 31 -4.8; 34 -4.9; 37 -5.1; 41 -5.2; 45 -5.3; 49 -5.5; 54 -5.7; 60 -6.2; 66 -6.5; 72 -6.8; 79 -7.2; 87 -7.6; 96 -8.0; 106 -8.3; 116 -8.6; 128 -8.9; 141 -9.2; 155 -9.5; 170 -9.7; 187 -9.8; 206 -10.0; 227 -10.0; 249 -10.2; 274 -10.2; 302 -10.3; 332 -10.4; 365 -10.5; 402 -10.6; 442 -10.6; 486 -10.8; 535 -10.8; 588 -10.4; 647 -9.7; 712 -8.7; 783 -7.3; 861 -6.3; 947 -5.8; 1042 -5.7; 1146 -5.7; 1261 -6.0; 1387 -6.5; 1526 -7.1; 1678 -7.7; 1846 -8.0; 2031 -8.1; 2234 -8.0; 2457 -6.9; 2703 -4.3; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech UE 900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.54 | 2.2 dB  |
| Peaking | 466 Hz  | 0.26 | -4.7 dB |
| Peaking | 1002 Hz | 1.65 | 4.5 dB  |
| Peaking | 2199 Hz | 2.68 | -4.0 dB |
| Peaking | 3824 Hz | 0.92 | 8.0 dB  |
| Peaking | 285 Hz  | 3.75 | 0.4 dB  |
| Peaking | 3031 Hz | 6.83 | 2.4 dB  |
| Peaking | 3789 Hz | 1.41 | -1.2 dB |
| Peaking | 6222 Hz | 2.26 | 5.3 dB  |
| Peaking | 7539 Hz | 1.41 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -4.5 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE%20900/Logitech%20UE%20900.png)