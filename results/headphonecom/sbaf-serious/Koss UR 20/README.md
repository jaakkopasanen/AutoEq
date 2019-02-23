# Koss UR 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.7; 66 -2.3; 72 -2.2; 79 -2.4; 87 -3.2; 96 -4.0; 106 -4.7; 116 -5.2; 128 -5.5; 141 -6.1; 155 -6.5; 170 -6.5; 187 -7.0; 206 -7.3; 227 -7.4; 249 -7.6; 274 -8.7; 302 -9.5; 332 -10.7; 365 -12.0; 402 -13.3; 442 -14.3; 486 -14.8; 535 -15.4; 588 -14.7; 647 -11.7; 712 -8.8; 783 -6.3; 861 -7.9; 947 -6.8; 1042 -4.2; 1146 -1.8; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -1.4; 2031 -5.4; 2234 -6.4; 2457 -3.8; 2703 -3.8; 2973 -0.7; 3270 -0.5; 3597 -1.8; 3957 -5.3; 4353 -4.6; 4788 -6.5; 5267 -5.2; 5793 -9.7; 6373 -8.4; 7010 -7.7; 7711 -8.8; 8482 -9.5; 9330 -8.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss UR 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss UR 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 34 Hz   |  0.5  | 6.6 dB  |
| Peaking | 494 Hz  |  1.33 | -9.6 dB |
| Peaking | 1375 Hz |  1.63 | 7.6 dB  |
| Peaking | 3239 Hz |  3.81 | 6.4 dB  |
| Peaking | 7625 Hz |  1.56 | -2.7 dB |
| Peaking | 769 Hz  |  5.25 | 5.9 dB  |
| Peaking | 799 Hz  |  2.63 | -3.6 dB |
| Peaking | 1982 Hz |  2.75 | 3.1 dB  |
| Peaking | 2109 Hz |  6.47 | -6.0 dB |
| Peaking | 5962 Hz | 16.07 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 4.2 dB   |
| Peaking | 125 Hz   | 1.41 | 0.5 dB   |
| Peaking | 250 Hz   | 1.41 | 0.1 dB   |
| Peaking | 500 Hz   | 1.41 | -10.6 dB |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.4 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20UR%2020/Koss%20UR%2020.png)