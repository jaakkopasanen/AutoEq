# Koss UR-20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -4.0; 25 -4.4; 28 -4.9; 31 -5.2; 34 -5.3; 37 -5.3; 41 -5.2; 45 -5.2; 49 -5.3; 54 -5.4; 60 -5.7; 66 -5.9; 72 -6.1; 79 -6.3; 87 -6.6; 96 -7.0; 106 -7.5; 116 -8.0; 128 -8.4; 141 -8.7; 155 -8.8; 170 -8.9; 187 -8.9; 206 -8.9; 227 -8.6; 249 -8.3; 274 -8.5; 302 -8.8; 332 -9.2; 365 -9.7; 402 -10.2; 442 -10.6; 486 -10.8; 535 -10.3; 588 -9.8; 647 -9.4; 712 -8.7; 783 -7.5; 861 -6.2; 947 -6.8; 1042 -5.7; 1146 -3.4; 1261 -0.9; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -1.0; 2234 -0.8; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -2.5; 3957 -7.9; 4353 -9.1; 4788 -7.6; 5267 -6.7; 5793 -9.0; 6373 -9.2; 7010 -9.3; 7711 -13.8; 8482 -14.7; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss UR-20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss UR-20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 1216 Hz | 0.21 | -6.8 dB |
| Peaking | 1541 Hz | 0.89 | 12.7 dB |
| Peaking | 2968 Hz | 2.21 | 7.5 dB  |
| Peaking | 8127 Hz | 5.34 | -8.4 dB |
| Peaking | 19 Hz   | 1.31 | 3.1 dB  |
| Peaking | 54 Hz   | 1.88 | 1.2 dB  |
| Peaking | 279 Hz  | 4.26 | 1.3 dB  |
| Peaking | 8800 Hz | 7.32 | -2.8 dB |
| Peaking | 9848 Hz | 2.84 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -4.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20UR-20/Koss%20UR-20.png)