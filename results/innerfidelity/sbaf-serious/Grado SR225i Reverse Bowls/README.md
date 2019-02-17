# Grado SR225i Reverse Bowls
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.4; 45 -2.6; 49 -3.5; 54 -4.6; 60 -5.5; 66 -6.3; 72 -7.0; 79 -7.7; 87 -8.2; 96 -8.6; 106 -8.8; 116 -8.9; 128 -9.0; 141 -9.0; 155 -8.9; 170 -8.8; 187 -8.6; 206 -8.4; 227 -8.2; 249 -8.0; 274 -7.6; 302 -7.6; 332 -7.6; 365 -7.2; 402 -7.2; 442 -7.0; 486 -6.9; 535 -6.8; 588 -6.3; 647 -6.3; 712 -6.4; 783 -6.1; 861 -6.4; 947 -6.5; 1042 -6.5; 1146 -6.7; 1261 -7.2; 1387 -8.1; 1526 -9.1; 1678 -9.8; 1846 -11.2; 2031 -14.3; 2234 -13.2; 2457 -10.3; 2703 -8.2; 2973 -7.4; 3270 -6.1; 3597 -7.4; 3957 -6.1; 4353 -4.2; 4788 -4.4; 5267 -6.1; 5793 -4.5; 6373 -6.3; 7010 -10.1; 7711 -11.0; 8482 -12.0; 9330 -12.6; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i Reverse Bowls GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i Reverse Bowls ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.58 | 7.6 dB  |
| Peaking | 95 Hz    | 0.56 | -4.4 dB |
| Peaking | 2081 Hz  | 3.04 | -8.2 dB |
| Peaking | 5055 Hz  | 1.5  | 2.8 dB  |
| Peaking | 8442 Hz  | 2.34 | -6.9 dB |
| Peaking | 844 Hz   | 1.46 | 0.6 dB  |
| Peaking | 1509 Hz  | 6.82 | -1.1 dB |
| Peaking | 9555 Hz  | 6.87 | -3.1 dB |
| Peaking | 10626 Hz | 2.68 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20Reverse%20Bowls/Grado%20SR225i%20Reverse%20Bowls.png)