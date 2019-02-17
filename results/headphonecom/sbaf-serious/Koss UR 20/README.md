# Koss UR 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.7; 60 -2.9; 66 -3.5; 72 -3.4; 79 -3.6; 87 -4.4; 96 -5.2; 106 -5.9; 116 -6.4; 128 -6.7; 141 -7.3; 155 -7.7; 170 -7.7; 187 -8.2; 206 -8.5; 227 -8.6; 249 -8.8; 274 -9.9; 302 -10.7; 332 -11.9; 365 -13.2; 402 -14.5; 442 -15.5; 486 -16.0; 535 -16.6; 588 -15.9; 647 -12.9; 712 -10.0; 783 -7.5; 861 -9.1; 947 -8.0; 1042 -5.4; 1146 -3.0; 1261 -1.3; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -2.6; 2031 -6.6; 2234 -7.6; 2457 -5.0; 2703 -5.0; 2973 -1.3; 3270 -0.5; 3597 -2.8; 3957 -6.5; 4353 -5.8; 4788 -7.7; 5267 -6.4; 5793 -10.9; 6373 -9.6; 7010 -8.9; 7711 -10.0; 8482 -10.7; 9330 -9.7; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss UR 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss UR 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.66 | 6.8 dB   |
| Peaking | 488 Hz   | 1.14 | -10.4 dB |
| Peaking | 1397 Hz  | 1.98 | 8.1 dB   |
| Peaking | 3249 Hz  | 4.98 | 7.1 dB   |
| Peaking | 7311 Hz  | 1.32 | -3.8 dB  |
| Peaking | 760 Hz   | 5.26 | 5.3 dB   |
| Peaking | 764 Hz   | 2.35 | -2.8 dB  |
| Peaking | 1756 Hz  | 7.91 | 2.6 dB   |
| Peaking | 2139 Hz  | 8.88 | -4.0 dB  |
| Peaking | 11187 Hz | 4.84 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB   |
| Peaking | 62 Hz    | 1.41 | 3.2 dB   |
| Peaking | 125 Hz   | 1.41 | -0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -11.6 dB |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB  |
| Peaking | 16000 Hz | 1.41 | 0.6 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20UR%2020/Koss%20UR%2020.png)