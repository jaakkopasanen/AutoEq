# Ultrasone PRO 900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -2.0; 28 -3.0; 31 -3.9; 34 -4.6; 37 -5.2; 41 -5.7; 45 -5.7; 49 -5.6; 54 -5.9; 60 -6.4; 66 -7.0; 72 -7.9; 79 -8.5; 87 -9.1; 96 -9.6; 106 -10.0; 116 -10.3; 128 -10.1; 141 -10.1; 155 -9.9; 170 -9.2; 187 -8.8; 206 -7.3; 227 -5.4; 249 -3.2; 274 -0.5; 302 -1.6; 332 -4.3; 365 -5.5; 402 -6.1; 442 -5.9; 486 -4.7; 535 -1.9; 588 -3.3; 647 -4.4; 712 -4.2; 783 -4.0; 861 -3.9; 947 -3.4; 1042 -2.8; 1146 -1.9; 1261 -1.8; 1387 -3.2; 1526 -4.1; 1678 -5.0; 1846 -5.0; 2031 -2.9; 2234 -1.7; 2457 -5.6; 2703 -7.7; 2973 -8.3; 3270 -8.6; 3597 -9.3; 3957 -10.5; 4353 -11.4; 4788 -11.4; 5267 -10.0; 5793 -11.5; 6373 -10.5; 7010 -7.9; 7711 -5.7; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -7.5; 13660 -12.3; 15026 -15.0; 16529 -13.7; 18182 -11.0; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.45 | 5.6 dB   |
| Peaking | 125 Hz   | 1.04 | -6.8 dB  |
| Peaking | 1836 Hz  | 0.06 | 3.3 dB   |
| Peaking | 4596 Hz  | 1.1  | -8.8 dB  |
| Peaking | 15990 Hz | 1.02 | -11.0 dB |
| Peaking | 283 Hz   | 3.47 | 9.2 dB   |
| Peaking | 311 Hz   | 1.4  | -4.8 dB  |
| Peaking | 2210 Hz  | 6.55 | 5.5 dB   |
| Peaking | 2575 Hz  | 1.98 | -2.4 dB  |
| Peaking | 3858 Hz  | 2.45 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB   |
| Peaking | 62 Hz    | 1.41 | -0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.1 dB  |
| Peaking | 250 Hz   | 1.41 | 3.0 dB   |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 16000 Hz | 1.41 | -10.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20PRO%20900/Ultrasone%20PRO%20900.png)