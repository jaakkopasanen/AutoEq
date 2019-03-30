# Yamaha RH-5Ma
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.7; 25 -9.1; 28 -9.6; 31 -9.9; 34 -10.2; 37 -10.4; 41 -10.7; 45 -10.8; 49 -10.9; 54 -10.9; 60 -11.1; 66 -11.2; 72 -11.2; 79 -11.0; 87 -10.9; 96 -10.8; 106 -10.6; 116 -10.6; 128 -10.4; 141 -10.3; 155 -10.1; 170 -9.9; 187 -9.7; 206 -9.4; 227 -8.6; 249 -7.5; 274 -6.6; 302 -6.6; 332 -6.7; 365 -6.7; 402 -6.5; 442 -6.2; 486 -5.6; 535 -4.7; 588 -3.8; 647 -2.9; 712 -2.0; 783 -1.2; 861 -0.7; 947 -0.5; 1042 -0.7; 1146 -1.3; 1261 -2.3; 1387 -3.2; 1526 -3.9; 1678 -4.1; 1846 -3.8; 2031 -3.2; 2234 -2.6; 2457 -2.1; 2703 -2.7; 2973 -4.0; 3270 -5.4; 3597 -5.4; 3957 -2.7; 4353 -3.1; 4788 -8.3; 5267 -8.8; 5793 -5.5; 6373 -3.1; 7010 -3.7; 7711 -4.8; 8482 -5.0; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha RH-5Ma GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha RH-5Ma ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.55 | -4.2 dB |
| Peaking | 128 Hz  | 0.5  | -4.3 dB |
| Peaking | 914 Hz  | 1.45 | 5.1 dB  |
| Peaking | 2450 Hz | 3.25 | 2.7 dB  |
| Peaking | 5100 Hz | 9.19 | -5.0 dB |
| Peaking | 278 Hz  | 6.57 | 1.2 dB  |
| Peaking | 432 Hz  | 4.26 | -0.8 dB |
| Peaking | 4158 Hz | 6.8  | 6.2 dB  |
| Peaking | 4281 Hz | 2.04 | -2.7 dB |
| Peaking | 6501 Hz | 4.95 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Yamaha%20RH-5Ma/Yamaha%20RH-5Ma.png)