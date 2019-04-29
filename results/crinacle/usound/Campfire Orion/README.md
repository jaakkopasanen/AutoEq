# Campfire Orion
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.6; 25 -4.7; 28 -4.9; 31 -5.0; 34 -5.1; 37 -5.3; 41 -5.4; 45 -5.6; 49 -5.7; 54 -6.0; 60 -6.2; 66 -6.5; 72 -6.9; 79 -7.2; 87 -7.7; 96 -8.1; 106 -8.6; 116 -8.9; 128 -9.3; 141 -9.6; 155 -9.9; 170 -10.1; 187 -10.2; 206 -10.3; 227 -10.2; 249 -10.2; 274 -10.1; 302 -10.0; 332 -9.8; 365 -9.6; 402 -9.4; 442 -9.1; 486 -8.8; 535 -8.5; 588 -8.1; 647 -7.6; 712 -7.1; 783 -6.5; 861 -6.1; 947 -5.9; 1042 -6.0; 1146 -6.6; 1261 -7.4; 1387 -7.8; 1526 -7.8; 1678 -7.7; 1846 -7.7; 2031 -8.0; 2234 -7.8; 2457 -6.0; 2703 -3.1; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -4.4; 5267 -7.8; 5793 -4.0; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Orion GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Orion ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.33 | 2.1 dB  |
| Peaking | 213 Hz  | 0.55 | -4.1 dB |
| Peaking | 2283 Hz | 1.51 | -7.9 dB |
| Peaking | 2957 Hz | 1.25 | 10.3 dB |
| Peaking | 4158 Hz | 6.42 | 2.5 dB  |
| Peaking | 936 Hz  | 3.21 | 1.4 dB  |
| Peaking | 1388 Hz | 4.66 | -1.0 dB |
| Peaking | 5278 Hz | 6.88 | -5.5 dB |
| Peaking | 6409 Hz | 3.16 | 5.8 dB  |
| Peaking | 7519 Hz | 2.26 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Orion/Campfire%20Orion.png)