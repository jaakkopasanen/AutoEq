# Grado SR225i Goo Bowl
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.2; 54 -1.9; 60 -3.0; 66 -3.9; 72 -4.7; 79 -5.3; 87 -5.8; 96 -6.2; 106 -6.5; 116 -6.5; 128 -6.7; 141 -6.6; 155 -6.6; 170 -6.4; 187 -6.1; 206 -5.9; 227 -5.6; 249 -5.3; 274 -4.9; 302 -5.0; 332 -5.0; 365 -4.6; 402 -4.7; 442 -4.5; 486 -4.5; 535 -4.4; 588 -4.0; 647 -4.0; 712 -4.0; 783 -3.9; 861 -4.1; 947 -4.3; 1042 -4.5; 1146 -4.8; 1261 -5.3; 1387 -6.3; 1526 -7.3; 1678 -8.2; 1846 -10.2; 2031 -12.6; 2234 -11.5; 2457 -9.0; 2703 -7.3; 2973 -6.9; 3270 -5.7; 3597 -7.2; 3957 -6.1; 4353 -4.5; 4788 -4.9; 5267 -6.8; 5793 -5.1; 6373 -6.1; 7010 -9.1; 7711 -10.5; 8482 -12.2; 9330 -13.4; 10263 -8.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i Goo Bowl GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i Goo Bowl ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.9  | 7.0 dB  |
| Peaking | 717 Hz   | 0.66 | 2.7 dB  |
| Peaking | 2054 Hz  | 3.1  | -7.1 dB |
| Peaking | 4612 Hz  | 2.45 | 2.0 dB  |
| Peaking | 8858 Hz  | 3.17 | -7.4 dB |
| Peaking | 52 Hz    | 3.35 | 1.5 dB  |
| Peaking | 112 Hz   | 1.61 | -1.2 dB |
| Peaking | 6144 Hz  | 8.01 | 1.9 dB  |
| Peaking | 7213 Hz  | 5.88 | -1.6 dB |
| Peaking | 11135 Hz | 5.72 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20Goo%20Bowl/Grado%20SR225i%20Goo%20Bowl.png)