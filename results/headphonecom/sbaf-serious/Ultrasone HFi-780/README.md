# Ultrasone HFi-780
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.3; 45 -2.0; 49 -2.4; 54 -2.9; 60 -3.7; 66 -3.9; 72 -3.7; 79 -3.6; 87 -3.6; 96 -3.8; 106 -3.8; 116 -3.6; 128 -3.2; 141 -2.9; 155 -2.7; 170 -2.0; 187 -1.8; 206 -1.2; 227 -2.9; 249 -4.8; 274 -6.3; 302 -8.3; 332 -9.7; 365 -10.0; 402 -10.6; 442 -10.7; 486 -10.5; 535 -10.0; 588 -9.5; 647 -9.1; 712 -8.9; 783 -8.9; 861 -9.1; 947 -9.4; 1042 -9.6; 1146 -8.9; 1261 -10.0; 1387 -10.9; 1526 -11.4; 1678 -11.5; 1846 -11.1; 2031 -10.6; 2234 -1.5; 2457 -4.8; 2703 -6.4; 2973 -6.7; 3270 -7.3; 3597 -8.4; 3957 -7.1; 4353 -3.2; 4788 -5.6; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.7; 9330 -10.5; 10263 -12.2; 11289 -9.1; 12418 -7.6; 13660 -7.0; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFi-780 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFi-780 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.17 | 6.3 dB  |
| Peaking | 191 Hz   | 1.52 | 7.7 dB  |
| Peaking | 480 Hz   | 0.28 | -4.4 dB |
| Peaking | 5871 Hz  | 2.49 | 7.1 dB  |
| Peaking | 10070 Hz | 3.27 | -6.5 dB |
| Peaking | 398 Hz   | 1.64 | -2.7 dB |
| Peaking | 1023 Hz  | 0.32 | 2.3 dB  |
| Peaking | 1797 Hz  | 1.5  | -5.8 dB |
| Peaking | 2300 Hz  | 7.88 | 9.6 dB  |
| Peaking | 3655 Hz  | 7.92 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | 3.5 dB  |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -4.7 dB |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFi-780/Ultrasone%20HFi-780.png)