# Noontec Zoro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.7; 25 -8.0; 28 -8.3; 31 -8.6; 34 -8.9; 37 -9.0; 41 -9.3; 45 -9.4; 49 -9.5; 54 -9.7; 60 -9.9; 66 -10.2; 72 -10.5; 79 -10.8; 87 -11.0; 96 -11.3; 106 -11.6; 116 -11.7; 128 -11.8; 141 -11.9; 155 -12.1; 170 -12.0; 187 -12.0; 206 -12.1; 227 -12.0; 249 -11.9; 274 -11.5; 302 -11.2; 332 -11.2; 365 -11.1; 402 -10.9; 442 -10.6; 486 -10.6; 535 -10.3; 588 -9.8; 647 -9.4; 712 -8.9; 783 -8.1; 861 -7.7; 947 -7.3; 1042 -7.3; 1146 -7.4; 1261 -7.5; 1387 -8.4; 1526 -9.1; 1678 -8.8; 1846 -7.9; 2031 -6.1; 2234 -4.2; 2457 -1.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.4; 6373 -3.0; 7010 -5.0; 7711 -8.8; 8482 -9.6; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 71 Hz    | 0.34 | -1.9 dB |
| Peaking | 269 Hz   | 0.31 | -4.7 dB |
| Peaking | 1706 Hz  | 1.81 | -6.8 dB |
| Peaking | 3285 Hz  | 0.47 | 7.9 dB  |
| Peaking | 8276 Hz  | 2.74 | -6.8 dB |
| Peaking | 2619 Hz  | 6.64 | 1.5 dB  |
| Peaking | 3564 Hz  | 1.26 | -0.7 dB |
| Peaking | 5478 Hz  | 3.86 | 1.4 dB  |
| Peaking | 13020 Hz | 1.66 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro/Noontec%20Zoro.png)