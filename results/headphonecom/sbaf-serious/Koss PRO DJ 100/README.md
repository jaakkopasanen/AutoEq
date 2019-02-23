# Koss PRO DJ 100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.2; 37 -1.6; 41 -2.0; 45 -2.5; 49 -2.9; 54 -3.5; 60 -4.2; 66 -4.8; 72 -4.9; 79 -4.7; 87 -5.5; 96 -4.7; 106 -6.5; 116 -7.5; 128 -8.4; 141 -9.1; 155 -9.7; 170 -9.5; 187 -10.3; 206 -10.6; 227 -10.7; 249 -10.7; 274 -10.3; 302 -9.2; 332 -9.1; 365 -9.7; 402 -9.9; 442 -10.5; 486 -11.0; 535 -10.5; 588 -9.8; 647 -9.3; 712 -8.6; 783 -7.5; 861 -6.6; 947 -5.6; 1042 -6.6; 1146 -6.1; 1261 -5.6; 1387 -5.6; 1526 -6.2; 1678 -6.7; 1846 -7.4; 2031 -7.9; 2234 -8.7; 2457 -9.1; 2703 -8.5; 2973 -6.8; 3270 -7.2; 3597 -4.6; 3957 -1.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -9.6; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss PRO DJ 100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss PRO DJ 100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.35 | 6.3 dB  |
| Peaking | 201 Hz  | 0.99 | -4.6 dB |
| Peaking | 504 Hz  | 2.23 | -3.9 dB |
| Peaking | 2543 Hz | 2.61 | -3.6 dB |
| Peaking | 4937 Hz | 1.79 | 7.3 dB  |
| Peaking | 133 Hz  | 6.81 | -0.6 dB |
| Peaking | 1268 Hz | 3    | 1.3 dB  |
| Peaking | 6402 Hz | 6.38 | 2.7 dB  |
| Peaking | 7600 Hz | 4.67 | -1.3 dB |
| Peaking | 9514 Hz | 5.83 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -4.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20PRO%20DJ%20100/Koss%20PRO%20DJ%20100.png)