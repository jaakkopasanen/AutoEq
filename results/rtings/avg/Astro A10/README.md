# Astro A10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.0; 31 -1.8; 34 -2.5; 37 -3.1; 41 -3.7; 45 -4.3; 49 -4.7; 54 -5.1; 60 -5.5; 66 -5.8; 72 -6.0; 79 -6.1; 87 -6.2; 96 -6.1; 106 -6.0; 116 -5.8; 128 -5.6; 141 -5.2; 155 -4.8; 170 -4.4; 187 -3.8; 206 -3.2; 227 -2.8; 249 -3.0; 274 -2.8; 302 -3.0; 332 -2.0; 365 -1.6; 402 -1.2; 442 -0.8; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -2.3; 947 -5.2; 1042 -7.1; 1146 -7.6; 1261 -7.0; 1387 -6.4; 1526 -4.9; 1678 -3.6; 1846 -2.2; 2031 -0.6; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -1.8; 6373 -3.9; 7010 -5.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astro A10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astro A10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 1.29 | 6.3 dB   |
| Peaking | 792 Hz  | 5.11 | 1.8 dB   |
| Peaking | 1065 Hz | 0.34 | 10.5 dB  |
| Peaking | 1159 Hz | 1.37 | -12.3 dB |
| Peaking | 4424 Hz | 1.69 | 3.3 dB   |
| Peaking | 95 Hz   | 2.33 | -0.8 dB  |
| Peaking | 1609 Hz | 3.27 | -1.7 dB  |
| Peaking | 2189 Hz | 1.1  | 1.4 dB   |
| Peaking | 5597 Hz | 2.52 | 3.2 dB   |
| Peaking | 6414 Hz | 0.86 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 7.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Astro%20A10/Astro%20A10.png)