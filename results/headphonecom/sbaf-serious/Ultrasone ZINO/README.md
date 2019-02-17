# Ultrasone Zino
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -1.0; 31 -2.1; 34 -3.3; 37 -4.3; 41 -5.3; 45 -6.1; 49 -6.7; 54 -7.3; 60 -7.7; 66 -7.8; 72 -8.0; 79 -8.1; 87 -8.2; 96 -8.0; 106 -7.8; 116 -7.7; 128 -7.4; 141 -7.2; 155 -6.9; 170 -6.5; 187 -6.0; 206 -5.3; 227 -4.6; 249 -5.2; 274 -4.9; 302 -4.4; 332 -3.6; 365 -2.8; 402 -2.2; 442 -1.5; 486 -0.7; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.8; 947 -4.4; 1042 -8.0; 1146 -10.6; 1261 -13.3; 1387 -15.0; 1526 -16.1; 1678 -18.1; 1846 -19.9; 2031 -21.0; 2234 -19.3; 2457 -11.9; 2703 -12.4; 2973 -11.6; 3270 -10.5; 3597 -9.7; 3957 -6.3; 4353 -11.3; 4788 -8.2; 5267 -7.3; 5793 -10.9; 6373 -11.0; 7010 -6.8; 7711 -8.7; 8482 -13.5; 9330 -17.5; 10263 -16.0; 11289 -10.4; 12418 -6.6; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Zino GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Zino ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 2.33 | 6.6 dB   |
| Peaking | 661 Hz   | 0.99 | 9.0 dB   |
| Peaking | 1803 Hz  | 1.3  | -15.5 dB |
| Peaking | 9592 Hz  | 3.37 | -12.0 dB |
| Peaking | 19866 Hz | 2.87 | -3.9 dB  |
| Peaking | 74 Hz    | 1.82 | -1.8 dB  |
| Peaking | 116 Hz   | 2.25 | -1.2 dB  |
| Peaking | 863 Hz   | 6.72 | 2.6 dB   |
| Peaking | 1092 Hz  | 4.79 | -1.2 dB  |
| Peaking | 1258 Hz  | 7.4  | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB   |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB   |
| Peaking | 500 Hz   | 1.41 | 7.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -15.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -6.6 dB  |
| Peaking | 16000 Hz | 1.41 | 0.2 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20Zino/Ultrasone%20Zino.png)