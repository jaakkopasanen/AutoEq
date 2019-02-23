# Ultrasone HFi-2400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.4; 25 -2.2; 28 -3.7; 31 -4.9; 34 -5.9; 37 -6.8; 41 -7.8; 45 -8.4; 49 -8.7; 54 -9.2; 60 -9.8; 66 -10.0; 72 -10.2; 79 -10.9; 87 -11.3; 96 -11.3; 106 -11.4; 116 -11.3; 128 -11.2; 141 -11.0; 155 -10.8; 170 -10.4; 187 -10.1; 206 -9.5; 227 -10.1; 249 -10.9; 274 -10.1; 302 -9.4; 332 -8.7; 365 -8.1; 402 -7.9; 442 -7.5; 486 -7.6; 535 -6.6; 588 -6.2; 647 -6.7; 712 -6.8; 783 -6.8; 861 -6.7; 947 -6.3; 1042 -6.7; 1146 -6.3; 1261 -6.2; 1387 -6.2; 1526 -6.0; 1678 -6.3; 1846 -7.1; 2031 -6.6; 2234 -4.2; 2457 -0.5; 2703 -1.9; 2973 -4.4; 3270 -6.9; 3597 -6.7; 3957 -6.0; 4353 -6.9; 4788 -2.4; 5267 -1.3; 5793 -5.1; 6373 -15.1; 7010 -11.0; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.9; 13660 -12.2; 15026 -15.1; 16529 -13.4; 18182 -8.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFi-2400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFi-2400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.21 | 6.9 dB   |
| Peaking | 106 Hz   | 0.41 | -5.0 dB  |
| Peaking | 5562 Hz  | 0.41 | 2.9 dB   |
| Peaking | 6604 Hz  | 7.26 | -12.7 dB |
| Peaking | 15361 Hz | 1.48 | -10.0 dB |
| Peaking | 256 Hz   | 7.68 | -1.4 dB  |
| Peaking | 2094 Hz  | 3.57 | -4.7 dB  |
| Peaking | 2456 Hz  | 3.04 | 9.0 dB   |
| Peaking | 3694 Hz  | 1.11 | -4.2 dB  |
| Peaking | 5159 Hz  | 4.92 | 6.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -8.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFi-2400/Ultrasone%20HFi-2400.png)