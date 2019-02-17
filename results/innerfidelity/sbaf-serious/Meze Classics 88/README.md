# Meze Classics 88
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.1; 25 -2.3; 28 -2.5; 31 -2.7; 34 -2.8; 37 -3.0; 41 -3.1; 45 -3.2; 49 -3.3; 54 -3.4; 60 -3.5; 66 -3.6; 72 -3.7; 79 -4.0; 87 -4.6; 96 -5.2; 106 -5.2; 116 -5.5; 128 -6.0; 141 -6.2; 155 -6.4; 170 -6.2; 187 -6.5; 206 -6.5; 227 -6.3; 249 -5.8; 274 -5.4; 302 -5.3; 332 -5.3; 365 -4.9; 402 -4.4; 442 -3.2; 486 -1.8; 535 -0.5; 588 -0.5; 647 -1.5; 712 -3.2; 783 -4.3; 861 -5.5; 947 -6.5; 1042 -6.0; 1146 -7.6; 1261 -8.3; 1387 -8.4; 1526 -7.7; 1678 -6.2; 1846 -3.9; 2031 -1.9; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze Classics 88 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze Classics 88 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.64 | 4.3 dB  |
| Peaking | 66 Hz   | 1.57 | 1.9 dB  |
| Peaking | 562 Hz  | 2.13 | 6.1 dB  |
| Peaking | 1373 Hz | 1.85 | -5.6 dB |
| Peaking | 3111 Hz | 0.62 | 7.2 dB  |
| Peaking | 1686 Hz | 6.88 | -0.8 dB |
| Peaking | 2168 Hz | 3.84 | 1.4 dB  |
| Peaking | 3270 Hz | 2.16 | -1.1 dB |
| Peaking | 6364 Hz | 2    | 5.6 dB  |
| Peaking | 7258 Hz | 1.37 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 6.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%20Classics%2088/Meze%20Classics%2088.png)