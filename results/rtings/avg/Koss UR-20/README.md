# Koss UR-20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.3; 25 -4.7; 28 -5.2; 31 -5.5; 34 -5.6; 37 -5.6; 41 -5.5; 45 -5.5; 49 -5.6; 54 -5.7; 60 -6.0; 66 -6.2; 72 -6.5; 79 -6.6; 87 -6.9; 96 -7.4; 106 -7.9; 116 -8.3; 128 -8.8; 141 -9.0; 155 -9.2; 170 -9.2; 187 -9.2; 206 -9.1; 227 -8.9; 249 -8.5; 274 -8.7; 302 -8.9; 332 -9.3; 365 -9.8; 402 -10.3; 442 -10.7; 486 -10.9; 535 -10.3; 588 -9.8; 647 -9.5; 712 -8.7; 783 -7.5; 861 -6.1; 947 -6.9; 1042 -5.7; 1146 -3.4; 1261 -1.0; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.6; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -2.6; 3957 -8.4; 4353 -9.7; 4788 -7.4; 5267 -6.3; 5793 -9.3; 6373 -10.3; 7010 -9.2; 7711 -13.0; 8482 -15.2; 9330 -10.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss UR-20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss UR-20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 153 Hz   | 1.23 | -2.5 dB |
| Peaking | 523 Hz   | 0.9  | -4.9 dB |
| Peaking | 1849 Hz  | 0.85 | 7.6 dB  |
| Peaking | 8034 Hz  | 2.35 | -8.4 dB |
| Peaking | 1299 Hz  | 9.67 | 1.8 dB  |
| Peaking | 3373 Hz  | 3.75 | 4.7 dB  |
| Peaking | 4140 Hz  | 4.15 | -6.3 dB |
| Peaking | 10327 Hz | 5.33 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -4.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB |
| Peaking | 16000 Hz | 1.41 | 1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20UR-20/Koss%20UR-20.png)