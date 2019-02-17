# Koss SP540
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.5; 25 -11.7; 28 -12.0; 31 -12.3; 34 -12.4; 37 -12.6; 41 -12.8; 45 -12.9; 49 -13.0; 54 -13.1; 60 -13.3; 66 -13.5; 72 -13.6; 79 -13.8; 87 -14.0; 96 -14.2; 106 -14.2; 116 -14.1; 128 -14.0; 141 -14.0; 155 -14.4; 170 -13.7; 187 -13.1; 206 -13.0; 227 -13.1; 249 -13.4; 274 -12.7; 302 -11.4; 332 -11.8; 365 -10.6; 402 -9.0; 442 -8.1; 486 -7.4; 535 -6.5; 588 -5.3; 647 -5.0; 712 -4.6; 783 -3.9; 861 -3.4; 947 -2.7; 1042 -1.8; 1146 -0.9; 1261 -0.8; 1387 -1.2; 1526 -2.2; 1678 -3.5; 1846 -4.4; 2031 -5.2; 2234 -6.6; 2457 -7.7; 2703 -8.8; 2973 -9.4; 3270 -9.7; 3597 -8.4; 3957 -6.6; 4353 -3.8; 4788 -0.5; 5267 -4.7; 5793 -2.4; 6373 -1.1; 7010 -3.5; 7711 -4.1; 8482 -4.0; 9330 -3.8; 10263 -2.2; 11289 -2.2; 12418 -2.2; 13660 -2.2; 15026 -2.2; 16529 -4.0; 18182 -4.7; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss SP540 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss SP540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.32 | -9.1 dB |
| Peaking | 141 Hz  | 0.64 | -7.0 dB |
| Peaking | 309 Hz  | 1.18 | -5.6 dB |
| Peaking | 3019 Hz | 2.08 | -8.1 dB |
| Peaking | 1258 Hz | 2.82 | 2.8 dB  |
| Peaking | 1890 Hz | 3.7  | -0.9 dB |
| Peaking | 2286 Hz | 6.03 | -1.1 dB |
| Peaking | 6578 Hz | 2.15 | 3.1 dB  |
| Peaking | 7653 Hz | 2.32 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.8 dB |
| Peaking | 62 Hz    | 1.41 | -8.2 dB |
| Peaking | 125 Hz   | 1.41 | -9.3 dB |
| Peaking | 250 Hz   | 1.41 | -9.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | -3.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20SP540/Koss%20SP540.png)