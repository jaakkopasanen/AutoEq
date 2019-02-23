# Beyerdynamic DT 231
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.7; 96 -1.3; 106 -2.3; 116 -2.8; 128 -3.4; 141 -3.9; 155 -4.3; 170 -4.4; 187 -3.9; 206 -4.1; 227 -4.4; 249 -4.8; 274 -5.1; 302 -5.3; 332 -5.6; 365 -5.9; 402 -6.2; 442 -6.3; 486 -6.7; 535 -6.9; 588 -7.1; 647 -7.6; 712 -7.8; 783 -8.6; 861 -9.1; 947 -9.3; 1042 -9.1; 1146 -8.5; 1261 -8.0; 1387 -8.2; 1526 -10.5; 1678 -13.7; 1846 -13.8; 2031 -10.1; 2234 -7.2; 2457 -4.2; 2703 -1.9; 2973 -0.5; 3270 -0.8; 3597 -1.5; 3957 -0.5; 4353 -5.2; 4788 -13.1; 5267 -10.8; 5793 -6.3; 6373 -5.8; 7010 -8.6; 7711 -12.3; 8482 -12.8; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -7.6; 13660 -15.3; 15026 -16.9; 16529 -13.5; 18182 -11.1; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 231 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 231 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.33 | 6.5 dB   |
| Peaking | 1817 Hz  | 1.58 | -9.5 dB  |
| Peaking | 3071 Hz  | 1.32 | 9.5 dB   |
| Peaking | 4947 Hz  | 6.26 | -10.0 dB |
| Peaking | 15524 Hz | 1.01 | -9.8 dB  |
| Peaking | 884 Hz   | 1.96 | -2.1 dB  |
| Peaking | 1376 Hz  | 4.86 | 2.7 dB   |
| Peaking | 6224 Hz  | 5.1  | 2.3 dB   |
| Peaking | 8067 Hz  | 3.71 | -7.2 dB  |
| Peaking | 11004 Hz | 2.59 | 4.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB   |
| Peaking | 62 Hz    | 1.41 | 5.4 dB   |
| Peaking | 125 Hz   | 1.41 | 2.3 dB   |
| Peaking | 250 Hz   | 1.41 | 1.3 dB   |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB  |
| Peaking | 16000 Hz | 1.41 | -10.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20231/Beyerdynamic%20DT%20231.png)