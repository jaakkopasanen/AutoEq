# Westone UM3X RC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.6; 25 -4.9; 28 -5.3; 31 -5.6; 34 -5.9; 37 -6.1; 41 -6.4; 45 -6.6; 49 -6.9; 54 -7.2; 60 -7.7; 66 -8.0; 72 -8.2; 79 -8.7; 87 -9.1; 96 -9.4; 106 -9.7; 116 -9.9; 128 -10.2; 141 -10.2; 155 -10.5; 170 -10.7; 187 -10.6; 206 -10.6; 227 -10.5; 249 -10.4; 274 -10.3; 302 -10.0; 332 -9.6; 365 -9.2; 402 -8.8; 442 -8.5; 486 -8.1; 535 -7.6; 588 -7.1; 647 -6.7; 712 -6.4; 783 -6.1; 861 -6.2; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -7.2; 1387 -7.6; 1526 -8.1; 1678 -8.1; 1846 -7.1; 2031 -5.7; 2234 -3.8; 2457 -1.4; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -9.4; 10263 -8.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM3X RC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM3X RC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.5  | 2.9 dB  |
| Peaking | 195 Hz   | 0.42 | -4.4 dB |
| Peaking | 1646 Hz  | 1.29 | -8.1 dB |
| Peaking | 3029 Hz  | 0.37 | 8.4 dB  |
| Peaking | 9402 Hz  | 1.97 | -6.0 dB |
| Peaking | 2606 Hz  | 5.48 | 1.7 dB  |
| Peaking | 4524 Hz  | 0.8  | -1.3 dB |
| Peaking | 6676 Hz  | 1.57 | 3.1 dB  |
| Peaking | 7375 Hz  | 5.01 | -3.6 dB |
| Peaking | 14825 Hz | 1.51 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%20UM3X%20RC/Westone%20UM3X%20RC.png)