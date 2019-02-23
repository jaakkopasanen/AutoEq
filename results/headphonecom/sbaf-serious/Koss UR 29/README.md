# Koss UR 29
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.3; 54 -2.7; 60 -2.9; 66 -2.7; 72 -3.5; 79 -4.5; 87 -5.2; 96 -5.8; 106 -6.2; 116 -6.5; 128 -6.7; 141 -7.2; 155 -7.3; 170 -7.2; 187 -7.3; 206 -7.5; 227 -7.8; 249 -8.1; 274 -8.2; 302 -8.1; 332 -7.9; 365 -7.8; 402 -7.8; 442 -7.7; 486 -7.9; 535 -8.3; 588 -8.9; 647 -9.8; 712 -9.8; 783 -9.6; 861 -10.2; 947 -10.1; 1042 -9.9; 1146 -9.3; 1261 -9.1; 1387 -9.4; 1526 -9.7; 1678 -10.5; 1846 -12.2; 2031 -12.3; 2234 -11.9; 2457 -9.7; 2703 -7.4; 2973 -5.5; 3270 -4.4; 3597 -2.4; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.4; 8482 -11.8; 9330 -12.2; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss UR 29 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss UR 29 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 32 Hz   | 0.7  | 6.8 dB   |
| Peaking | 1022 Hz | 0.25 | -3.0 dB  |
| Peaking | 2116 Hz | 2.03 | -6.3 dB  |
| Peaking | 4825 Hz | 0.75 | 8.7 dB   |
| Peaking | 8840 Hz | 3.14 | -10.0 dB |
| Peaking | 67 Hz   | 4.15 | 1.1 dB   |
| Peaking | 126 Hz  | 0.97 | -0.7 dB  |
| Peaking | 444 Hz  | 2.2  | 1.3 dB   |
| Peaking | 820 Hz  | 2.25 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20UR%2029/Koss%20UR%2029.png)