# Koss Tony Bennett
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.4; 31 -2.1; 34 -2.7; 37 -3.2; 41 -3.8; 45 -4.4; 49 -4.8; 54 -5.3; 60 -5.9; 66 -6.3; 72 -6.5; 79 -5.8; 87 -4.7; 96 -5.9; 106 -7.8; 116 -8.6; 128 -9.2; 141 -10.0; 155 -10.4; 170 -10.0; 187 -10.8; 206 -11.0; 227 -10.7; 249 -10.6; 274 -10.0; 302 -9.3; 332 -8.7; 365 -8.3; 402 -8.6; 442 -9.4; 486 -10.3; 535 -10.2; 588 -9.6; 647 -8.9; 712 -8.4; 783 -7.2; 861 -6.2; 947 -5.5; 1042 -6.3; 1146 -5.4; 1261 -4.3; 1387 -4.0; 1526 -4.0; 1678 -4.0; 1846 -3.9; 2031 -3.8; 2234 -4.4; 2457 -4.3; 2703 -4.5; 2973 -4.5; 3270 -5.2; 3597 -2.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Tony Bennett GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Tony Bennett ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.57 | 6.6 dB  |
| Peaking | 193 Hz  | 1.07 | -4.7 dB |
| Peaking | 545 Hz  | 2    | -3.5 dB |
| Peaking | 1575 Hz | 1.18 | 2.6 dB  |
| Peaking | 4890 Hz | 1.65 | 6.8 dB  |
| Peaking | 89 Hz   | 8.81 | 2.2 dB  |
| Peaking | 3924 Hz | 5.48 | 3.8 dB  |
| Peaking | 3954 Hz | 1.93 | -2.0 dB |
| Peaking | 6266 Hz | 5.61 | 2.8 dB  |
| Peaking | 8989 Hz | 2.69 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Tony%20Bennett/Koss%20Tony%20Bennett.png)