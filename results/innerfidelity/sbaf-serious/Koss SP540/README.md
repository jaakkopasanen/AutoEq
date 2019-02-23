# Koss SP540
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.4; 23 -10.8; 25 -11.1; 28 -11.4; 31 -11.6; 34 -11.8; 37 -11.9; 41 -12.1; 45 -12.2; 49 -12.4; 54 -12.5; 60 -12.6; 66 -12.8; 72 -13.0; 79 -13.1; 87 -13.3; 96 -13.5; 106 -13.5; 116 -13.4; 128 -13.4; 141 -13.3; 155 -13.7; 170 -13.0; 187 -12.5; 206 -12.3; 227 -12.4; 249 -12.7; 274 -12.0; 302 -10.7; 332 -11.1; 365 -9.9; 402 -8.4; 442 -7.4; 486 -6.7; 535 -5.8; 588 -4.7; 647 -4.3; 712 -3.9; 783 -3.3; 861 -2.7; 947 -2.0; 1042 -1.1; 1146 -0.5; 1261 -0.5; 1387 -0.6; 1526 -1.5; 1678 -2.8; 1846 -3.8; 2031 -4.6; 2234 -5.9; 2457 -7.0; 2703 -8.1; 2973 -8.8; 3270 -9.1; 3597 -7.7; 3957 -5.9; 4353 -3.1; 4788 -0.5; 5267 -4.0; 5793 -1.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss SP540 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss SP540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.38 | -5.2 dB |
| Peaking | 138 Hz  | 0.85 | -4.2 dB |
| Peaking | 274 Hz  | 1.74 | -3.5 dB |
| Peaking | 1130 Hz | 1.31 | 6.6 dB  |
| Peaking | 5871 Hz | 2.67 | 5.2 dB  |
| Peaking | 606 Hz  | 4.86 | 1.3 dB  |
| Peaking | 1574 Hz | 3.51 | 1.4 dB  |
| Peaking | 3087 Hz | 2.26 | -3.7 dB |
| Peaking | 4647 Hz | 7.09 | 4.8 dB  |
| Peaking | 8239 Hz | 4.18 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20SP540/Koss%20SP540.png)