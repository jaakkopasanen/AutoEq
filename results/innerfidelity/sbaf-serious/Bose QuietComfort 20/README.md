# Bose QuietComfort 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -3.4; 25 -4.5; 28 -5.5; 31 -6.0; 34 -6.1; 37 -6.1; 41 -5.9; 45 -5.7; 49 -5.5; 54 -5.4; 60 -5.5; 66 -5.7; 72 -6.1; 79 -6.6; 87 -7.2; 96 -7.7; 106 -8.1; 116 -8.1; 128 -8.1; 141 -8.1; 155 -8.0; 170 -8.0; 187 -8.0; 206 -8.1; 227 -7.9; 249 -7.8; 274 -7.6; 302 -7.5; 332 -7.4; 365 -7.4; 402 -7.4; 442 -7.3; 486 -7.3; 535 -7.0; 588 -6.4; 647 -6.3; 712 -6.4; 783 -5.8; 861 -5.2; 947 -5.0; 1042 -5.5; 1146 -6.3; 1261 -7.3; 1387 -8.9; 1526 -10.6; 1678 -11.2; 1846 -10.0; 2031 -8.7; 2234 -7.7; 2457 -6.8; 2703 -6.1; 2973 -4.3; 3270 -2.9; 3597 -3.3; 3957 -5.8; 4353 -7.7; 4788 -4.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -5.7; 7711 -7.6; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 1.53 | 8.4 dB  |
| Peaking | 168 Hz  | 0.85 | -1.9 dB |
| Peaking | 1680 Hz | 3.39 | -5.2 dB |
| Peaking | 3302 Hz | 5.61 | 4.0 dB  |
| Peaking | 5742 Hz | 4.05 | 7.1 dB  |
| Peaking | 58 Hz   | 3.33 | 1.3 dB  |
| Peaking | 935 Hz  | 2.1  | 2.5 dB  |
| Peaking | 2623 Hz | 0.17 | -0.8 dB |
| Peaking | 4275 Hz | 5.74 | -6.0 dB |
| Peaking | 4439 Hz | 1.9  | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)