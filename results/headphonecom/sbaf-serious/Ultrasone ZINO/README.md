# Ultrasone Zino
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.9; 34 -1.8; 37 -2.8; 41 -3.9; 45 -4.7; 49 -5.3; 54 -5.9; 60 -6.2; 66 -6.4; 72 -6.6; 79 -6.7; 87 -6.7; 96 -6.6; 106 -6.4; 116 -6.2; 128 -5.9; 141 -5.8; 155 -5.5; 170 -5.0; 187 -4.5; 206 -3.8; 227 -3.2; 249 -3.8; 274 -3.5; 302 -2.9; 332 -2.1; 365 -1.4; 402 -0.7; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -3.0; 1042 -6.5; 1146 -9.2; 1261 -11.8; 1387 -13.5; 1526 -14.7; 1678 -16.7; 1846 -18.5; 2031 -19.5; 2234 -17.8; 2457 -10.4; 2703 -11.0; 2973 -10.1; 3270 -9.0; 3597 -8.2; 3957 -4.9; 4353 -9.9; 4788 -6.8; 5267 -5.9; 5793 -9.5; 6373 -9.5; 7010 -5.3; 7711 -7.3; 8482 -12.1; 9330 -16.1; 10263 -14.5; 11289 -8.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Zino GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Zino ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 26 Hz    |  1.54 | 6.9 dB   |
| Peaking | 470 Hz   |  0.88 | 6.5 dB   |
| Peaking | 827 Hz   |  3.21 | 5.4 dB   |
| Peaking | 1837 Hz  |  1.63 | -13.7 dB |
| Peaking | 9596 Hz  |  3.99 | -10.8 dB |
| Peaking | 1283 Hz  |  5.31 | -2.2 dB  |
| Peaking | 2139 Hz  |  7.19 | -8.4 dB  |
| Peaking | 2217 Hz  |  2.77 | 4.6 dB   |
| Peaking | 3876 Hz  | 17.11 | 4.0 dB   |
| Peaking | 12292 Hz |  5.96 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB   |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.9 dB   |
| Peaking | 500 Hz   | 1.41 | 7.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -14.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20Zino/Ultrasone%20Zino.png)