# Venture Electronics Monk Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.6; 87 -1.7; 96 -3.0; 106 -4.2; 116 -5.3; 128 -6.4; 141 -7.4; 155 -8.3; 170 -8.6; 187 -8.9; 206 -8.6; 227 -8.7; 249 -8.7; 274 -8.5; 302 -8.1; 332 -7.7; 365 -7.3; 402 -9.0; 442 -7.1; 486 -6.8; 535 -6.7; 588 -6.3; 647 -6.2; 712 -6.2; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.3; 1387 -8.4; 1526 -10.0; 1678 -11.5; 1846 -12.9; 2031 -14.0; 2234 -14.7; 2457 -14.0; 2703 -13.0; 2973 -10.6; 3270 -7.9; 3597 -6.5; 3957 -7.2; 4353 -9.3; 4788 -10.8; 5267 -9.2; 5793 -8.5; 6373 -6.2; 7010 -10.9; 7711 -12.4; 8482 -11.2; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.7; 15026 -13.6; 16529 -9.3; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venture Electronics Monk Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venture Electronics Monk Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.75 | 7.3 dB  |
| Peaking | 2209 Hz  | 1.85 | -8.6 dB |
| Peaking | 7787 Hz  | 3.85 | -6.2 dB |
| Peaking | 14641 Hz | 4.76 | -5.4 dB |
| Peaking | 15518 Hz | 3.77 | -4.7 dB |
| Peaking | 22 Hz    | 3.38 | 2.0 dB  |
| Peaking | 81 Hz    | 2.42 | 3.3 dB  |
| Peaking | 191 Hz   | 1.04 | -3.2 dB |
| Peaking | 4376 Hz  | 1.65 | 3.3 dB  |
| Peaking | 4797 Hz  | 3.87 | -6.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 6.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Venture%20Electronics%20Monk%20Plus/Venture%20Electronics%20Monk%20Plus.png)