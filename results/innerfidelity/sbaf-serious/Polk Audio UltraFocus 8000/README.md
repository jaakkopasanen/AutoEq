# Polk Audio UltraFocus 8000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.2; 23 -12.1; 25 -12.0; 28 -11.7; 31 -11.4; 34 -11.0; 37 -10.5; 41 -10.1; 45 -9.7; 49 -9.4; 54 -9.0; 60 -8.5; 66 -8.2; 72 -8.0; 79 -8.0; 87 -8.0; 96 -8.0; 106 -7.8; 116 -7.6; 128 -7.6; 141 -7.5; 155 -7.3; 170 -7.0; 187 -7.2; 206 -7.2; 227 -7.1; 249 -7.2; 274 -7.3; 302 -7.4; 332 -7.5; 365 -7.3; 402 -7.6; 442 -7.6; 486 -7.9; 535 -7.6; 588 -7.3; 647 -7.3; 712 -7.6; 783 -7.4; 861 -7.9; 947 -8.6; 1042 -9.2; 1146 -8.7; 1261 -8.3; 1387 -7.9; 1526 -7.4; 1678 -6.9; 1846 -6.1; 2031 -5.8; 2234 -5.1; 2457 -3.5; 2703 -2.4; 2973 -1.0; 3270 -0.9; 3597 -0.7; 3957 -2.0; 4353 -3.6; 4788 -6.7; 5267 -4.5; 5793 -1.6; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -6.0; 9330 -7.4; 10263 -6.4; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFocus 8000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFocus 8000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 15 Hz   |  0.34 | -6.8 dB |
| Peaking | 382 Hz  |  0.37 | -1.3 dB |
| Peaking | 1145 Hz |  1.64 | -2.5 dB |
| Peaking | 3231 Hz |  2.19 | 6.0 dB  |
| Peaking | 6249 Hz |  6.02 | 5.9 dB  |
| Peaking | 4188 Hz |  6.53 | 3.1 dB  |
| Peaking | 4656 Hz |  5.27 | -4.1 dB |
| Peaking | 6069 Hz |  3.49 | 1.8 dB  |
| Peaking | 6191 Hz | 13.24 | -2.0 dB |
| Peaking | 9378 Hz |  4.39 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFocus%208000/Polk%20Audio%20UltraFocus%208000.png)