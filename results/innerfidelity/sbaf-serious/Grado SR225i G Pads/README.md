# Grado SR225i G Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.9; 37 -1.6; 41 -2.7; 45 -3.3; 49 -3.8; 54 -4.9; 60 -6.3; 66 -7.3; 72 -7.9; 79 -8.5; 87 -9.0; 96 -9.5; 106 -9.8; 116 -9.8; 128 -9.8; 141 -9.8; 155 -9.7; 170 -9.4; 187 -9.1; 206 -8.9; 227 -8.5; 249 -8.2; 274 -7.8; 302 -7.7; 332 -7.4; 365 -7.2; 402 -7.3; 442 -6.9; 486 -6.9; 535 -6.9; 588 -6.7; 647 -6.5; 712 -6.6; 783 -6.3; 861 -6.5; 947 -6.6; 1042 -6.6; 1146 -6.9; 1261 -7.4; 1387 -8.0; 1526 -8.1; 1678 -8.5; 1846 -8.1; 2031 -8.4; 2234 -7.9; 2457 -8.4; 2703 -8.7; 2973 -9.6; 3270 -9.3; 3597 -11.3; 3957 -10.9; 4353 -9.7; 4788 -11.1; 5267 -14.6; 5793 -15.9; 6373 -17.0; 7010 -15.2; 7711 -14.1; 8482 -15.5; 9330 -16.7; 10263 -13.0; 11289 -7.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i G Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i G Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.57 | 7.2 dB  |
| Peaking | 101 Hz   | 0.6  | -4.9 dB |
| Peaking | 5952 Hz  | 4.45 | -2.0 dB |
| Peaking | 7048 Hz  | 0.88 | -9.1 dB |
| Peaking | 22050 Hz | 2.64 | -6.8 dB |
| Peaking | 1671 Hz  | 2.64 | -1.3 dB |
| Peaking | 7730 Hz  | 4.86 | 2.9 dB  |
| Peaking | 9350 Hz  | 2.16 | -5.2 dB |
| Peaking | 9777 Hz  | 3.82 | -2.6 dB |
| Peaking | 11350 Hz | 1.45 | 5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB   |
| Peaking | 62 Hz    | 1.41 | -1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -10.3 dB |
| Peaking | 16000 Hz | 1.41 | 1.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20G%20Pads/Grado%20SR225i%20G%20Pads.png)