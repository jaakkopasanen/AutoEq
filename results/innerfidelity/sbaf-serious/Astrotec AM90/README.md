# Astrotec AM90
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.4; 25 -3.5; 28 -3.5; 31 -3.6; 34 -3.7; 37 -3.9; 41 -4.0; 45 -4.2; 49 -4.3; 54 -4.5; 60 -4.8; 66 -5.2; 72 -5.5; 79 -5.9; 87 -6.4; 96 -6.9; 106 -7.1; 116 -7.3; 128 -7.7; 141 -7.9; 155 -8.2; 170 -8.3; 187 -8.5; 206 -8.5; 227 -8.5; 249 -8.6; 274 -8.4; 302 -8.4; 332 -8.2; 365 -8.1; 402 -7.9; 442 -7.5; 486 -7.4; 535 -7.2; 588 -6.6; 647 -6.4; 712 -6.3; 783 -5.8; 861 -6.0; 947 -6.2; 1042 -6.6; 1146 -6.9; 1261 -7.0; 1387 -6.8; 1526 -5.9; 1678 -5.8; 1846 -6.1; 2031 -6.2; 2234 -6.8; 2457 -7.7; 2703 -9.5; 2973 -7.5; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astrotec AM90 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AM90 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.67 | 3.1 dB  |
| Peaking | 54 Hz   | 1.36 | 1.2 dB  |
| Peaking | 213 Hz  | 0.7  | -2.3 dB |
| Peaking | 2732 Hz | 4.43 | -6.7 dB |
| Peaking | 4273 Hz | 1.16 | 7.4 dB  |
| Peaking | 1277 Hz | 7.31 | -1.0 dB |
| Peaking | 3416 Hz | 7.22 | 3.0 dB  |
| Peaking | 4175 Hz | 1.38 | -1.3 dB |
| Peaking | 6218 Hz | 2.59 | 5.2 dB  |
| Peaking | 7488 Hz | 1.65 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AM90/Astrotec%20AM90.png)