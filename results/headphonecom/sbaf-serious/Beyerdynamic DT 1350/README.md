# Beyerdynamic DT 1350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -7.9; 25 -8.0; 28 -8.0; 31 -8.1; 34 -8.2; 37 -8.3; 41 -8.3; 45 -8.3; 49 -8.4; 54 -8.2; 60 -8.2; 66 -8.6; 72 -8.8; 79 -8.9; 87 -8.5; 96 -7.7; 106 -7.1; 116 -7.7; 128 -7.8; 141 -6.9; 155 -7.2; 170 -8.2; 187 -9.5; 206 -10.1; 227 -10.3; 249 -10.5; 274 -10.2; 302 -9.9; 332 -10.6; 365 -10.8; 402 -10.4; 442 -10.6; 486 -10.7; 535 -10.3; 588 -9.7; 647 -9.2; 712 -8.2; 783 -7.4; 861 -7.4; 947 -7.0; 1042 -6.4; 1146 -5.8; 1261 -5.4; 1387 -5.5; 1526 -5.9; 1678 -6.4; 1846 -6.3; 2031 -5.2; 2234 -3.1; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.4; 4353 -4.5; 4788 -4.1; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.7; 8482 -13.6; 9330 -15.5; 10263 -8.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 44 Hz   | 0.66 | -1.9 dB  |
| Peaking | 362 Hz  | 0.78 | -4.5 dB  |
| Peaking | 2996 Hz | 1.63 | 6.6 dB   |
| Peaking | 6066 Hz | 2.69 | 6.3 dB   |
| Peaking | 8994 Hz | 4.41 | -11.4 dB |
| Peaking | 151 Hz  | 4.15 | 1.5 dB   |
| Peaking | 200 Hz  | 3.78 | -1.4 dB  |
| Peaking | 1292 Hz | 2.26 | 1.9 dB   |
| Peaking | 1841 Hz | 1.69 | -1.9 dB  |
| Peaking | 2406 Hz | 6.11 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -3.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%201350/Beyerdynamic%20DT%201350.png)