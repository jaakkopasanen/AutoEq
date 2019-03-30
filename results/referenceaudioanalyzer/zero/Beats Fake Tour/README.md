# Beats Fake Tour
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.7; 25 -4.5; 28 -5.5; 31 -6.3; 34 -6.9; 37 -7.4; 41 -8.0; 45 -8.4; 49 -8.8; 54 -9.1; 60 -9.4; 66 -9.5; 72 -9.7; 79 -9.8; 87 -9.8; 96 -9.8; 106 -9.8; 116 -9.8; 128 -9.7; 141 -9.5; 155 -9.4; 170 -9.2; 187 -9.1; 206 -8.7; 227 -8.4; 249 -8.7; 274 -9.0; 302 -8.9; 332 -8.7; 365 -8.5; 402 -8.2; 442 -7.9; 486 -7.4; 535 -6.8; 588 -6.1; 647 -5.3; 712 -4.4; 783 -3.5; 861 -2.7; 947 -1.8; 1042 -0.9; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.8; 2234 -2.8; 2457 -5.3; 2703 -7.3; 2973 -8.4; 3270 -9.5; 3597 -10.6; 3957 -11.2; 4353 -11.6; 4788 -12.8; 5267 -14.9; 5793 -15.6; 6373 -13.5; 7010 -7.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.6; 11289 -9.7; 12418 -9.3; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Fake Tour GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Fake Tour ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.22 | 5.3 dB  |
| Peaking | 85 Hz    | 0.42 | -3.5 dB |
| Peaking | 382 Hz   | 1.16 | -2.1 dB |
| Peaking | 1383 Hz  | 0.87 | 7.4 dB  |
| Peaking | 4973 Hz  | 1.37 | -8.8 dB |
| Peaking | 2065 Hz  | 3.66 | 3.2 dB  |
| Peaking | 3110 Hz  | 1.04 | -4.2 dB |
| Peaking | 5947 Hz  | 0.87 | 7.1 dB  |
| Peaking | 5953 Hz  | 3.35 | -9.1 dB |
| Peaking | 11702 Hz | 3.38 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -8.4 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beats%20Fake%20Tour/Beats%20Fake%20Tour.png)