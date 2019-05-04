# Grado SR80e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.8; 49 -1.4; 54 -2.1; 60 -2.8; 66 -3.4; 72 -3.8; 79 -4.1; 87 -4.5; 96 -4.8; 106 -5.0; 116 -5.2; 128 -5.3; 141 -5.3; 155 -5.3; 170 -5.2; 187 -5.1; 206 -4.9; 227 -4.8; 249 -4.7; 274 -4.7; 302 -4.8; 332 -4.9; 365 -4.8; 402 -4.8; 442 -4.9; 486 -5.0; 535 -4.9; 588 -4.7; 647 -4.6; 712 -4.4; 783 -4.2; 861 -3.9; 947 -3.9; 1042 -3.9; 1146 -4.0; 1261 -4.3; 1387 -4.8; 1526 -5.6; 1678 -7.0; 1846 -11.1; 2031 -13.6; 2234 -12.8; 2457 -11.1; 2703 -9.1; 2973 -7.5; 3270 -6.5; 3597 -7.4; 3957 -9.0; 4353 -6.9; 4788 -5.0; 5267 -6.3; 5793 -6.7; 6373 -8.1; 7010 -11.2; 7711 -11.4; 8482 -11.7; 9330 -10.8; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR80e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR80e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.6  | 6.5 dB   |
| Peaking | 277 Hz   | 1.12 | 1.3 dB   |
| Peaking | 1439 Hz  | 0.63 | 4.4 dB   |
| Peaking | 2097 Hz  | 2.18 | -10.8 dB |
| Peaking | 8120 Hz  | 2.45 | -6.0 dB  |
| Peaking | 3439 Hz  | 5.18 | 1.7 dB   |
| Peaking | 4003 Hz  | 3.55 | -3.6 dB  |
| Peaking | 4641 Hz  | 4.25 | 3.1 dB   |
| Peaking | 9455 Hz  | 6.32 | -1.6 dB  |
| Peaking | 11029 Hz | 2.54 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR80e/Grado%20SR80e.png)