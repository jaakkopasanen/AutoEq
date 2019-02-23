# Polk Audio Melee
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.6; 25 -9.0; 28 -9.3; 31 -9.5; 34 -9.7; 37 -9.8; 41 -9.9; 45 -10.0; 49 -10.1; 54 -10.2; 60 -10.2; 66 -10.2; 72 -10.1; 79 -10.1; 87 -10.9; 96 -11.7; 106 -11.2; 116 -10.9; 128 -11.7; 141 -12.7; 155 -12.4; 170 -11.6; 187 -12.6; 206 -12.4; 227 -12.0; 249 -11.6; 274 -10.9; 302 -10.3; 332 -10.3; 365 -10.1; 402 -9.5; 442 -8.9; 486 -8.8; 535 -8.5; 588 -7.9; 647 -7.7; 712 -7.7; 783 -7.5; 861 -7.4; 947 -7.2; 1042 -7.0; 1146 -6.6; 1261 -6.2; 1387 -6.0; 1526 -5.7; 1678 -4.8; 1846 -3.3; 2031 -1.8; 2234 -0.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.1; 3597 -2.0; 3957 -3.6; 4353 -3.6; 4788 -3.2; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio Melee GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio Melee ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.62 | -1.8 dB |
| Peaking | 154 Hz  | 0.03 | -1.0 dB |
| Peaking | 180 Hz  | 0.66 | -4.7 dB |
| Peaking | 2661 Hz | 1.19 | 7.2 dB  |
| Peaking | 5827 Hz | 3.42 | 5.8 dB  |
| Peaking | 1580 Hz | 3.35 | -0.9 dB |
| Peaking | 2114 Hz | 2.69 | 1.1 dB  |
| Peaking | 2604 Hz | 4.54 | -0.9 dB |
| Peaking | 8237 Hz | 3.75 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20Melee/Polk%20Audio%20Melee.png)