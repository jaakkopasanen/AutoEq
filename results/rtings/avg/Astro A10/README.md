# Astro A10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -4.0; 25 -4.7; 28 -5.7; 31 -6.5; 34 -7.3; 37 -7.8; 41 -8.5; 45 -9.0; 49 -9.4; 54 -9.8; 60 -10.2; 66 -10.5; 72 -10.7; 79 -10.9; 87 -10.9; 96 -10.9; 106 -10.7; 116 -10.6; 128 -10.3; 141 -9.9; 155 -9.6; 170 -9.1; 187 -8.6; 206 -8.0; 227 -7.5; 249 -7.7; 274 -7.5; 302 -7.7; 332 -6.7; 365 -6.3; 402 -5.9; 442 -5.5; 486 -4.8; 535 -2.7; 588 -0.6; 647 -0.5; 712 -0.5; 783 -3.1; 861 -7.0; 947 -10.0; 1042 -11.9; 1146 -12.4; 1261 -11.7; 1387 -11.1; 1526 -9.6; 1678 -8.3; 1846 -7.0; 2031 -5.1; 2234 -5.3; 2457 -4.3; 2703 -4.2; 2973 -4.1; 3270 -3.7; 3597 -2.9; 3957 -1.1; 4353 -0.5; 4788 -0.5; 5267 -5.1; 5793 -6.5; 6373 -8.6; 7010 -9.8; 7711 -9.5; 8482 -9.2; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -9.1; 13660 -10.7; 15026 -10.5; 16529 -7.5; 18182 -6.5; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astro A10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astro A10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 93 Hz    | 0.69 | -4.6 dB |
| Peaking | 669 Hz   | 2.07 | 8.6 dB  |
| Peaking | 1108 Hz  | 1.9  | -8.0 dB |
| Peaking | 4111 Hz  | 1.57 | 7.8 dB  |
| Peaking | 10037 Hz | 0.35 | -3.0 dB |
| Peaking | 20 Hz    | 2.43 | 3.6 dB  |
| Peaking | 4845 Hz  | 9.68 | 3.1 dB  |
| Peaking | 7395 Hz  | 0.99 | -8.4 dB |
| Peaking | 10343 Hz | 0.57 | 9.4 dB  |
| Peaking | 13870 Hz | 1.39 | -7.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 5.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Astro%20A10/Astro%20A10.png)