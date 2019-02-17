# Campfire Audio Comet
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -2.7; 25 -2.9; 28 -3.1; 31 -3.3; 34 -3.4; 37 -3.5; 41 -3.7; 45 -3.9; 49 -4.1; 54 -4.3; 60 -4.6; 66 -4.9; 72 -5.2; 79 -5.6; 87 -6.1; 96 -6.5; 106 -6.9; 116 -7.3; 128 -7.6; 141 -7.9; 155 -8.1; 170 -8.2; 187 -8.4; 206 -8.4; 227 -8.4; 249 -8.5; 274 -8.8; 302 -9.0; 332 -8.8; 365 -8.6; 402 -8.4; 442 -8.2; 486 -7.9; 535 -7.6; 588 -7.3; 647 -6.9; 712 -6.5; 783 -6.0; 861 -5.7; 947 -5.5; 1042 -5.5; 1146 -5.5; 1261 -5.5; 1387 -5.3; 1526 -4.8; 1678 -4.1; 1846 -3.3; 2031 -2.9; 2234 -2.8; 2457 -3.4; 2703 -4.8; 2973 -6.9; 3270 -7.9; 3597 -6.0; 3957 -3.4; 4353 -1.5; 4788 -0.5; 5267 -0.6; 5793 -1.8; 6373 -4.8; 7010 -8.0; 7711 -7.8; 8482 -6.9; 9330 -6.8; 10263 -6.8; 11289 -5.7; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Comet GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Comet ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.38 | 2.9 dB  |
| Peaking | 242 Hz  | 0.52 | -3.5 dB |
| Peaking | 2016 Hz | 3.12 | 3.1 dB  |
| Peaking | 5221 Hz | 2.71 | 7.1 dB  |
| Peaking | 7270 Hz | 1.61 | -3.5 dB |
| Peaking | 116 Hz  | 3.95 | -0.3 dB |
| Peaking | 2021 Hz | 3.69 | -2.0 dB |
| Peaking | 2396 Hz | 1.48 | 2.6 dB  |
| Peaking | 3194 Hz | 3.2  | -4.7 dB |
| Peaking | 4210 Hz | 5.79 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Campfire%20Audio%20Comet/Campfire%20Audio%20Comet.png)