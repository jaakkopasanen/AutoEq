# Sunrise Feeling 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.6; 141 -1.2; 155 -1.7; 170 -2.3; 187 -2.8; 206 -3.3; 227 -3.8; 249 -4.2; 274 -4.6; 302 -4.9; 332 -5.3; 365 -5.7; 402 -6.0; 442 -6.2; 486 -6.0; 535 -5.7; 588 -5.3; 647 -5.2; 712 -5.5; 783 -6.3; 861 -7.2; 947 -8.2; 1042 -9.1; 1146 -10.0; 1261 -10.9; 1387 -11.6; 1526 -12.2; 1678 -12.4; 1846 -12.4; 2031 -12.3; 2234 -12.0; 2457 -11.5; 2703 -10.6; 2973 -9.3; 3270 -7.8; 3597 -6.3; 3957 -5.3; 4353 -5.1; 4788 -6.0; 5267 -8.4; 5793 -11.5; 6373 -11.9; 7010 -8.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sunrise Feeling 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sunrise Feeling 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 52 Hz    | 0.24 | 6.5 dB  |
| Peaking | 727 Hz   | 1.84 | 3.2 dB  |
| Peaking | 2264 Hz  | 0.51 | -9.3 dB |
| Peaking | 4321 Hz  | 0.8  | 8.7 dB  |
| Peaking | 5996 Hz  | 3.1  | -8.7 dB |
| Peaking | 17 Hz    | 0.97 | 1.3 dB  |
| Peaking | 46 Hz    | 0.77 | -0.7 dB |
| Peaking | 123 Hz   | 2.43 | 1.0 dB  |
| Peaking | 334 Hz   | 1.8  | -0.5 dB |
| Peaking | 11351 Hz | 2.69 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 5.2 dB  |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -7.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sunrise%20Feeling%202/Sunrise%20Feeling%202.png)