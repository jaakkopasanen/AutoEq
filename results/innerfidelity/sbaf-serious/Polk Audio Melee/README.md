# Polk Audio Melee
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.1; 25 -8.4; 28 -8.7; 31 -8.9; 34 -9.1; 37 -9.2; 41 -9.3; 45 -9.4; 49 -9.5; 54 -9.6; 60 -9.7; 66 -9.6; 72 -9.5; 79 -9.5; 87 -10.3; 96 -11.1; 106 -10.6; 116 -10.4; 128 -11.1; 141 -12.1; 155 -11.8; 170 -11.1; 187 -12.0; 206 -11.8; 227 -11.4; 249 -11.0; 274 -10.3; 302 -9.7; 332 -9.7; 365 -9.5; 402 -8.9; 442 -8.4; 486 -8.2; 535 -7.9; 588 -7.3; 647 -7.1; 712 -7.1; 783 -6.9; 861 -6.8; 947 -6.6; 1042 -6.4; 1146 -6.0; 1261 -5.6; 1387 -5.5; 1526 -5.1; 1678 -4.2; 1846 -2.7; 2031 -1.2; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.4; 3957 -3.0; 4353 -3.0; 4788 -2.6; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio Melee GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio Melee ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.81 | -1.4 dB |
| Peaking | 130 Hz  | 0.25 | -1.8 dB |
| Peaking | 179 Hz  | 0.76 | -3.5 dB |
| Peaking | 2646 Hz | 1.21 | 6.6 dB  |
| Peaking | 5759 Hz | 3.18 | 5.5 dB  |
| Peaking | 1607 Hz | 1.96 | -1.7 dB |
| Peaking | 2252 Hz | 1.31 | 2.6 dB  |
| Peaking | 2570 Hz | 3.33 | -2.6 dB |
| Peaking | 6600 Hz | 7.07 | 2.4 dB  |
| Peaking | 7496 Hz | 1.7  | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20Melee/Polk%20Audio%20Melee.png)