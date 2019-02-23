# Ultrasone Signature Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.9; 25 -8.3; 28 -8.8; 31 -9.3; 34 -9.6; 37 -9.9; 41 -10.3; 45 -10.6; 49 -10.8; 54 -10.9; 60 -10.8; 66 -10.9; 72 -9.7; 79 -7.8; 87 -10.0; 96 -12.7; 106 -13.8; 116 -13.3; 128 -13.6; 141 -14.5; 155 -14.3; 170 -12.6; 187 -13.3; 206 -12.2; 227 -10.7; 249 -9.3; 274 -8.1; 302 -7.4; 332 -7.2; 365 -7.3; 402 -7.5; 442 -7.8; 486 -8.2; 535 -8.3; 588 -8.4; 647 -8.3; 712 -7.9; 783 -8.0; 861 -7.8; 947 -7.6; 1042 -6.9; 1146 -6.3; 1261 -6.8; 1387 -7.7; 1526 -8.1; 1678 -7.0; 1846 -5.1; 2031 -3.6; 2234 -2.5; 2457 -1.1; 2703 -1.2; 2973 -1.0; 3270 -1.3; 3597 -1.6; 3957 -1.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -5.8; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -10.8; 10263 -11.9; 11289 -11.4; 12418 -10.9; 13660 -8.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Signature Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Signature Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 1.27 | -3.5 dB |
| Peaking | 142 Hz   | 1.02 | -7.7 dB |
| Peaking | 2656 Hz  | 2.67 | 4.7 dB  |
| Peaking | 4879 Hz  | 1.4  | 6.5 dB  |
| Peaking | 10789 Hz | 1.67 | -6.5 dB |
| Peaking | 80 Hz    | 5.56 | 5.8 dB  |
| Peaking | 81 Hz    | 2.09 | -2.9 dB |
| Peaking | 312 Hz   | 3.06 | 1.7 dB  |
| Peaking | 640 Hz   | 1.41 | -1.6 dB |
| Peaking | 1505 Hz  | 6.24 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -7.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20Signature%20Pro/Ultrasone%20Signature%20Pro.png)