# Koss KDE250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.8; 187 -1.5; 206 -2.0; 227 -2.5; 249 -3.2; 274 -3.8; 302 -4.1; 332 -4.3; 365 -4.5; 402 -4.4; 442 -4.5; 486 -4.2; 535 -4.3; 588 -4.2; 647 -4.3; 712 -4.3; 783 -4.5; 861 -4.8; 947 -5.3; 1042 -6.0; 1146 -6.6; 1261 -7.6; 1387 -9.2; 1526 -11.4; 1678 -13.2; 1846 -14.6; 2031 -16.9; 2234 -20.2; 2457 -21.9; 2703 -20.0; 2973 -18.1; 3270 -12.9; 3597 -7.2; 3957 -4.0; 4353 -0.7; 4788 -0.7; 5267 -3.1; 5793 -3.1; 6373 -4.9; 7010 -9.6; 7711 -13.6; 8482 -14.0; 9330 -12.0; 10263 -10.8; 11289 -11.3; 12418 -11.3; 13660 -7.6; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KDE250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KDE250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 55 Hz    | 0.2  | 6.4 dB   |
| Peaking | 971 Hz   | 0.92 | 5.0 dB   |
| Peaking | 2560 Hz  | 1.06 | -23.0 dB |
| Peaking | 4577 Hz  | 0.99 | 17.3 dB  |
| Peaking | 8502 Hz  | 1.2  | -10.1 dB |
| Peaking | 157 Hz   | 4.47 | 1.0 dB   |
| Peaking | 6369 Hz  | 4.45 | 5.0 dB   |
| Peaking | 7200 Hz  | 1.41 | -5.6 dB  |
| Peaking | 10468 Hz | 0.83 | 5.4 dB   |
| Peaking | 12037 Hz | 2.43 | -6.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 4.2 dB   |
| Peaking | 125 Hz   | 1.41 | 5.4 dB   |
| Peaking | 250 Hz   | 1.41 | 2.2 dB   |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -16.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20KDE250/Koss%20KDE250.png)