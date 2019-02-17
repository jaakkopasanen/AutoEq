# Koss PRO DJ 100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.1; 37 -1.5; 41 -2.0; 45 -2.4; 49 -2.8; 54 -3.4; 60 -4.1; 66 -4.7; 72 -4.9; 79 -4.6; 87 -5.4; 96 -4.6; 106 -6.4; 116 -7.4; 128 -8.3; 141 -9.0; 155 -9.6; 170 -9.4; 187 -10.3; 206 -10.5; 227 -10.6; 249 -10.7; 274 -10.2; 302 -9.1; 332 -9.0; 365 -9.7; 402 -9.8; 442 -10.4; 486 -11.0; 535 -10.4; 588 -9.8; 647 -9.3; 712 -8.5; 783 -7.4; 861 -6.5; 947 -5.5; 1042 -6.5; 1146 -6.1; 1261 -5.5; 1387 -5.5; 1526 -6.1; 1678 -6.7; 1846 -7.3; 2031 -7.8; 2234 -8.6; 2457 -9.0; 2703 -8.5; 2973 -6.7; 3270 -7.1; 3597 -4.6; 3957 -1.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -9.5; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 20 Hz   | 0.35 | 6.2 dB  |
| Peaking | 202 Hz  | 0.99 | -4.5 dB |
| Peaking | 503 Hz  | 2.28 | -3.8 dB |
| Peaking | 2542 Hz | 2.7  | -3.6 dB |
| Peaking | 4935 Hz | 1.78 | 7.2 dB  |
| Peaking | 135 Hz  | 6.74 | -0.6 dB |
| Peaking | 1263 Hz | 2.87 | 1.4 dB  |
| Peaking | 6405 Hz | 6.32 | 2.7 dB  |
| Peaking | 7563 Hz | 4.37 | -1.3 dB |
| Peaking | 9626 Hz | 5.89 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20PRO%20DJ%20100/Koss%20PRO%20DJ%20100.png)