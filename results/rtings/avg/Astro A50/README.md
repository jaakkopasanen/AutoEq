# Astro A50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.0; 25 -1.4; 28 -1.8; 31 -2.1; 34 -2.4; 37 -2.6; 41 -2.9; 45 -3.2; 49 -3.5; 54 -3.8; 60 -4.1; 66 -4.5; 72 -4.8; 79 -5.1; 87 -5.4; 96 -5.7; 106 -5.9; 116 -6.1; 128 -6.3; 141 -6.4; 155 -6.4; 170 -6.4; 187 -6.2; 206 -6.0; 227 -5.7; 249 -5.7; 274 -5.7; 302 -5.6; 332 -5.4; 365 -5.0; 402 -4.3; 442 -3.5; 486 -3.1; 535 -2.4; 588 -1.0; 647 -0.5; 712 -1.8; 783 -2.5; 861 -2.8; 947 -4.9; 1042 -5.7; 1146 -5.6; 1261 -5.4; 1387 -4.9; 1526 -4.4; 1678 -3.9; 1846 -3.6; 2031 -3.7; 2234 -3.4; 2457 -2.7; 2703 -2.0; 2973 -2.1; 3270 -2.1; 3597 -1.8; 3957 -1.4; 4353 -1.3; 4788 -3.0; 5267 -5.6; 5793 -5.1; 6373 -8.6; 7010 -9.1; 7711 -7.8; 8482 -6.4; 9330 -4.5; 10263 -4.4; 11289 -5.5; 12418 -8.2; 13660 -7.3; 15026 -4.6; 16529 -4.4; 18182 -4.5; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astro A50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astro A50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.68 | 3.8 dB  |
| Peaking | 630 Hz   | 3.86 | 4.3 dB  |
| Peaking | 3781 Hz  | 1.4  | 3.5 dB  |
| Peaking | 6826 Hz  | 2.83 | -5.7 dB |
| Peaking | 13029 Hz | 3.84 | -4.2 dB |
| Peaking | 44 Hz    | 1.29 | 1.2 dB  |
| Peaking | 155 Hz   | 0.62 | -2.1 dB |
| Peaking | 949 Hz   | 0.87 | 1.9 dB  |
| Peaking | 1118 Hz  | 2.17 | -3.4 dB |
| Peaking | 9955 Hz  | 6.66 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Astro%20A50/Astro%20A50.png)