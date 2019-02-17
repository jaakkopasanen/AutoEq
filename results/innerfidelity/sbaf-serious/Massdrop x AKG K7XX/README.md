# Massdrop x AKG K7XX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.9; 25 -4.3; 28 -4.8; 31 -5.2; 34 -5.6; 37 -5.9; 41 -6.2; 45 -6.4; 49 -6.7; 54 -6.9; 60 -7.2; 66 -7.5; 72 -7.7; 79 -8.1; 87 -8.4; 96 -8.8; 106 -8.9; 116 -9.1; 128 -9.3; 141 -9.3; 155 -9.4; 170 -9.5; 187 -9.1; 206 -9.1; 227 -9.2; 249 -9.0; 274 -9.0; 302 -8.9; 332 -8.7; 365 -8.3; 402 -8.0; 442 -7.5; 486 -7.1; 535 -6.7; 588 -5.8; 647 -5.2; 712 -4.6; 783 -3.8; 861 -3.4; 947 -3.8; 1042 -4.0; 1146 -4.6; 1261 -5.1; 1387 -6.1; 1526 -7.6; 1678 -9.1; 1846 -9.6; 2031 -9.6; 2234 -8.5; 2457 -5.4; 2703 -2.7; 2973 -0.5; 3270 -0.5; 3597 -2.2; 3957 -4.1; 4353 -5.3; 4788 -4.7; 5267 -2.6; 5793 -2.5; 6373 -4.0; 7010 -6.7; 7711 -7.2; 8482 -8.6; 9330 -7.5; 10263 -4.1; 11289 -4.0; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -4.7; 18182 -7.9; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x AKG K7XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x AKG K7XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 124 Hz   | 0.52 | -5.0 dB |
| Peaking | 329 Hz   | 1.34 | -2.8 dB |
| Peaking | 1943 Hz  | 2.38 | -6.6 dB |
| Peaking | 3050 Hz  | 3.44 | 5.3 dB  |
| Peaking | 8473 Hz  | 3.74 | -5.1 dB |
| Peaking | 14 Hz    | 2.28 | 1.2 dB  |
| Peaking | 875 Hz   | 3.59 | 1.7 dB  |
| Peaking | 4469 Hz  | 5.7  | -1.9 dB |
| Peaking | 5531 Hz  | 6.33 | 2.7 dB  |
| Peaking | 18151 Hz | 2.18 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20AKG%20K7XX/Massdrop%20x%20AKG%20K7XX.png)